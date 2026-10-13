#!/usr/bin/env python3
"""Build the published pages from the source parts.

    python3 src/build.py doc      writes index.html  (the plan)
    python3 src/build.py review   writes review.html (the archived red-team review)

It expands label chips ([[F]], [[I]] ...), citations ([[@key:L10-20]]), charts, map figures and the
works-cited list, and it refuses to write a page that cites an unknown source, leaves a source
uncited, or contains an em dash. Standard library only."""
import glob, html, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from refs import REFS, GROUPS  # noqa: E402
import figs  # noqa: E402

LABELS = {
    "P": ("Plan says", "p"), "F": ("Fact", "f"), "C": ("Calculation", "c"), "I": ("Inference", "i"),
    "E": ("Estimate", "e"), "O": ("Opinion", "o"), "R": ("Recommendation", "r"), "U": ("Unverified", "u"),
}

num = {}
ref_by_key = {}
for i, (key, group, text, url, kind) in enumerate(REFS, 1):
    if key in num:
        raise SystemExit(f"duplicate ref key {key}")
    num[key] = i
    ref_by_key[key] = (group, text, url, kind)
used = set()
errors = []


def gh_url(url):
    if re.search(r"\.md$", url):
        return url + "?plain=1"
    return url


def pin_html(key, pin):
    group, text, url, kind = ref_by_key[key]
    pin = pin.strip()
    parts = [p.strip() for p in pin.split(",")]
    out = []
    for p in parts:
        m = re.fullmatch(r"L(\d+)(?:-(\d+))?", p)
        if m and kind == "gh":
            anchor = f"#L{m.group(1)}" + (f"-L{m.group(2)}" if m.group(2) else "")
            out.append(f'<a class="pin" href="{html.escape(gh_url(url) + anchor)}" target="_blank" rel="noopener">{p}</a>')
        else:
            out.append(html.escape(p))
    return ", ".join(out)


def cite(m):
    body = m.group(1)
    items = [x.strip() for x in body.split(";") if x.strip()]
    out = []
    for it in items:
        if ":" in it:
            key, pin = it.split(":", 1)
        else:
            key, pin = it, ""
        key = key.strip()
        if key not in num:
            errors.append(f"unknown citation key: {key}")
            continue
        used.add(key)
        s = f'<a href="#ref-{num[key]}">{num[key]}</a>'
        if pin:
            s += " " + pin_html(key, pin)
        out.append(s)
    return '<span class="ct">[' + "; ".join(out) + "]</span>"


def label(m):
    name, cls = LABELS[m.group(1)]
    return f'<span class="lb lb-{cls}">{name}</span>'


def fmt(v):
    s = f"{v:.2f}"
    return s[:-1] if s.endswith("0") else s


def bars(rows, domain, unit="%"):
    out = ['<div class="bars">']
    for name, val, note in rows:
        w = max(0.6, min(100.0, 100.0 * val / domain))
        out.append(
            f'<div class="bar"><div class="bl">{name}</div><div class="bt"><i style="width:{w:.1f}%"></i></div>'
            f'<div class="bv">{fmt(val)}{unit}</div>' + (f'<div class="bn">{note}</div>' if note else "") + "</div>"
        )
    out.append("</div>")
    return "\n".join(out)


CHANNEL_ROWS = [
    ("Test and bot channels", 44.5, "8,668 messages: #test, #volcano, #testing, #meshbud, #foobot, #bot, #foo, #meshai, #ai-bot"),
    ("#wardriving", 24.0, "4,670 messages: MeshMapper pings"),
    ("Public", 22.2, "4,324 messages"),
    ("Topic and social channels", 4.4, "866 messages: #hardware, #hamradio, #chat, #3dprinting and others"),
    ("County, city and town channels", 2.6, "502 messages across 12 channels: the traffic the sub-region tier is built for"),
    ("Weather, alerts and emergency", 2.3, "457 messages: #weather (366, includes bot posts), #socalalert, #socal-incidents, #cert, #wx, #earthquake, #emcommplanning"),
]
AIRTIME_ROWS = [
    ("GRP_TXT, channel messages", 44.5, ""),
    ("ADVERT", 18.0, ""),
    ("REQ", 13.6, ""),
    ("TXT_MSG, direct messages", 9.65, ""),
    ("ANON_REQ", 5.8, ""),
    ("PATH", 3.9, ""),
    ("RESPONSE", 3.0, ""),
    ("ACK", 1.1, ""),
    ("All other types", 0.45, ""),
]
HOPS = {1: 5878, 2: 1259, 3: 1097, 4: 694, 5: 937, 6: 1266, 7: 3917, 8: 6718, 9: 5641, 10: 4233, 11: 2992, 12: 2406, 13: 2177,
        14: 1821, 15: 1541, 16: 1402, 17: 1167, 18: 1054, 19: 923, 20: 788, 21: 1052, 22: 592, 23: 460, 24: 459, 25: 369}


