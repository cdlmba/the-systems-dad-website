import os
import glob
import markdown
import frontmatter
from datetime import datetime
import sys
import json
import argparse


# CONFIGURATION
POSTS_DIR = '_posts'
OUTPUT_DIR = 'blog'
TSD_OUTPUT_DIR = 'vault_tsd'
TEMPLATES_DIR = 'templates'
COMPONENTS_DIR = 'components'
INDEX_OUTPUT = 'blog.html'
TSD_INDEX_OUTPUT = os.path.join(TSD_OUTPUT_DIR, 'blog.html')
MR_INDEX_OUTPUT = os.path.join('vault_mr', 'blog.html')

def load_text(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def load_global_config():
    if os.path.exists('site-config.json'):
        with open('site-config.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def load_components():
    components = {}
    # Recursively load all .html files from components directory and its subdirectories
    for root, dirs, files in os.walk(COMPONENTS_DIR):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                name = file.replace('.html', '').replace('-', '_')
                components[name] = load_text(file_path)
    
    # Explicit brand heads to guarantee clean measurement-ID isolation
    if os.path.exists(os.path.join(COMPONENTS_DIR, 'cls', 'head.html')):
        components['head_cls'] = load_text(os.path.join(COMPONENTS_DIR, 'cls', 'head.html'))
    if os.path.exists(os.path.join(COMPONENTS_DIR, 'tsd', 'head.html')):
        components['head_tsd'] = load_text(os.path.join(COMPONENTS_DIR, 'tsd', 'head.html'))
    if os.path.exists(os.path.join(COMPONENTS_DIR, 'mr', 'head.html')):
        components['head_mr'] = load_text(os.path.join(COMPONENTS_DIR, 'mr', 'head.html'))
    
    # Also load base head if it was moved to shared
    if 'head' not in components and os.path.exists('head.html'):
        components['head'] = load_text('head.html')
    
    return components

def fix_path(path, root_depth=0):
    if path.startswith('http') or path.startswith('//') or path.startswith('mailto:'):
        return path
    prefix = '../' * root_depth
    return prefix + path

def inject_components(html, components, global_vars=None, global_config=None):
    # First inject actual components
    for name, content in components.items():
        placeholder = f'{{{{{name}}}}}'
        html = html.replace(placeholder, content)
    
    # Then inject global configuration ({{global_...}}) from the 'globals' key
    if global_config and 'globals' in global_config:
        for key, value in global_config['globals'].items():
            placeholder = f'{{{{global_{key}}}}}'
            html = html.replace(placeholder, str(value))
    
    # Finally inject specific override variables (like root_path, title, description)
    if global_vars:
        for name, value in global_vars.items():
            placeholder = f'{{{{{name}}}}}'
            html = html.replace(placeholder, str(value))
            
    return html

def build_blog():
    # Force UTF-8 encoding for Windows terminals
    if sys.platform == 'win32':
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        
    parser = argparse.ArgumentParser(description='Build Multi-Brand Blog.')
    parser.add_argument('--version', default='2', help='Build version for cache busting')
    args = parser.parse_args()
    build_version = args.version
    
    print(f"🚀 Starting Multi-Brand Blog Build Process (v{build_version})...")
    
    components = load_components()
    global_config = load_global_config()
    
    # 1. Get all markdown files
    post_files = glob.glob(os.path.join(POSTS_DIR, '*.md'))
    posts = []

    if not post_files:
        print("No posts found in /_posts. Add some markdown files first!")
        return

    # 2. Parse all posts
    for file_path in post_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
            
            if 'title' not in post.metadata:
                print(f"Skipping {file_path}: Missing 'title' in frontmatter")
                continue
            
            filename = os.path.basename(file_path)
            slug = filename.replace('.md', '')
            
            html_content = markdown.markdown(post.content)
            
            # Normalize date to datetime object
            date_val = post.metadata.get('date', datetime.min)
            if isinstance(date_val, str):
                try:
                    date_val = datetime.strptime(date_val, '%Y-%m-%d')
                except ValueError:
                    date_val = datetime.min
            elif not isinstance(date_val, datetime):
                date_val = datetime.combine(date_val, datetime.min.time())
            
            # CATEGORY LOGIC: Support both 'category' (singular) and 'categories' (plural/list)
            raw_category = post.metadata.get('category', post.metadata.get('categories', 'General'))
            
            # If it's a list, we check if it contains our brands, otherwise join it
            if isinstance(raw_category, list):
                if 'The Systems Dad' in raw_category:
                    brand_category = 'The Systems Dad'
                elif any(c in ['Professional Architecture', 'AI-PM', 'Leadership', 'Systems'] for c in raw_category):
                    brand_category = 'Professional Education'
                else:
                    brand_category = raw_category[0] if raw_category else 'General'
            else:
                brand_category = str(raw_category)
            
            post_data = {
                'metadata': post.metadata,
                'content': html_content,
                'slug': slug,
                'url': f'blog/{slug}',
                'date_obj': date_val,
                'brand_category': brand_category
            }
            posts.append(post_data)

    # 3. Sort by date (Newest first)
    posts.sort(key=lambda x: x['date_obj'], reverse=True)

    # 4. Generate Individual Post Pages
    post_template = load_text(os.path.join(TEMPLATES_DIR, 'blog_post_template.html'))
    
    import shutil
    blog_dirs = [
        os.path.join('vault_tsd', 'blog'),
        os.path.join('vault_mr', 'blog'),
        os.path.join('vault_cls', 'blog')
    ]
    for d in blog_dirs:
        if os.path.exists(d):
            shutil.rmtree(d, ignore_errors=True)
        os.makedirs(d, exist_ok=True)

    for post in posts:
        output_html = post_template
        # (title/description now handled by inject_components)
        output_html = output_html.replace('{{date}}', str(post['metadata'].get('date', '')))
        
        category = post['brand_category']
        output_html = output_html.replace('{{category}}', category)
        
        # CATEGORY-BASED BRAND SKINNING
        if category == 'The Systems Dad':
            body_class = "brand-tsd"
            back_link = "{{root_path}}blog.html"
            back_text = "← Back to Essays"
        else:
            body_class = ""
            back_link = "{{root_path}}blog.html"
            back_text = "← Back to Blog"

        output_html = output_html.replace('{{body_class}}', body_class)
        output_html = output_html.replace('{{back_link}}', back_link)
        output_html = output_html.replace('{{back_text}}', back_text)
        output_html = output_html.replace('{{content}}', post['content'])
        
        # BRAND-AWARE COMPONENT INJECTION
        # If the post is TSD brand, use TSD headers in the individual post
        if category == 'The Systems Dad':
            output_html = output_html.replace('{{header}}', components.get('header_tsd', ''))
            output_html = output_html.replace('{{footer}}', components.get('footer_tsd', ''))
            
            # TSD Specific CTA Box
            cta_box = f"""
            <div class="cta-box" style="margin-top: 3rem; background: var(--background-secondary); padding: 2rem; border-radius: 0.5rem; text-align: center; border: 1px solid var(--border-color);">
                <h3 style="margin-bottom: 1rem;">Reclaim 10 Hours This Week</h3>
                <p style="margin-bottom: 1.5rem; color: var(--text-color-muted);">Stop letting the chaos run your home. Let's install the architectural systems you use at work in your household.</p>
                <a href="https://tidycal.com/christopherlynnsystems/30-minute-meeting?utm_source=tsd_blog&utm_content={post['slug']}" target="_blank" class="cta-button cta-button-primary">Reclaim 10 Hours This Week \u2192</a>
            </div>
            """
            output_html = output_html.replace('{{cta_box}}', cta_box)
        else:
            output_html = output_html.replace('{{header}}', components.get('header_cls', ''))
            output_html = output_html.replace('{{footer}}', components.get('footer_cls', ''))
            
            # CLS Specific CTA Box
            cta_box = f"""
            <div class="cta-box" style="margin-top: 3rem; background: var(--primary-glow-light); padding: 2rem; border-radius: 0.5rem; text-align: center; border: 1px solid var(--primary-color);">
                <h3 style="margin-bottom: 1rem;">Run Your CEO Systems Audit</h3>
                <p style="margin-bottom: 1.5rem; color: var(--text-color-muted);">Stop managing and start leading. Let's build a high-velocity system for your organization.</p>
                <a href="https://tidycal.com/christopherlynnsystems/30-minute-meeting?utm_source=cls_blog&utm_content={post['slug']}" target="_blank" class="cta-button cta-button-primary" style="background: var(--primary-color); border-color: var(--primary-color);">Run Your CEO Systems Audit \u2192</a>
            </div>
            """
            output_html = output_html.replace('{{cta_box}}', cta_box)
            
        og_img_raw = post['metadata'].get('image', 'images/systems_dad_cover_hero.png')
        og_img = og_img_raw if og_img_raw.startswith(('http', '//')) else og_img_raw.lstrip('/')
        post_vars = {
            'root_path': '../', 
            'og_image': og_img, 
            'slug': f"blog/{post['slug']}",
            'title': post['metadata'].get('title', 'Untitled'),
            'description': post['metadata'].get('description', ''),
            'favicon_url': '/images/tsd-favicon.png' if category == 'The Systems Dad' else '/images/HeadshotThumbnail.png',
            'robots_meta': '<meta name="robots" content="index, follow">'
        }

        
        # Determine destination paths and brand heads
        dest_configs = [
            (os.path.join('vault_mr', 'blog', f"{post['slug']}.html"), 'head_mr')
        ]
        if category == 'The Systems Dad':
            dest_configs.append((os.path.join('vault_tsd', 'blog', f"{post['slug']}.html"), 'head_tsd'))
        else:
            dest_configs.append((os.path.join('vault_cls', 'blog', f"{post['slug']}.html"), 'head_cls'))

        for dest_path, head_key in dest_configs:
            brand_components = dict(components)
            if head_key in brand_components:
                brand_components['head'] = brand_components[head_key]
            
            rendered_post_html = inject_components(output_html, brand_components, global_vars=post_vars, global_config=global_config)
            # Path repairs for items not covered by {{root_path}} (local images inside content)
            rendered_post_html = rendered_post_html.replace('src="images/', 'src="../images/')
            rendered_post_html = rendered_post_html.replace('url(\'images/', 'url(\'../images/')
            
            with open(dest_path, 'w', encoding='utf-8') as f:
                f.write(rendered_post_html)
            print(f"Generated Post: {dest_path}")

    # 5. Generate Indices
    
    # A. Professional Index (blog.html)
    cls_index_template = load_text(os.path.join(TEMPLATES_DIR, 'blog_index_template.html'))
    
    # B. Personal Index (tsd/blog.html)
    tsd_index_template = load_text(os.path.join(TEMPLATES_DIR, 'blog_index_tsd_template.html'))
    
    # C. MarginReset Index (vault_mr/blog.html)
    mr_index_template = load_text(os.path.join(TEMPLATES_DIR, 'blog_index_mr_template.html'))
    
    
    # RE-RENDER Post List for CLS
    cls_posts_html = ""
    visible_index = 0
    for post in posts:
        if post['brand_category'] == 'The Systems Dad':
            continue  # STRICT SEGMENTATION: No personal content on professional site
            
        card_class = "blog-card featured-post" if visible_index == 0 else "blog-card"
        visible_index += 1
        raw_img = post['metadata'].get('image', 'images/cls-margin-hero.jpg')
        image_url = raw_img if raw_img.startswith(('http', '//')) else '/' + raw_img.lstrip('/')
        post_url = "{{root_path}}" + post['url']
        
        card_html = f"""
        <article class="{card_class}">
            <div class="blog-card-img-wrapper" style="height: 200px; overflow: hidden; background-color: var(--background-secondary);">
                <img src="{image_url}" alt="{post['metadata'].get('title')}" class="blog-card-img" loading="lazy" width="400" height="220" style="width: 100%; height: 100%; object-fit: cover; display: block;">
            </div>
            <div class="blog-card-content">
                <div class="blog-card-meta">{post['metadata'].get('date', '')}  {post['brand_category']}</div>
                <h2 class="blog-card-title"><a href="{post_url}">{post['metadata'].get('title')}</a></h2>
                <p class="blog-card-excerpt">{post['metadata'].get('description', '')}</p>
                <a href="{post_url}" class="blog-card-link">Read Article </a>
            </div>
        </article>
        """
        cls_posts_html += card_html
        
    final_cls_html = cls_index_template.replace('{{posts_list}}', cls_posts_html)
    final_cls_html = final_cls_html.replace('{{body_class}}', '') # Default professional brand
    
    global_vars_cls = {
        'root_path': '/', 
        'og_image': 'images/cls-margin-hero.jpg', 
        'slug': 'blog',
        'title': 'The Systems Blog | Christopher Lynn Systems',
        'description': 'Insights on leadership, burnout, and building systems that scale.',
        'favicon_url': '/images/HeadshotThumbnail.png',
        'robots_meta': '<meta name="robots" content="index, follow">'
    }
    
    components_cls = dict(components)
    if 'head_cls' in components_cls:
        components_cls['head'] = components_cls['head_cls']
    final_cls_html = inject_components(final_cls_html, components_cls, global_vars=global_vars_cls, global_config=global_config)
    # Apply versioning to indices
    for asset in ['style.css', 'systems-dad-bot-v4.js', 'core.js']:
        final_cls_html = final_cls_html.replace(f'{asset}', f'{asset}?v={build_version}')

    with open(INDEX_OUTPUT, 'w', encoding='utf-8') as f:
        f.write(final_cls_html)
    cls_vault_index = os.path.join('vault_cls', 'blog.html')
    with open(cls_vault_index, 'w', encoding='utf-8') as f:
        f.write(final_cls_html)
    print(f"Professional Blog Index Updated (Segmented): {INDEX_OUTPUT} and {cls_vault_index}")

    # RE-RENDER Post List for TSD
    tsd_posts_html = ""
    visible_index = 0
    for post in posts:
        if post['brand_category'] != 'The Systems Dad':
            continue  # STRICT SEGMENTATION: No professional content on personal site
            
        card_class = "blog-card featured-post" if visible_index == 0 else "blog-card"
        visible_index += 1
        raw_img = post['metadata'].get('image', 'images/systems_dad_cover_hero.png')
        image_url = raw_img if raw_img.startswith(('http', '//')) else '/' + raw_img.lstrip('/')
        post_url = "{{root_path}}" + post['url']
        
        card_html = f"""
        <article class="{card_class}">
            <div class="blog-card-img-wrapper" style="height: 200px; overflow: hidden; background-color: var(--background-secondary);">
                <img src="{image_url}" alt="{post['metadata'].get('title')}" class="blog-card-img" loading="lazy" width="400" height="220" style="width: 100%; height: 100%; object-fit: cover; display: block;">
            </div>
            <div class="blog-card-content">
                <div class="blog-card-meta">{post['metadata'].get('date', '')}  {post['brand_category']}</div>
                <h2 class="blog-card-title"><a href="{post_url}">{post['metadata'].get('title')}</a></h2>
                <p class="blog-card-excerpt">{post['metadata'].get('description', '')}</p>
                <a href="{post_url}" class="blog-card-link">Read Article </a>
            </div>
        </article>
        """
        tsd_posts_html += card_html

    final_tsd_html = tsd_index_template.replace('{{posts_list}}', tsd_posts_html)
    final_tsd_html = final_tsd_html.replace('{{body_class}}', 'brand-tsd')
    
    global_vars_tsd = {
        'root_path': '/', 
        'og_image': 'images/tsd-margin-hero.jpg', 
        'slug': 'blog',
        'title': 'The Systems Dad Blog | Systems & Rhythms for Intentional Fatherhood',
        'description': 'Tactical systems for the executive dad. High-authority thinking on family, performance, and reclaiming your time.',
        'favicon_url': '/images/tsd-favicon.png',
        'robots_meta': '<meta name="robots" content="index, follow">'
    }
    
    components_tsd = dict(components)
    if 'head_tsd' in components_tsd:
        components_tsd['head'] = components_tsd['head_tsd']
    final_tsd_html = inject_components(final_tsd_html, components_tsd, global_vars=global_vars_tsd, global_config=global_config)
    
    # Minimal repairs
    final_tsd_html = final_tsd_html.replace('src="/systems-dad-bot-v4.js"', 'src="../systems-dad-bot-v4.js"')
    
    # Apply versioning to TSD index
    for asset in ['style.css', 'systems-dad-bot-v4.js', 'core.js']:
        final_tsd_html = final_tsd_html.replace(f'{asset}', f'{asset}?v={build_version}')

    with open(TSD_INDEX_OUTPUT, 'w', encoding='utf-8') as f:
        f.write(final_tsd_html)
    print(f"Personal Blog Index Updated (Segmented): {TSD_INDEX_OUTPUT}")

    # RE-RENDER Post List for MarginReset (Aggregated feed from both brands)
    mr_posts_html = ""
    for post in posts:
        category = post['brand_category']
        
        # Determine category label and meta color for visual separation
        if category == 'The Systems Dad':
            category_label = "The Systems Dad"
            meta_color = "#f59e0b"  # Gold accent
        else:
            category_label = f"Professional Operator ({category})"
            meta_color = "#3b82f6"  # Blue accent
            
        post_url = "{{root_path}}" + post['url']
        date_str = post['metadata'].get('date', '')
        
        card_html = f"""
        <article class="blog-item" style="margin-bottom: 4rem; padding-bottom: 4rem; border-bottom: 1px solid rgba(255,255,255,0.08);">
            <div class="meta" style="color: {meta_color}; font-weight: 700; font-size: 0.9rem; margin-bottom: 0.5rem; text-transform: uppercase; letter-spacing: 0.05em;">{category_label} · {date_str}</div>
            <h2 class="h2" style="font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 800; letter-spacing: -0.02em; line-height: 1.2; margin: 0.5rem 0 1rem;"><a href="{post_url}" style="text-decoration: none; color: white;">{post['metadata'].get('title')}</a></h2>
            <p style="margin-top: 1rem; color: #94a3b8; line-height: 1.7; font-size: 1.05rem;">{post['metadata'].get('description', '')}</p>
            <a href="{post_url}" class="cta-link" style="margin-top: 1.5rem; display: inline-block; color: {meta_color}; text-decoration: none; font-weight: 700; font-size: 0.95rem;">Read Article →</a>
        </article>
        """
        mr_posts_html += card_html

    final_mr_html = mr_index_template.replace('{{posts_list}}', mr_posts_html)
    final_mr_html = final_mr_html.replace('{{body_class}}', 'brand-mr')
    
    global_vars_mr = {
        'root_path': '/', 
        'og_image': 'images/systems_dad_cover_hero.png', 
        'slug': 'blog',
        'title': 'Stories from the Front Door | MarginReset Blog',
        'description': 'Weekly experiments and case studies from executive dads who are reclaiming their presence.',
        'favicon_url': '/images/tsd-favicon.png',
        'robots_meta': '<meta name="robots" content="index, follow">'
    }
    
    components_mr = dict(components)
    if 'head_mr' in components_mr:
        components_mr['head'] = components_mr['head_mr']
    final_mr_html = inject_components(final_mr_html, components_mr, global_vars=global_vars_mr, global_config=global_config)
    
    # Apply versioning to MarginReset index
    for asset in ['style.css', 'systems-dad-bot-v4.js', 'core.js']:
        final_mr_html = final_mr_html.replace(f'{asset}', f'{asset}?v={build_version}')

    with open(MR_INDEX_OUTPUT, 'w', encoding='utf-8') as f:
        f.write(final_mr_html)
    print(f"MarginReset Unified Blog Index Updated: {MR_INDEX_OUTPUT}")

if __name__ == "__main__":
    try:
        build_blog()
    except Exception as e:
        print(f"An error occurred: {e}")
