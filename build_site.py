import os
import sys
import json
import argparse
import shutil

# CONFIGURATION
COMPONENTS_ROOT = 'components'
TEMPLATES_ROOT = 'templates'

# Brand-to-folder mapping
BRAND_CONFIG = {
    'cls': {
        'template_dir': os.path.join(TEMPLATES_ROOT, 'cls'),
        'component_dirs': [
            os.path.join(COMPONENTS_ROOT, 'cls'),
            os.path.join(COMPONENTS_ROOT, 'shared'),
            os.path.join(COMPONENTS_ROOT, 'tsd')
        ],
        'output_prefix': 'vault_cls/'
    },
    'tsd': {
        'template_dir': os.path.join(TEMPLATES_ROOT, 'tsd'),
        'component_dirs': [
            os.path.join(COMPONENTS_ROOT, 'tsd'),
            os.path.join(COMPONENTS_ROOT, 'shared'),
            os.path.join('src', 'protected'),
            os.path.join(COMPONENTS_ROOT, 'cls')
        ],
        'output_prefix': 'vault_tsd/'
    },
    'mr': {
        'template_dir': os.path.join(TEMPLATES_ROOT, 'mr'),
        'component_dirs': [
            os.path.join(COMPONENTS_ROOT, 'mr'),
            os.path.join(COMPONENTS_ROOT, 'shared'),
            os.path.join(COMPONENTS_ROOT, 'tsd'), # Reuse TSD interactive components (audit, eggshell, etc.)
            os.path.join(COMPONENTS_ROOT, 'cls')
        ],
        'output_prefix': 'vault_mr/'
    }
}

