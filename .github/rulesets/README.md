# Repository rulesets

These files describe the branch and tag rules this repository is meant to run with. GitHub does not read them from here. A repository admin imports each one once:

Settings, Rules, Rulesets, New ruleset, Import a ruleset, then choose the file and press Create.

| File | What it does | Who can bypass |
| --- | --- | --- |
| `main-history.json` | Nobody can force-push to `main` or delete it, so published history cannot be rewritten | Nobody |
| `main-pull-requests.json` | Changes to `main` arrive by pull request, the `build` check must pass, and review comments must be resolved | Repository admins |
| `release-tags.json` | A tag such as `v6` cannot be moved or deleted once pushed, so a cited draft stays what it was | Nobody |

The `build` check comes from `.github/workflows/check.yml`. It rebuilds both pages and fails if they differ from the committed ones.