def hops_chart():
    mx = max(HOPS.values())
    out = ['<div class="hops" role="img" aria-label="Observed path lengths, 1 to 25 hops. Peak at 8 hops with 6,718 observations; a second peak at 1 hop with 5,878.">']
    for h in range(1, 26):
        v = HOPS[h]
        cls = "hb"
        if h > 16:
            cls += " over"
        else:
            cls += " in"
        if h == 9:
            cls += " med"
        out.append(f'<div class="{cls}" title="{h} hops: {v:,} observations"><i style="height:{100.0 * v / mx:.1f}%"></i><b>{h}</b></div>')
    out.append("</div>")
    return "\n".join(out)


def packets_block():
    import json
    pk = json.load(open(os.path.join(HERE, "packets.json")))
    words = {3: "three repeater adverts", 13: "13 packets"}.get(len(pk), f"{len(pk)} packets")
    rows = []
    for p in pk:
        rows.append(f"# {p['label']}  code {p['code']}  name {p['name'] or 'no match'}\n{p['hex']}")
    body = html.escape("\n\n".join(rows))
    return (f'<details><summary>Raw bytes of the {words}, as served by the analyzer</summary>'
            '<div class="cb"><div class="cap"><span>Hex, one packet per block</span><button type="button" data-copy>Copy</button></div>'
            f'<pre class="wrap">{body}</pre></div></details>')


def works_cited():
    out = ['<div class="wc">']
    for g, title in GROUPS:
        items = [(k, ref_by_key[k]) for k in num if ref_by_key[k][0] == g]
        if not items:
            continue
        out.append(f'<h3 class="wg">{g}. {title}</h3><ol class="refs">')
        for k, (group, text, url, kind) in items:
            n = num[k]
            link = ""
            if url.startswith("#"):
                link = f' <a href="{url}">See the appendix</a>.'
            elif url:
                shown = url if len(url) <= 96 else url[:93] + "..."
                link = f' <a class="u" href="{html.escape(gh_url(url) if kind == "gh" else url)}" target="_blank" rel="noopener">{html.escape(shown)}</a>'
            out.append(f'<li id="ref-{n}" value="{n}">{text}{link}</li>')
        out.append("</ol>")
    out.append("</div>")
    return "\n".join(out)


TARGETS = {
    "doc": ("index.html", "A community proposal for region scoping on the Southern California MeshCore network: what to do first, "
                          "which names to agree, and what is still unknown."),
    "review": ("review.html", "Red-team review of Draft v3 of the SoCal MeshCore Scoping Plan: every claim checked against its source."),
}
PARTS_DIR = sys.argv[1] if len(sys.argv) > 1 else "doc"
if PARTS_DIR not in TARGETS:
    raise SystemExit("usage: python3 src/build.py [doc|review]")
FULL_NAME, FULL_DESC = TARGETS[PARTS_DIR]
USED_ONLY = True  # number only the sources a page cites
ROOT = os.path.dirname(HERE)


def include_block(m):
    src = open(os.path.join(HERE, "review", "40_fixes.html"), encoding="utf-8").read()
    mm = re.search(r'<h3 id="%s">.*?</h3>(.*?)(?=<h3 id=|</section>)' % re.escape(m.group(1)), src, flags=re.S)
    if not mm:
        errors.append("include not found: " + m.group(1))
        return ""
    return mm.group(1)