def load_site_config():
    try:
        with open('site-config.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Warning: site-config.json not found. Returning empty metadata.")
        return {}

PAGE_METADATA = load_site_config()

import markdown
import frontmatter

def load_all_components(brand):
    """Loads all components available to a specific brand, respecting priority. Supports HTML and Markdown with Frontmatter."""
    components = {}
    dirs = BRAND_CONFIG[brand]['component_dirs']
    md_converter = markdown.Markdown(extensions=['extra', 'nl2br', 'sane_lists'])
    
    # Load in reverse order of priority so high-priority dirs overwrite
    for d in reversed(dirs):
        if not os.path.exists(d):
            continue
        for root, _, files in os.walk(d):
            for f in files:
                base_name = f.replace('.html', '').replace('.md', '').replace('-', '_')
                path = os.path.join(root, f)
                
                content_val = None
                if f.endswith('.html'):
                    with open(path, 'r', encoding='utf-8') as src:
                        content_val = src.read()
                elif f.endswith('.md'):
                    with open(path, 'r', encoding='utf-8') as src:
                        post = frontmatter.load(src)
                        
                        # 1. Store the body as the primary component
                        if post.content:
                            html_text = md_converter.convert(post.content)
                            # Only wrap in markdown-content if it's substantial body text
                            if len(post.content) > 100:
                                content_val = f'<div class="markdown-content brand-markdown">{html_text}</div>'
                            else:
                                # Strip paragraph wrapper for short strings if markdown added them
                                clean_html = html_text.replace('<p>', '').replace('</p>', '') if html_text.count('<p>') == 1 else html_text
                                content_val = clean_html
                        
                        # 2. Map all frontmatter keys to [base_name]_[key]
                        for key, value in post.metadata.items():
                            styled_name = f"{base_name}_{key}"
                            components[styled_name] = str(value)
                            components[styled_name.replace('_', '-')] = str(value)
                
                if content_val is not None:
                    components[base_name] = content_val
                    components[base_name.replace('_', '-')] = content_val
                        
    return components

TSD_HOMEPAGE_ARTIFACT = os.path.join('artifacts', 'tsd-onepager.html')
TSD_HOMEPAGE_DEST = os.path.join('vault_tsd', 'index.html')

def apply_tsd_homepage_artifact():
    """TSD / is a standalone one-pager; do not regenerate from tsd-index.template.html."""
    if not os.path.isfile(TSD_HOMEPAGE_ARTIFACT):
        print(f"Warning: Missing {TSD_HOMEPAGE_ARTIFACT}; TSD homepage not updated.")
        return
    os.makedirs(os.path.dirname(TSD_HOMEPAGE_DEST), exist_ok=True)
    shutil.copy2(TSD_HOMEPAGE_ARTIFACT, TSD_HOMEPAGE_DEST)
    print(f"  ✅ Applied TSD homepage: {TSD_HOMEPAGE_ARTIFACT} → {TSD_HOMEPAGE_DEST}")

def build_brand(brand, args):
    print(f"🛠️ Building Brand: {brand.upper()}")
    
    config = BRAND_CONFIG[brand]
    components = load_all_components(brand)
    is_tsd = (brand == 'tsd')
    is_mr = (brand == 'mr')
    
    if not os.path.exists(config['template_dir']):
        print(f"Error: Template directory {config['template_dir']} not found.")
        return

    for f in os.listdir(config['template_dir']):
        if not f.endswith('.template.html'):
            continue
        if is_tsd and f == 'tsd-index.template.html':
            continue

        template_path = os.path.join(config['template_dir'], f)
        clean_name = f.replace('.template.html', '')
        
        # 1. PATH RESOLUTION LOGIC
        if f == 'margin-first-productivity.template.html':
            output_file = os.path.join(config['output_prefix'], 'margin-first-productivity.html')
        elif is_mr:
            # MR path mapping
            mr_name = clean_name
            output_file = os.path.join(config['output_prefix'], f'{mr_name}.html')
        elif is_tsd:
            # TSD Specific path mapping
            tsd_name = clean_name.replace('tsd-', '')
            if 'agile-at-home' in tsd_name and '-' in tsd_name:
                sub = tsd_name.split('-')[-1]
                if sub == 'dash': 
                    output_file = os.path.join(config['output_prefix'], 'agile-at-home/index.html')
                elif sub in ['m1', 'm2', 'm3', 'm4']:
                    num = sub.replace('m', '')
                    output_file = os.path.join(config['output_prefix'], f'agile-at-home/module-{num}.html')
                elif sub == 'resources':
                    output_file = os.path.join(config['output_prefix'], 'agile-at-home/resources.html')
                else:
                    output_file = os.path.join(config['output_prefix'], f'{tsd_name}.html')
            else:
                output_file = os.path.join(config['output_prefix'], f'{tsd_name}.html')
        else:
            # CLS Path mapping - Output to root for build_dist.py collection
            output_file = f"{config['output_prefix']}{clean_name}.html"

        # Normalize windows paths
        output_file = output_file.replace('\\', '/')



        with open(template_path, 'r', encoding='utf-8') as src:
            content = src.read()
            
        # 2. META & SLUG RESOLUTION
        # Calculate slug relative to brand root for Clean URLs
        clean_slug = output_file.replace(config['output_prefix'], '').replace('.html', '')
        if clean_slug == 'index': clean_slug = ''
        elif clean_slug.endswith('/index'): clean_slug = clean_slug[:-6]
        
        if is_mr:
            default_title = 'MarginReset'
            default_desc = 'The system for the 25 minutes that matter most.'
        elif is_tsd:
            default_title = 'The Systems Dad'
            default_desc = 'Reclaim your presence.'
        else:
            default_title = 'Christopher Lynn Systems'
            default_desc = 'Systems for high-impact leaders.'
        # Standardize metadata key matching for site-config.json
        meta_key_alt = output_file
        if output_file.startswith('vault_mr/'):
            meta_key_alt = output_file.replace('vault_mr/', '_mr/')
        elif output_file.startswith('vault_tsd/'):
            meta_key_alt = output_file.replace('vault_tsd/', '_tsd/')
        elif output_file.startswith('vault_cls/'):
            meta_key_alt = output_file.replace('vault_cls/', '')

        meta = PAGE_METADATA.get(output_file) or PAGE_METADATA.get(meta_key_alt) or {
            'title': default_title,
            'description': default_desc,
            'slug': clean_slug
        }

        # 3. PATH RESOLUTION LOGIC continues...
        
        body_class = 'brand-tsd' if is_tsd else ('brand-mr' if is_mr else '')
        # Force Absolute Pathing for multi-brand/subdirectory architecture
        # Force Root-Relative Pathing for production stability with vanity URLs
        root_path = '/'
        if is_mr:
            base_url = 'https://marginreset.com'
            favicon_val = f'{root_path}images/mr-logo.png'
        elif is_tsd:
            base_url = 'https://thesystemsdad.com'
            favicon_val = f'{root_path}images/tsd-favicon.png'
        else:
            base_url = 'https://christopherlynnsystems.com'
            favicon_val = f'{root_path}images/HeadshotThumbnail.png'
        
        # Build Version for Cache Busting
        build_version = getattr(args, 'version', '2')

        # Special Case: Margin-First Content TSD override
        if is_tsd and 'margin_first_content' in content:
            content = content.replace("{{margin_first_content}}", components.get('margin_first_content_tsd', components.get('margin_first_content', '')))
        
        # Special Case: Agile at Home Module Mapping
        if is_tsd and 'agile_content' in content:
            if 'agile-at-home/index.html' in output_file:
                content = content.replace("{{agile_content}}", components.get('agile_at_home_dash', ''))
            elif 'agile-at-home/module-1.html' in output_file:
                content = content.replace("{{agile_content}}", components.get('agile_at_home_m1', ''))
            elif 'agile-at-home/module-2.html' in output_file:
                content = content.replace("{{agile_content}}", components.get('agile_at_home_m2', ''))
            elif 'agile-at-home/module-3.html' in output_file:
                content = content.replace("{{agile_content}}", components.get('agile_at_home_m3', ''))
            elif 'agile-at-home/module-4.html' in output_file:
                content = content.replace("{{agile_content}}", components.get('agile_at_home_m4', ''))
            elif 'agile-at-home/resources.html' in output_file:
                content = content.replace("{{agile_content}}", components.get('agile_at_home_resources', ''))
        
        # Recursive Component Replacement (up to 3 levels)
        for _ in range(3):
            for p, component_html in components.items():
                content = content.replace(f"{{{{{p}}}}}", component_html)
        
        # Header/Footer Selection
        header_html = components.get('header_tsd' if is_tsd else 'header_cls', '')
        footer_html = components.get('footer_tsd' if is_tsd else 'footer_cls', '')

        # Meta and Brand Injection
        content = content.replace('{{title}}', meta.get('title', ''))
        content = content.replace('{{description}}', meta.get('description', ''))
        content = content.replace('{{slug}}', meta.get('slug', ''))
        content = content.replace('{{og_image}}', f"images/{meta.get('og_image', 'HeadshotThumbnail.png')}")
        content = content.replace('{{favicon_url}}', favicon_val)
        content = content.replace('{{body_class}}', body_class)
        content = content.replace('{{header}}', header_html)
        content = content.replace('{{footer}}', footer_html)
        content = content.replace('{{root_path}}', root_path)

        # Robots Meta Tag Resolution
        noindex_pages = {
            'systems-dad-reset-bundle', 'dad-mode-kit',
            'shop', 'pool', 'trenches-kit-sources', 'implementation-bridge'
        }
        if clean_slug in noindex_pages or clean_name in noindex_pages:
            robots_meta = '<meta name="robots" content="noindex, nofollow">'
        else:
            robots_meta = '<meta name="robots" content="index, follow">'
        content = content.replace('{{robots_meta}}', robots_meta)

        # Global Variable Injection (Run after all components are merged)
        site_globals = PAGE_METADATA.get('globals', {})
        for g_key, g_val in site_globals.items():
            content = content.replace("{{global_" + g_key + "}}", str(g_val))
        
        # Global asset path correction with cache busting
        assets_to_version = [
            'ChristopherLynnHeadshot_v2.jpg', 'tsd-favicon.png', 'HeadshotThumbnail.png', 'mr-logo.png',
            'tsd-margin-hero.jpg', 'cls-margin-hero.jpg', 'tsd-audit-hero.jpg', 'tsd-reset-hero.jpg',
            'systems_dad_presence_split_view_1774573176565.png', 'day3_hub_hero.png',
            'ghost_at_dinner_table_1774490562808.png', 'tsd_presence_handshake_blueprint.png',
            'js/systems-dad-bot-v4.js', 'style.css', 'js/core.js', 'js/stripe-payment-links.js', 'js/checkout.js', 'js/audit.js'
        ]
        for asset in assets_to_version:
            # Special case for root-level assets
            pure_asset = asset.split('/')[-1]
            path_prefix = f"{root_path}" if pure_asset == 'style.css' or asset.startswith('js/') else f"{root_path}images/"
            
            # Match variants: "style.css", "/style.css", "../style.css", "/images/style.css"
            patterns = [f'"{asset}"', f'"{root_path}{asset}"', f'"../{asset}"', f'"{root_path}images/{asset}"']
            for pattern in patterns:
                content = content.replace(f'src={pattern}', f'src="{path_prefix}{asset}?v={build_version}"')
                content = content.replace(f'href={pattern}', f'href="{path_prefix}{asset}?v={build_version}"')
            
            # OG/Twitter meta tags still need the full base_url prefix
            full_prefix = f"{base_url}/" if pure_asset == 'style.css' or asset.startswith('js/') else f"{base_url}/images/"
            content = content.replace(f'content="{base_url}/{asset}"', f'content="{full_prefix}{asset}?v={build_version}"')

        # Canonical and OG URL Hardening
        content = content.replace('https://christopherlynnsystems.com', base_url)

        # Directory correction
        content = content.replace('src="images/', f'src="{root_path}images/')
        content = content.replace('src="../images/', f'src="{root_path}images/')
        content = content.replace("url('images/", f"url('{root_path}images/")
        content = content.replace("url('../images/", f"url('{root_path}images/")
            
        # Ensure output directory exists
        os.makedirs(os.path.dirname(output_file) if '/' in output_file else '.', exist_ok=True)
            
        with open(output_file, 'w', encoding='utf-8') as dest:
            dest.write(content)
        print(f"  ✅ Generated: {output_file}")

def write_stripe_payment_links_js():
    """Emit js/stripe-payment-links.js from site-config globals.stripe_products."""
    globals_cfg = PAGE_METADATA.get('globals', {})
    products = globals_cfg.get('stripe_products', {})
    if not products:
        return
    js_path = os.path.join('js', 'stripe-payment-links.js')
    lines = [
        '/**',
        ' * TSD checkout: productId → Stripe Payment Link URL.',
        ' * Generated from site-config.json globals.stripe_products — do not edit by hand.',
        ' */',
        'window.TSD_STRIPE_PAYMENT_LINKS = ' + json.dumps(products, indent=4) + ';',
        ''
    ]
    os.makedirs('js', exist_ok=True)
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f"  ✅ Generated: {js_path}")


def build_site():
    if sys.platform == 'win32':
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    
    parser = argparse.ArgumentParser(description='Build Christopher Lynn Systems, The Systems Dad, or MarginReset.')
    parser.add_argument('--brand', choices=['cls', 'tsd', 'mr', 'all'], default='all', help='Which brand to build (default: all)')
    parser.add_argument('--version', default='4', help='Build version for cache busting')
    args = parser.parse_args()

    print("🚀 Starting Site Build Process...")
    write_stripe_payment_links_js()

    if args.brand in ['cls', 'all']:
        build_brand('cls', args)
        
    if args.brand in ['tsd', 'all']:
        build_brand('tsd', args)
        apply_tsd_homepage_artifact()

    if args.brand in ['mr', 'all']:
        build_brand('mr', args)

    print("\n✨ Site Build Complete!")


if __name__ == "__main__":
    build_site()
