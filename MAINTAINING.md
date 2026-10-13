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
| Settings, Actions, General | Approval for running fork pull request workflows from contributors | Require approval for first-time contributors | A stranger's pull request cannot run code until you look at it |
| Settings, Actions, General | Workflow permissions | Read repository contents and packages permissions | Workflows cannot write to the repository by default |
| Settings, Actions, General | Allow GitHub Actions to create and approve pull requests | Off | A workflow cannot approve its own change |
| Settings, Advanced Security | Private vulnerability reporting, Dependabot alerts, Secret Protection and push protection | On | Free for public repositories; catches leaked credentials |
| Settings, Pages | Enforce HTTPS | On | Readers always get the encrypted site |
| Repository home page, About (gear icon) | Website | The Pages address | Visitors on GitHub find the readable version |

## Rulesets

Definitions live in [.github/rulesets](.github/rulesets). GitHub does not read them from the repository; each is imported once. The import screen asks for a file on your computer, so download the file first (open it on GitHub and use "Download raw file"), then: Settings, Rules, Rulesets, New ruleset, Import a ruleset, choose the file, review, Create.

After `main-pull-requests.json` is active, every change to `main` arrives by pull request and must pass the `build` check. Admins can bypass in an emergency.

## Everyday work

- Edit text in `src/doc/`, run `python3 src/build.py doc`, commit both the source and the rebuilt `index.html`.
- Open a pull request. The `build` and `sources` checks run by themselves.
- Record what changed in `CHANGELOG.md`.

## Publishing a new draft

1. Update the draft number and date in `src/doc/10_doc.html`, rebuild, merge.
2. Tag the merge commit, for example `git tag v7 && git push origin v7`. Tags that start with `v` cannot be moved or deleted once the tag ruleset is active, so a cited draft stays what it was.

## What the checks do

- `build`: rebuilds both pages and fails if the committed pages differ from what the source produces. It also confirms the scope decoder still reproduces the published packets.
- `sources`: confirms every pinned GitHub link exists at its commit and every quotation matches its cited file.
