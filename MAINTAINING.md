# Maintaining this repository

A record of how the repository is set up, so the setup can be checked or repeated.

## One-time settings (repository admin, in the browser)

| Where | Setting | Value | Why |
| --- | --- | --- | --- |
| Settings, General, Features | Wikis, Projects | Off | One place for content (this repo) and one for feedback (Issues) |
| Settings, General, Features | Issues | On | The feedback form opens issues |
| Settings, General, Pull Requests | Allow squash merging | On | One commit per change keeps history readable |
| Settings, General, Pull Requests | Allow merge commits, Allow rebase merging | Off | Same reason |
| Settings, General, Pull Requests | Automatically delete head branches | On | No stale branches after a merge |
| Settings, Actions, General | Actions permissions | Allow bubbadog, and select non-bubbadog, actions: actions created by GitHub and by Marketplace verified creators | Only trusted publishers' actions can run |
| Settings, Actions, General | Require actions to be pinned to a full-length commit SHA | On | A moved or hijacked tag cannot swap in different code; Dependabot keeps the pins current |
| Settings, Actions, General | Approval for running fork pull request workflows from contributors | Require approval for first-time contributors | A stranger's pull request cannot run code until you look at it |
| Settings, Actions, General | Workflow permissions | Read repository contents and packages permissions | Workflows cannot write to the repository by default |
| Settings, Actions, General | Allow GitHub Actions to create and approve pull requests | Off | A workflow cannot approve its own change |
| Settings, Advanced Security | Private vulnerability reporting, Dependabot alerts, Secret Protection and push protection | On | Free for public repositories; catches leaked credentials |
| Settings, Pages | Enforce HTTPS | On | Readers always get the encrypted site |
| Repository home page, About (gear icon) | Website | The Pages address | Visitors on GitHub find the readable version |

## Rulesets

Definitions live in [.github/rulesets](.github/rulesets) and must always match what GitHub enforces. Change both together: edit the ruleset in Settings, export it, and commit the exported file in the same pull request. The `rulesets` workflow fails if they drift. To apply a file to a fresh repository: Settings, Rules, Rulesets, New ruleset, Import a ruleset, choose the file, review, Create.

`main-pull-requests.json` routes contributors' changes through a squash-merged pull request that must pass `build`. Repository admins are on its bypass list, so the maintainer can push small changes straight to `main`; GitHub shows a bypass notice on the push. Nobody can force-push, delete `main`, or move a `v` tag.

## Everyday work

- Edit text in `src/doc/`, run `python3 src/build.py doc`, commit both the source and the rebuilt `index.html`.
- Open a pull request. The `build` and `sources` checks run by themselves.
- Record what changed in `CHANGELOG.md`.

## Publishing a new draft

1. Update the draft number and date in `src/doc/10_doc.html`, rebuild, merge.
2. Tag the merge commit with the public number, for example `git tag v1.0 && git push origin v1.0` for public draft 1 (internal numbering stays in CHANGELOG.md). Tags that start with `v` cannot be moved or deleted once the tag ruleset is active, so a cited draft stays what it was.

## Dependencies

`.github/dependabot.yml` checks the pinned actions weekly and opens one grouped pull request when there are updates. Merge it once `build` passes; that is how the SHA pins stay current.

## What the checks do

- `build`: rebuilds both pages and fails if the committed pages differ from what the source produces. It also confirms the scope decoder still reproduces the published packets.
- `sources`: confirms every pinned GitHub link exists at its commit and every quotation matches its cited file.
- `rulesets`: weekly and on ruleset changes, confirms the files in `.github/rulesets` match the live rulesets. GitHub pauses scheduled workflows after 60 days without repository activity; re-enable it from the Actions tab if that happens.

## Review roadmap

Security settings were set on 13 October 2026. Review them by **13 January 2027**, or sooner when a second maintainer joins or outside pull requests start arriving. Questions to answer at that review:

1. Has anyone other than the maintainer sent a pull request? If yes, raise required approvals to 1 for non-admins, or keep 0.
2. Is the admin bypass still needed, or have direct pushes stopped? Removing it makes every change go through a pull request.
3. Did the Actions allow-list or SHA pinning block a workflow you wanted? If yes, add that publisher deliberately rather than loosening the policy.
4. Did Dependabot's action updates merge cleanly? If they piled up, change the schedule to monthly.
5. Has the `rulesets` drift check failed? Every failure should end with the file and the live ruleset matching again.
6. Have first-time contributor workflows been abused? If yes, switch approval to all outside contributors.
7. Is two-factor authentication on the owner account a passkey or security key? It protects the repository more than any setting here.
