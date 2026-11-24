#!/usr/bin/env python3
"""
Buduje wszystko z build/content.py:
  docs/karty/bryd-N-*.png       karty na telefon, 1080x1920 (9:16)
  docs/karty/karty-do-druku.pdf A4 pionowo, 4 karty na jednej stronie, jasny motyw
  docs/index.html, docs/system/index.html   strona klubu

Wymaga: pip install playwright && playwright install chromium
Użycie:  python build/build.py
Inny Chrome: CHROME_PATH=/ścieżka/do/chrome python build/build.py
"""
import asyncio, html, os, re, shutil, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from content import CARDS, CONVENTIONS, CLUB, CITY_YEAR, Row, Panel, Note  # noqa: E402
from playwright.async_api import async_playwright            # noqa: E402

B = Path(__file__).resolve().parent
ROOT = B.parent
DOCS = ROOT / "docs"
KARTY = DOCS / "karty"
TMP = B / ".tmp"

FONTS = [("Fraunces", "fraunces", (400, 600, 700, 900)),
         ("Source", "source-sans-3", (400, 600, 700))]


SITE_FONTS = FONTS + [("Shantell Sans", "shantell-sans", (500, 700, 800))]


def font_css(base: str, fonts=FONTS) -> str:
    out = []
    for fam, pkg, weights in fonts:
        for w in weights:
            for sub in ("latin", "latin-ext"):
                out.append(f"@font-face{{font-family:'{fam}';font-weight:{w};font-display:swap;"
                           f"src:url('{base}{pkg}-{sub}-{w}-normal.woff2') format('woff2');}}")
    # kolory kart (♠♥♦♣) zawsze z tego samego kroju, niezależnie od systemu
    out.append(f"@font-face{{font-family:'DejaVu Sans';font-display:swap;unicode-range:U+2660,U+2663,U+2665,U+2666;"
               f"src:url('{base}dejavu-sans-suits.woff2') format('woff2');}}")
    return "\n".join(out) + "\n"


# ---------- mini-składnia ----------
def suit(t: str) -> str:
    t = re.sub(r"([♥♦])", r'<span class="s r">\1</span>', t)
    return re.sub(r"([♠♣])", r'<span class="s">\1</span>', t)


def fmt(t: str) -> str:
    t = html.escape(t, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"\{(.+?)\}", r'<span class="pts">\1</span>', t)
    return suit(t).replace("\n", "<br>")


def bid_tile(b: str) -> str:
    if b.startswith("po "):
        return '<span class="po">po</span>' + bid_tile(b[3:])
    cls = "bid" if re.search(r"[♠♥♦♣]|BA|^\d", b) else "bid word"
    return f'<span class="{cls}">{suit(html.escape(b))}</span>'


def render_row(r: Row) -> str:
    bs = r.bid if isinstance(r.bid, list) else [r.bid]
    if len(bs) > 1 and all(re.match(r"^\d[♠♥♦♣]$", x) for x in bs):
        bs = [bs[0][0] + " ".join(x[1] for x in bs)]   # ["2♦","2♥"] -> "2♦ ♥"
    sub = f'<span class="m">{fmt(r.sub)}</span>' if r.sub else ""
    return (f'<div class="row"><div class="bids">{"".join(bid_tile(x) for x in bs)}</div>'
            f'<div class="d">{fmt(r.text)}{sub}</div></div>')


def render_block(bl, card_mode: bool) -> str:
    if isinstance(bl, Note):
        return f'<div class="note">{fmt(bl.text)}</div>'
    tag = f'<span class="tag">{fmt(bl.tag)}</span>' if bl.tag else ""
    callout = ""
    if bl.callout:
        first, *rest = bl.callout.split("\n")
        callout = f'<div class="callout"><span class="big">{fmt(first)}</span>' + \
                  "".join(f"<br>{fmt(x)}" for x in rest) + "</div>"
    # na karcie panele dzielą wysokość proporcjonalnie do liczby wierszy
    style = f' style="flex:{max(len(bl.rows), 1) + (1.6 if bl.callout else 0)} 1 0"' if card_mode else ""
    return (f'<section class="panel"{style}><div class="lbl">{fmt(bl.label)}{tag}</div>'
            f'{callout}{"".join(render_row(r) for r in bl.rows)}</section>')


def render_card(c, theme="") -> str:
    blocks = "".join(render_block(b, True) for b in c.blocks)
    return f"""<div class="card {theme}">
<header><div class="suits s">♠ <span class="r">♥</span> <span class="r">♦</span> ♣</div>
<div class="no">{c.no}</div><div class="t"><h1>{html.escape(c.title)}</h1><p>{fmt(c.sub)}</p></div></header>
<main>{blocks}</main>
<footer><span><span class="club">{CLUB}</span> · {CITY_YEAR}</span><span>{c.no} / {len(CARDS)}</span></footer>
</div>"""


def card_css(font_base: str) -> str:
    return font_css(font_base) + (B / "components.css").read_text() + (B / "card.css").read_text()


def png_name(c) -> str:
    return f"bryd-{c.no}-{c.slug}.png"


