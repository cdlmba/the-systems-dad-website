import os
import glob
from datetime import datetime

CLS_DOMAIN = "https://christopherlynnsystems.com"
TSD_DOMAIN = "https://thesystemsdad.com"
OUTPUT_CLS = "sitemap.xml"
OUTPUT_CLS_VAULT = os.path.join("vault_cls", "sitemap.xml")
OUTPUT_TSD = "sitemap-tsd.xml"
OUTPUT_TSD_VAULT = os.path.join("vault_tsd", "sitemap.xml")
OUTPUT_TSD_ROBOTS = os.path.join("vault_tsd", "robots.txt")

# Off-brand, POC, or redirect-only pages — not in the public CLS sitemap.
# Legal pages (privacy/terms/disclaimer) are live public URLs and must be listed.
CLS_EXCLUDE = {
    "index.html",
    "shop.html",
    "dad-mode-kit.html",
    "systems-dad-reset-bundle.html",
    "pool.html",
}
TSD_EXCLUDE = {
    "residue-audit.html",
    "dad-mode-kit.html",
    "home-os.html",
    "shop.html",
    "transition-ritual.html",
    "work-brain-reset.html",
    "stewardship-briefing.html",
    "936.html",
    "trenches-kit-sources.html",
    "implementation-bridge.html",
    "hangar.html",
    "assessment.html",
    "evening-shutdown.html",
    "family-cadence.html",
    "field-manual.html",
    "house-board.html",
    "premium-briefing.html",
    "speaking.html",
}

def create_sitemap_xml(urls):
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    today = datetime.now().strftime("%Y-%m-%d")
    for url in urls:
        xml += "  <url>\n"
        xml += f"    <loc>{url}</loc>\n"
        xml += f"    <lastmod>{today}</lastmod>\n"
        xml += "    <changefreq>weekly</changefreq>\n"
        xml += "    <priority>0.8</priority>\n"
        xml += "  </url>\n"
    xml += "</urlset>\n"
    return xml

def html_to_clean_url(domain, rel_path):
    rel_path = rel_path.replace("\\", "/")
    if rel_path.endswith("/index.html") or rel_path == "index.html":
        return f"{domain}/"
    if rel_path.endswith(".html"):
        rel_path = rel_path[:-5]
    return f"{domain}/{rel_path}"

def collect_cls_urls():
    urls = []
    seen = set()

    def add(url):
        if url not in seen:
            seen.add(url)
            urls.append(url)

    add(f"{CLS_DOMAIN}/")

    for path in glob.glob(os.path.join("vault_cls", "*.html")):
        filename = os.path.basename(path)
        if filename in CLS_EXCLUDE or filename.startswith("_"):
            continue
        add(html_to_clean_url(CLS_DOMAIN, filename))

    for path in glob.glob(os.path.join("vault_cls", "blog", "*.html")):
        filename = os.path.basename(path)
        add(html_to_clean_url(CLS_DOMAIN, f"blog/{filename}"))

    return urls

def collect_tsd_urls():
    urls = []
    seen = set()

    def add(url):
        if url not in seen:
            seen.add(url)
            urls.append(url)

    add(f"{TSD_DOMAIN}/")

    for path in glob.glob(os.path.join("vault_tsd", "*.html")):
        filename = os.path.basename(path)
        if filename.startswith("_") or filename in TSD_EXCLUDE:
            continue
        add(html_to_clean_url(TSD_DOMAIN, filename))

    for path in glob.glob(os.path.join("vault_tsd", "blog", "*.html")):
        filename = os.path.basename(path)
        add(html_to_clean_url(TSD_DOMAIN, f"blog/{filename}"))

    return urls

def build_sitemaps():
    import sys
    import io
    if sys.platform == "win32":
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

    print("Starting Sitemap Build Process...")
    cls_urls = collect_cls_urls()
    tsd_urls = collect_tsd_urls()

    cls_xml = create_sitemap_xml(cls_urls)
    with open(OUTPUT_CLS, "w", encoding="utf-8") as f:
        f.write(cls_xml)
    with open(OUTPUT_CLS_VAULT, "w", encoding="utf-8") as f:
        f.write(cls_xml)
    print(f"Generated CLS Sitemap: {OUTPUT_CLS} ({len(cls_urls)} URLs)")

    tsd_xml = create_sitemap_xml(tsd_urls)
    with open(OUTPUT_TSD, "w", encoding="utf-8") as f:
        f.write(tsd_xml)
    with open(OUTPUT_TSD_VAULT, "w", encoding="utf-8") as f:
        f.write(tsd_xml)
    print(f"Generated TSD Sitemap: {OUTPUT_TSD} & {OUTPUT_TSD_VAULT} ({len(tsd_urls)} URLs)")

    tsd_robots = f"User-agent: *\nAllow: /\n\nSitemap: {TSD_DOMAIN}/sitemap.xml\n"
    with open(OUTPUT_TSD_ROBOTS, "w", encoding="utf-8") as f:
        f.write(tsd_robots)
    print(f"Generated TSD Robots.txt: {OUTPUT_TSD_ROBOTS}")

if __name__ == "__main__":
    build_sitemaps()
