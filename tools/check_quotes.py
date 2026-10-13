#!/usr/bin/env python3
"""Check quotations and line references in the source text against the cited files.

  python3 tools/check_quotes.py [--sources DIR] [doc|review]

For every citation such as [[@wc-q2:L39]] it takes the quoted passages in the sentence or cell
that the citation closes and looks for them in the cited source, ignoring case, spacing and
punctuation. It also confirms each line reference is inside its file.

Only sources that are files pinned on GitHub can be checked this way. Quotations whose only cited
sources are web pages, live analyzer data or unpublished drafts are listed for checking by hand.
Run tools/check_links.py first so the cited repositories are present in DIR. MIT license.
"""
import glob
import html
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "src"))
from refs import REFS  # noqa: E402

# citations whose quoted wording sits in a neighbouring file of the same commit
EXTRA = {"fw-tks": ["src/helpers/TransportKeyStore.h"], "fw-chat": ["src/helpers/BaseChatMesh.h"],
         "fw-packet": ["src/Packet.h"], "cs-readme": ["cmd/ingestor/observer_fields.go"]}
REF = {k: (u, kind) for k, g, t, u, kind in REFS}


def norm(s):
    return re.sub(r"[^a-z0-9]", "", html.unescape(s).lower())


def repo_dir(sources, owner, repo):
    for cand in (os.path.join(sources, f"{owner}_{repo}", "repo"), os.path.join(sources, f"{owner}_{repo}")):
        if os.path.isdir(os.path.join(cand, ".git")):
            return cand
    return None


def show(d, sha, path):
    r = subprocess.run(["git", "-C", d, "show", f"{sha}:{path}"], capture_output=True)
    return r.stdout.decode("utf-8", "replace") if r.returncode == 0 else None


def source_text(key, sources):
    url, _ = REF[key]
    m = re.match(r"https://github\.com/([^/]+)/([^/]+)/blob/([0-9a-f]{40})/([^?#]+)", url)
    if not m:
        return None, None
    d = repo_dir(sources, m.group(1), m.group(2))
    if not d:
        return None, None
    main = show(d, m.group(3), m.group(4))
    full = main or ""
    for extra in EXTRA.get(key, []):
        full += "\n" + (show(d, m.group(3), extra) or "")
    return (full if main is not None else None), main


def main(argv):
    args = argv[1:]
    sources = os.path.join(ROOT, ".sources")
    if args[:1] == ["--sources"]:
        sources, args = os.path.abspath(args[1]), args[2:]
    if args[:1] in (["-h"], ["--help"]):
        print(__doc__)
        return 0
    target = args[0] if args else "doc"
    cache, wrong, by_hand = {}, [], []
    matched = pins = 0
    for p in sorted(glob.glob(os.path.join(ROOT, "src", target, "*.html"))):
        base = os.path.basename(p)
        if base[:2] in ("00", "99"):
            continue
        s = open(p, encoding="utf-8").read()
        pos = 0
        for m in re.finditer(r"\[\[@([^\]]+)\]\]", s):
            seg = s[pos:m.start()]
            pos = m.end()
            cut = max(seg.rfind(t) for t in ("<li", "<p", "<td", "<tr", "<figcaption", "<article"))
            if cut >= 0:
                seg = seg[cut:]
            text = re.sub(r"\[\[[A-Z]\]\]", " ", html.unescape(re.sub(r"<[^>]+>", "", seg)))
            keys = [tuple(x.strip() for x in (it.strip().partition(":")[0], it.strip().partition(":")[2])) for it in m.group(1).split(";")]
            texts = []
            for k, pin in keys:
                if k not in cache:
                    cache[k] = source_text(k, sources)
                full, main = cache[k]
                if full is not None:
                    texts.append(norm(full))
                if main is not None and pin:
                    n = main.count("\n") + 1
                    for a, b in re.findall(r"L(\d+)(?:-(\d+))?", pin):
                        pins += 1
                        if int(b or a) > n or int(a) > int(b or a):
                            wrong.append(f"{base}: line reference {k}:{pin} is outside the file ({n} lines)")
            for q in re.findall(r'"([^"]{10,})"', text):
                for frag in (f for f in re.split(r"\.\.\.", q) if len(norm(f)) >= 8):
                    if not texts:
                        by_hand.append(f"{', '.join(k for k, _ in keys)}: {frag}")
                    elif any(norm(frag) in t for t in texts):
                        matched += 1
                    else:
                        by_hand.append(f"{', '.join(k for k, _ in keys)} (not in the pinned file, so check the other cited source): {frag}")
    print(f"{target}: {matched} quotations matched to a pinned source file, {pins} line references inside their files, "
          f"{len(by_hand)} quotations to check by hand, {len(wrong)} problems")
    for w in wrong:
        print("  PROBLEM", w)
    for b in by_hand:
        print("  BY HAND", b)
    return 1 if wrong else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
