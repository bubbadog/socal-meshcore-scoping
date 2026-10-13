#!/usr/bin/env python3
"""Check every link in the built pages.

  python3 tools/check_links.py [--sources DIR] [page.html ...]

For each page (default: index.html and review.html) it confirms that
  * every internal #anchor resolves,
  * every GitHub file link is pinned to a full commit hash,
  * the file exists at that commit, and any #L line anchor is inside the file,
  * every commit link names a commit that exists.
Other web links are listed so they can be opened by hand.

Cited repositories are cloned without file contents into DIR (default .sources/, ignored by git)
and the pinned commits are fetched on demand. Needs git and network access. MIT license.
"""
import html
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def git(d, *args):
    return subprocess.run(["git", "-C", d, *args], capture_output=True)


def clone_dir(sources, owner, repo):
    for cand in (os.path.join(sources, f"{owner}_{repo}", "repo"), os.path.join(sources, f"{owner}_{repo}")):
        if os.path.isdir(os.path.join(cand, ".git")):
            return cand
    d = os.path.join(sources, f"{owner}_{repo}")
    os.makedirs(sources, exist_ok=True)
    r = subprocess.run(["git", "clone", "--quiet", "--filter=blob:none", "--no-checkout", "--depth", "1",
                        f"https://github.com/{owner}/{repo}", d], capture_output=True)
    return d if r.returncode == 0 else None


def have_commit(d, sha):
    if git(d, "cat-file", "-t", sha).stdout.strip() == b"commit":
        return True
    git(d, "fetch", "--quiet", "--depth", "1", "--filter=blob:none", "origin", sha)
    return git(d, "cat-file", "-t", sha).stdout.strip() == b"commit"


def check(page_path, sources):
    page = open(page_path, encoding="utf-8").read()
    ids = set(re.findall(r'\bid="([^"]+)"', page))
    bad, ext = [], set()
    n_int = n_file = n_commit = 0
    for h in (html.unescape(x) for x in re.findall(r'href="([^"]+)"', page)):
        if h.startswith("#"):
            n_int += 1
            if h[1:] not in ids:
                bad.append("missing anchor " + h)
            continue
        m = re.match(r"https://github\.com/([^/]+)/([^/]+)/blob/([^/]+)/([^?#]+)(?:\?plain=1)?(?:#L(\d+)(?:-L(\d+))?)?$", h)
        if m:
            owner, repo, sha, path, l1, l2 = m.groups()
            if not re.fullmatch(r"[0-9a-f]{40}", sha):
                bad.append("not pinned to a commit: " + h)
                continue
            d = clone_dir(sources, owner, repo)
            if not d or not have_commit(d, sha):
                bad.append("could not fetch the pinned commit: " + h)
                continue
            r = git(d, "show", f"{sha}:{path}")
            if r.returncode != 0:
                bad.append("file missing at commit: " + h)
                continue
            n_file += 1
            lines = r.stdout.count(b"\n") + 1
            if l1 and int(l2 or l1) > lines:
                bad.append(f"line anchor past the end ({lines} lines): {h}")
            continue
        m = re.match(r"https://github\.com/([^/]+)/([^/]+)/commits?/([0-9a-f]{40})", h)
        if m:
            owner, repo, sha = m.groups()
            d = clone_dir(sources, owner, repo)
            n_commit += 1
            if not d or not have_commit(d, sha):
                bad.append("commit not found: " + h)
            continue
        ext.add(h)
    print(f"{os.path.basename(page_path)}: {n_int} internal anchors, {n_file} pinned GitHub file links, "
          f"{n_commit} commit links, {len(ext)} other links, {len(bad)} problems")
    for b in bad:
        print("  PROBLEM", b)
    return bad, ext


def main(argv):
    args = argv[1:]
    sources = os.path.join(ROOT, ".sources")
    if args[:1] == ["--sources"]:
        sources, args = os.path.abspath(args[1]), args[2:]
    if args[:1] in (["-h"], ["--help"]):
        print(__doc__)
        return 0
    pages = args or [os.path.join(ROOT, "index.html"), os.path.join(ROOT, "review.html")]
    total, others = 0, set()
    for p in pages:
        bad, ext = check(p, sources)
        total += len(bad)
        others |= ext
    print("Other links, to open by hand:")
    for e in sorted(others):
        print("  " + e)
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
