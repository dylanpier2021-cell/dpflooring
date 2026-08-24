#!/usr/bin/env python3
"""
Pre-deploy audit for the DP Flooring Services site.

    python3 tools/audit.py [dir]

Exits non-zero if anything fails, so it can gate a deploy. Checks every rule the
site is supposed to hold to: unique title/description/H1 per page, sane lengths,
alt text on every image, valid JSON-LD with the required @types, no broken
internal links or missing assets, no unrendered template placeholders, the
service<->location internal linking matrix, click-to-call in header and footer,
minimum word counts on service and location pages, and sitemap completeness.
"""

import html
import json
import os
import re
import sys

ROOT = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else \
       os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {".git", "tools", "assets", "node_modules"}

MIN_WORDS = 1000         # every indexable page (noindex utility pages are exempt)
TITLE_MAX = 70
DESC_MIN, DESC_MAX = 110, 175

fails, warns = [], []
def fail(m): fails.append(m)
def warn(m): warns.append(m)


def pages():
    out = []
    for dp, dirs, fs in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in fs:
            if f.endswith(".html"):
                out.append(os.path.join(dp, f))
    return sorted(out)


def url_of(p):
    rel = os.path.relpath(p, ROOT).replace(os.sep, "/")
    if rel == "index.html": return "/"
    if rel.endswith("/index.html"): return "/" + rel[:-len("index.html")]
    return "/" + rel


def text_of(fragment):
    fragment = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", fragment, flags=re.S)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", fragment))).strip()


def body_words(src):
    head = re.search(r'<section class="pagehead">.*?</section>', src, re.S)
    main = re.search(r'<main id="main">(.*?)</main>', src, re.S)
    hero = re.search(r'<section class="hero">.*?</section>', src, re.S)
    chunk = (head.group(0) if head else "") + (hero.group(0) if hero else "") + \
            (main.group(1) if main else "")
    return len(text_of(chunk).split())


