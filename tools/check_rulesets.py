"""Compare .github/rulesets/*.json with the rulesets GitHub is enforcing.

Usage:
  python3 tools/check_rulesets.py                 # reads the live rulesets from the API
  python3 tools/check_rulesets.py --live FILE     # compares against a saved JSON list instead

Exits 1 and prints every difference if the files and the live rulesets disagree.
Bypass lists are compared only when the API returns them (it does so for admins);
the public API omits them, so this check cannot see a bypass change.
"""
import json
import os
import sys
import urllib.request
from pathlib import Path

FIELDS = ("name", "target", "enforcement", "conditions", "rules")
ROOT = Path(__file__).resolve().parent.parent
RULESET_DIR = ROOT / ".github" / "rulesets"


def api(url):
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json",
                                               "X-GitHub-Api-Version": "2022-11-28"})
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def live_rulesets(repo):
    listing = api(f"https://api.github.com/repos/{repo}/rulesets?per_page=100")
    return [api(r["_links"]["self"]["href"]) for r in listing]


def normalize(ruleset):
    out = {k: ruleset.get(k) for k in FIELDS}
    out["rules"] = sorted(out["rules"] or [], key=lambda r: r["type"])
    for rule in out["rules"]:
        checks = (rule.get("parameters") or {}).get("required_status_checks")
        if checks:
            checks.sort(key=lambda c: c["context"])
    if "bypass_actors" in ruleset:
        out["bypass_actors"] = sorted(ruleset["bypass_actors"] or [],
                                      key=lambda a: (a["actor_type"], str(a.get("actor_id"))))
    return out


def main(argv):
    if "--live" in argv:
        live = json.loads(Path(argv[argv.index("--live") + 1]).read_text())
    else:
        live = live_rulesets(os.environ.get("REPO", "bubbadog/socal-meshcore-scoping"))
    live_by_name = {r["name"]: r for r in live}

    problems = []
    seen = set()
    for path in sorted(RULESET_DIR.glob("*.json")):
        want = json.loads(path.read_text())
        name = want["name"]
        seen.add(name)
        if name not in live_by_name:
            problems.append(f"{path.name}: no live ruleset named '{name}'")
            continue
        got = normalize(live_by_name[name])
        exp = normalize(want)
        if "bypass_actors" not in got:
            exp.pop("bypass_actors", None)
        for key in exp:
            if exp[key] != got.get(key):
                problems.append(f"{path.name}: '{key}' differs\n  file: {json.dumps(exp[key])}\n  live: {json.dumps(got.get(key))}")
    for name in live_by_name:
        if name not in seen:
            problems.append(f"live ruleset '{name}' has no file in .github/rulesets")

    if problems:
        print("Ruleset files and live rulesets disagree. Update the file to match the live ruleset (or the reverse), in the same pull request as any change.")
        print("\n".join(problems))
        return 1
    print(f"OK: {len(seen)} ruleset files match the live rulesets.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