def main():
    parts = sorted(glob.glob(os.path.join(HERE, PARTS_DIR, "*.html")))
    if not parts:
        raise SystemExit("no parts")
    raw = {}
    for p in parts:
        raw[p] = re.sub(r"\[\[include:([a-z-]+)\]\]", include_block, open(p, encoding="utf-8").read())
    if USED_ONLY:
        seen = set()
        for p, txt in raw.items():
            for body in re.findall(r"\[\[@([^\]]+)\]\]", txt):
                for it in body.split(";"):
                    seen.add(it.split(":", 1)[0].strip())
        num.clear()
        for key, group, text, url, kind in REFS:
            if key in seen:
                num[key] = len(num) + 1
    chunks = []
    for p in parts:
        s = raw[p]
        base = os.path.basename(p)
        if not (base.startswith("00_") or base.startswith("99_")):
            s = re.sub(r"\[\[([PFCIEORU])\]\]", label, s)
            s = re.sub(r"\[\[@([^\]]+)\]\]", cite, s)
        chunks.append(s)
    doc = "\n".join(chunks)

    # verdict counts from the ledger
    counts = {}
    for v in re.findall(r'<article class="lg" data-v="([a-z]+)"', doc):
        counts[v] = counts.get(v, 0) + 1
    total = sum(counts.values())

    def count_sub(m):
        k = m.group(1)
        if k == "total":
            return str(total)
        if k == "refs":
            return str(len(num))
        if k == "findings":
            return str(len(re.findall(r'<section class="fd"', doc)))
        return str(counts.get(k, 0))

    doc = re.sub(r"\[\[#([a-z]+)\]\]", count_sub, doc)
    doc = doc.replace("[[chart:channels]]", bars(CHANNEL_ROWS, 50))
    doc = doc.replace("[[chart:airtime]]", bars(AIRTIME_ROWS, 50))
    doc = doc.replace("[[chart:hops]]", hops_chart())
    doc = doc.replace("[[works-cited]]", works_cited())
    doc = doc.replace("[[packets]]", packets_block())
    if "[[fig:" in doc:
        obs_svg, n_obs, n_lax = figs.fig_observers()
        doc = doc.replace("[[fig:names]]", figs.fig_names()).replace("[[fig:observers]]", obs_svg).replace("[[fig:conejo]]", figs.fig_conejo())
        doc = doc.replace("[[obs:located]]", str(n_obs)).replace("[[obs:lax]]", str(n_lax))

    unused = [k for k in num if k not in used]
    for k in unused:
        errors.append(f"reference never cited: {k}")
    for bad, nm in (("—", "em dash"), ("–", "en dash"), ("&mdash;", "em dash entity"), ("&ndash;", "en dash entity")):
        for m in re.finditer(re.escape(bad), doc):
            ctx = doc[max(0, m.start() - 50): m.start() + 30].replace("\n", " ")
            errors.append(f"{nm} at ...{ctx}...")
    for m in re.finditer(r"\[\[[^\]]{0,40}", doc):
        errors.append(f"unexpanded macro: {m.group(0)}")
    for w in ("genuinely", "honestly", "straightforward"):
        if re.search(w, doc, flags=re.I):
            errors.append(f"banned word: {w}")

    title = re.search(r"<title>(.*?)</title>", doc).group(1)
    head, body = doc.split("</style>", 1)
    page = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            f'<meta name="description" content="{html.escape(FULL_DESC)}">\n'
            f'<meta property="og:title" content="{html.escape(title)}">\n'
            f'<meta property="og:description" content="{html.escape(FULL_DESC)}">\n'
            '<meta property="og:type" content="article">\n'
            '<style>:root{color-scheme:light}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n'
            + head + "</style>\n</head>\n<body>\n" + body + "\n</body>\n</html>\n")
    path = os.path.join(ROOT, FULL_NAME)
    if not errors:
        open(path, "w", encoding="utf-8").write(page)
        frag = os.environ.get("FRAGMENT_OUT")  # optional: the same page without the document wrapper
        if frag:
            open(frag, "w", encoding="utf-8").write(doc)
    words = len(re.sub(r"<[^>]+>", " ", re.sub(r"<(style|script).*?</\1>", " ", doc, flags=re.S)).split())
    print(f"{'NOT written' if errors else 'wrote'} {path}: {len(page):,} bytes, about {words:,} words, {len(num)} sources cited")
    if errors:
        print(f"{len(errors)} PROBLEMS:")
        for e in errors:
            print("  -", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