def main():
    ps = pages()
    if not ps:
        fail("no HTML pages found - has the site been built?")
        return

    titles, descs, h1s = {}, {}, {}
    all_links, all_assets = set(), set()
    svc_urls = set(); loc_urls = set()
    docs = {}

    for p in ps:
        src = open(p, encoding="utf-8").read()
        u = url_of(p)
        docs[u] = src
        noindex = 'content="noindex' in src

        if u.startswith("/services/") and u != "/services/": svc_urls.add(u)
        elif re.match(r"^/epoxy-flooring-[a-z-]+-il/$", u): loc_urls.add(u)

        # --- head essentials -------------------------------------------------
        t = re.search(r"<title>(.*?)</title>", src, re.S)
        d = re.search(r'<meta name="description" content="(.*?)"', src, re.S)
        c = re.search(r'<link rel="canonical" href="(.*?)"', src)
        if not t: fail(f"{u}: no <title>")
        if not d: fail(f"{u}: no meta description")
        if not c: fail(f"{u}: no canonical link")
        if t and d and not noindex:
            ti, de = html.unescape(t.group(1)), html.unescape(d.group(1))
            titles.setdefault(ti, []).append(u)
            descs.setdefault(de, []).append(u)
            if len(ti) > TITLE_MAX: fail(f"{u}: title {len(ti)} chars (max {TITLE_MAX})")
            if not DESC_MIN <= len(de) <= DESC_MAX:
                fail(f"{u}: meta description {len(de)} chars (want {DESC_MIN}-{DESC_MAX})")

        h1 = re.findall(r"<h1[^>]*>(.*?)</h1>", src, re.S)
        if len(h1) != 1: fail(f"{u}: {len(h1)} <h1> tags (want exactly 1)")
        elif not noindex: h1s.setdefault(text_of(h1[0]), []).append(u)

        # --- images ----------------------------------------------------------
        for img in re.findall(r"<img\s[^>]*>", src):
            if 'alt="' not in img: fail(f"{u}: <img> with no alt attribute")
            elif re.search(r'alt=""', img) and "aria-hidden" not in img:
                warn(f"{u}: <img> with empty alt (fine only if decorative)")
            if "width=" not in img or "height=" not in img:
                warn(f"{u}: <img> without width/height (causes layout shift)")

        # --- structured data --------------------------------------------------
        types = set()
        for blk in re.findall(r'<script type="application/ld\+json">(.*?)</script>', src, re.S):
            try: data = json.loads(blk)
            except Exception as e:
                fail(f"{u}: invalid JSON-LD ({e})"); continue
            for node in (data if isinstance(data, list) else [data]):
                ty = node.get("@type")
                types.update(ty if isinstance(ty, list) else [ty])
        if u in svc_urls or u in loc_urls:
            if "LocalBusiness" not in types: fail(f"{u}: missing LocalBusiness schema")
            if "Service" not in types and "ItemList" not in types:
                fail(f"{u}: missing Service schema")
        if u == "/faq/" and "FAQPage" not in types: fail(f"{u}: missing FAQPage schema")

        # --- click-to-call, in both header and footer -------------------------
        hdr = re.search(r"<header class=\"header\">.*?</header>", src, re.S)
        ftr = re.search(r'<footer class="footer">.*?</footer>', src, re.S)
        if not (hdr and 'href="tel:' in hdr.group(0)): fail(f"{u}: no click-to-call in header")
        if not (ftr and 'href="tel:' in ftr.group(0)): fail(f"{u}: no click-to-call in footer")

        # --- unrendered template placeholders ---------------------------------
        for m in re.findall(r"\{[A-Za-z_][A-Za-z0-9_\[\]'\"]*\}", src):
            fail(f"{u}: unrendered placeholder {m}")

        # --- word count -------------------------------------------------------
        if not noindex:
            w = body_words(src)
            if w < MIN_WORDS: fail(f"{u}: {w} words (want {MIN_WORDS}+)")

        # --- call-first: the phone has to be impossible to miss ---------------
        if not re.search(r'<section class="callstrip">', src):
            fail(f"{u}: no full-width call strip")
        n_tel = len(re.findall(r'href="tel:', src))
        if n_tel < 5: fail(f"{u}: only {n_tel} click-to-call links (want 5+)")

        # --- epoxy only -------------------------------------------------------
        for term in ("polished concrete", "carpet installation", "tile installation",
                     "hardwood floor", "vinyl plank"):
            if re.search(term, src, re.I):
                fail(f"{u}: mentions non-epoxy service {term!r}")

        for h in re.findall(r'(?:href|src)="(/[^"#?]*)', src):
            (all_assets if re.search(r"\.(png|jpe?g|svg|css|js|ico|webmanifest|xml|txt)$", h)
             else all_links).add(h)

    # --- duplicates ----------------------------------------------------------
    for label, bag in (("title", titles), ("meta description", descs), ("H1", h1s)):
        for val, urls in bag.items():
            if len(urls) > 1: fail(f"duplicate {label} {val[:50]!r} on {urls}")

    # --- link + asset integrity ----------------------------------------------
    for h in sorted(all_links):
        tgt = os.path.join(ROOT, "index.html") if h == "/" else (
              os.path.join(ROOT, h.strip("/"), "index.html") if h.endswith("/")
              else os.path.join(ROOT, h.lstrip("/")))
        if not os.path.exists(tgt): fail(f"broken internal link: {h}")
    for a in sorted(all_assets):
        if not os.path.exists(os.path.join(ROOT, a.lstrip("/"))): fail(f"missing asset: {a}")

    # --- the internal-linking matrix -----------------------------------------
    for s in sorted(svc_urls):
        missing = [l for l in loc_urls if f'href="{l}"' not in docs[s]]
        if missing: fail(f"{s}: does not link {len(missing)} location page(s), e.g. {missing[:2]}")
    for l in sorted(loc_urls):
        missing = [s for s in svc_urls if f'href="{s}"' not in docs[l]]
        if missing: fail(f"{l}: does not link {len(missing)} service page(s), e.g. {missing[:2]}")

    # --- sitemap + robots -----------------------------------------------------
    smp = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(smp): fail("no sitemap.xml")
    else:
        sm = open(smp, encoding="utf-8").read()
        for u, src in docs.items():
            if 'content="noindex' in src: 
                if f"<loc>{'' if u=='/' else ''}" and re.search(rf"<loc>[^<]*{re.escape(u)}</loc>", sm):
                    fail(f"{u}: noindex page is listed in sitemap.xml")
            elif not re.search(rf"<loc>[^<]*{re.escape(u)}</loc>", sm):
                fail(f"{u}: indexable page missing from sitemap.xml")
    rb = os.path.join(ROOT, "robots.txt")
    if not os.path.exists(rb): fail("no robots.txt")
    elif "Sitemap:" not in open(rb, encoding="utf-8").read():
        fail("robots.txt does not point at the sitemap")

    # --- report ---------------------------------------------------------------
    print(f"audited {len(ps)} pages  ({len(svc_urls)} service, {len(loc_urls)} location)")
    for w in warns: print("  warn:", w)
    if fails:
        print(f"\nFAILED - {len(fails)} issue(s):")
        for f in fails: print("  -", f)
        sys.exit(1)
    print(f"\nPASS - no issues ({len(warns)} warning(s))")


main()
