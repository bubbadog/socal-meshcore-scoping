# Contributing

Corrections from people who know the network are the reason this is public. You do not need permission, an invitation or any connection to the author.

## The quickest way: open an issue

Use the [feedback form](https://github.com/bubbadog/socal-meshcore-scoping/issues/new/choose), or the form at the bottom of the document, which fills in an issue for you. Say which section, what is wrong or missing, and how you know. A link, a quote with its date, or a command output is worth more than an opinion.

## Proposing a change yourself: a pull request

1. Fork this repository on GitHub (the Fork button, top right). Anyone with a GitHub account can.
2. Edit the text in `src/doc/10_doc.html`. Do not edit `index.html` by hand; it is generated.
3. Rebuild: `python3 src/build.py doc` (Python 3, nothing to install).
4. Open the pull request against `main`. Small pull requests that change one thing get merged fastest.

If you only want to fix a typo, GitHub's pencil icon on the file does all of the above in the browser.

## House rules for the text

- **Label every statement.** `[[F]]` fact, `[[C]]` calculation, `[[I]]` inference, `[[E]]` estimate, `[[O]]` opinion, `[[R]]` recommendation, `[[U]]` unverified.
- **Give every fact a source.** Add the source to `src/refs.py`, then cite it as `[[@key]]` or with lines as `[[@key:L10-20]]`. GitHub sources must be pinned to a full commit hash, never `main` or `HEAD`, so the line numbers keep pointing at the same text.
- **Quote exactly.** `tools/check_quotes.py` compares quotations with the cited file.
- **Keep people out of it.** No names or handles of individual users. Paraphrase what private people said in Discord unless they agree to be quoted. Repeater names are fine where the evidence needs them.
- **Plain words.** Short sentences. No em dashes (the build rejects them).

## Bringing evidence from Discord

Neither AI system that worked on this could read the WCMesh Discord, so this is the most valuable thing a member can add. Please give the channel, the date, the exact text and the message link. An AI summary of a discussion is treated as a lead until the original words are supplied.

## Checking the work

```
python3 tools/check_links.py      # clones the cited repositories into .sources/ and verifies every link
python3 tools/check_quotes.py     # verifies quotations and line references
python3 tools/decode_scope.py --file src/packets.json
```

## Conduct

Be kind and be specific. Disagree with the claim, not the person. The maintainers of WCMesh, the config generator and MeshMapper owe this proposal nothing; if they comment, that is a favor.

By contributing you agree that your contribution is licensed under the terms in [LICENSE.md](LICENSE.md).