# ---------- strona ----------
def build_site():
    assets = DOCS / "assets"
    (assets / "fonts").mkdir(parents=True, exist_ok=True)
    for f in (B / "fonts").glob("*"):
        shutil.copy(f, assets / "fonts" / f.name)
    (assets / "style.css").write_text(font_css("fonts/", SITE_FONTS) + (B / "components.css").read_text()
                                      + (B / "site.css").read_text())
    (assets / "favicon.svg").write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#FDFDFB" stroke="#1F2F6B" stroke-width="4"/>'
        '<text x="32" y="46" text-anchor="middle" font-size="40" fill="#D42B3A" font-family="serif">♥</text></svg>')

    thumbs = "\n".join(
        f'      <a href="karty/{png_name(c)}" target="_blank" rel="noopener">'
        f'<img src="karty/{png_name(c)}" alt="Karta {c.no}: {html.escape(c.title)}" loading="lazy" width="1080" height="1920"></a>'
        for c in CARDS)
    idx = (B / "templates/index.html").read_text()
    idx = idx.replace("{{THUMBS}}", thumbs).replace("{{ROOT}}", "")
    (DOCS / "index.html").write_text(idx)

    nav = "\n".join(f'<a href="#{c.slug}"><b>{c.no}</b>{html.escape(c.title)}</a>' for c in CARDS)
    system = "\n".join(
        f'<article class="sys-card" id="{c.slug}"><div class="sys-head"><div class="no">{c.no}</div>'
        f'<div><h3>{html.escape(c.title)}</h3><p>{fmt(c.sub)}</p></div></div>'
        + "".join(render_block(b, False) for b in c.blocks) + "</article>"
        for c in CARDS)
    titles = {c.slug: c for c in CARDS}
    nav += '\n<a href="#konwencje">Konwencje</a>'
    system += ('\n<article class="sys-card conv" id="konwencje"><div class="sys-head"><div>'
               '<h3>Konwencje</h3><p>Wszystkie umowy, których używamy, w jednym spisie</p></div></div>'
               '<section class="panel"><dl>'
               + "".join(f'<div class="conv-row"><dt>{fmt(n)}</dt><dd>{fmt(d)} '
                         f'<a href="#{slug}">Karta {titles[slug].no}: {html.escape(titles[slug].title)}</a></dd></div>'
                         for n, d, slug in CONVENTIONS)
               + '</dl></section></article>')
    sysp = (B / "templates/system.html").read_text()
    sysp = sysp.replace("{{NAV}}", nav).replace("{{SYSTEM}}", system).replace("{{ROOT}}", "../")
    (DOCS / "system").mkdir(exist_ok=True)
    (DOCS / "system/index.html").write_text(sysp)


# ---------- karty ----------
def print_html(css: str) -> str:
    # A4 pionowo = 210x297 mm, 4 karty (2x2). Karta 9:16 skalowana do ok. 76x135 mm, z linią cięcia.
    scale = 0.53
    slots = "".join(
        f'<div class="slot"><div class="scaled">{render_card(c, "print")}</div></div>'
        for c in CARDS)
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{css}
@page{{size:A4 portrait;margin:0}}
html,body{{background:#fff}}
.sheet{{width:210mm;height:297mm;display:grid;grid-template-columns:repeat(2,max-content);
  justify-content:center;align-content:center;gap:10mm 14mm;overflow:hidden}}
.slot{{width:{540*scale}px;height:{960*scale}px;outline:.25mm dashed #B9B9B9;outline-offset:2.5mm}}
.scaled{{transform:scale({scale});transform-origin:0 0;width:540px;height:960px}}
</style></head><body><div class="sheet">{slots}</div></body></html>"""


async def build_cards():
    TMP.mkdir(exist_ok=True)
    KARTY.mkdir(parents=True, exist_ok=True)
    css = card_css((B / "fonts").as_uri() + "/")
    launch = {"args": ["--allow-file-access-from-files"]}
    if os.environ.get("CHROME_PATH"):
        launch["executable_path"] = os.environ["CHROME_PATH"]
    async with async_playwright() as p:
        br = await p.chromium.launch(**launch)
        pg = await br.new_page(viewport={"width": 540, "height": 960}, device_scale_factor=2)
        for c in CARDS:
            f = TMP / f"{c.slug}.html"
            f.write_text(f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head>'
                         f'<body>{render_card(c)}</body></html>')
            await pg.goto(f.as_uri())
            await pg.evaluate("document.fonts.ready")
            await pg.wait_for_timeout(200)
            over = await pg.evaluate("[...document.querySelectorAll('main,.panel')].some(e=>e.scrollHeight>e.clientHeight+1)")
            await pg.locator(".card").screenshot(path=str(KARTY / png_name(c)))
            print(f"  PNG  {png_name(c)}" + ("   UWAGA: treść się nie mieści!" if over else ""))
        f = TMP / "druk.html"
        f.write_text(print_html(css))
        await pg.goto(f.as_uri())
        await pg.evaluate("document.fonts.ready")
        await pg.wait_for_timeout(300)
        await pg.pdf(path=str(KARTY / "karty-do-druku.pdf"), width="210mm", height="297mm",
                     print_background=True, prefer_css_page_size=True)
        print("  PDF  karty-do-druku.pdf")
        await br.close()
    shutil.rmtree(TMP, ignore_errors=True)


if __name__ == "__main__":
    print("Karty…")
    asyncio.run(build_cards())
    print("Strona…")
    build_site()
    print("Gotowe. Podgląd strony:  python -m http.server -d docs 8000")
