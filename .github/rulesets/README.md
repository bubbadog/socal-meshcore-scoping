# Repository rulesets

These files are the source of truth for the branch and tag rules this repository runs with. GitHub does not read them from here, so the rule is: **a file here and its live ruleset change together, in the same pull request.** If you change a ruleset in Settings, export it (the ruleset's menu, Export ruleset) and replace the file. The `rulesets` workflow compares the two every week and on every pull request that touches this folder, and fails if they disagree.

To apply a file to a repository: Settings, Rules, Rulesets, New ruleset, Import a ruleset, choose the file, review, Create.

| File | What it does | Who can bypass |
| --- | --- | --- |
| `main-history.json` | Nobody can force-push to `main` or delete it, so published history cannot be rewritten | Nobody |
| `main-pull-requests.json` | Changes to `main` arrive by squash-merged pull request, the `build` check (from GitHub Actions only) must pass, and review comments must be resolved | Repository admins, so the maintainer can push directly |
| `release-tags.json` | A tag such as `v1.0` cannot be moved or deleted once pushed, so a cited draft stays what it was | Nobody |

The `build` check comes from `.github/workflows/check.yml`. It rebuilds both pages and fails if they differ from the committed ones. The check is tied to the GitHub Actions app (`integration_id` 15368), so another app cannot report a fake `build` result.

The public API does not show bypass lists, so the weekly comparison cannot see a bypass change. Check the bypass column above by eye when you review the rulesets.
