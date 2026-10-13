# SoCal MeshCore Scoping Plan

A community proposal for region scoping on the Southern California MeshCore network: what to do first, which region names to agree on, and what is still unknown.

**Status: Draft v6, 13 October 2026. Not adopted.** This is one repeater operator's proposal for the West Coast Mesh community to correct. It speaks for nobody else.

- **Read it:** https://bubbadog.github.io/socal-meshcore-scoping/
- **Red-team review of the earlier draft:** https://bubbadog.github.io/socal-meshcore-scoping/review.html
- **Tell us what is wrong:** [open an issue](https://github.com/bubbadog/socal-meshcore-scoping/issues/new/choose), or send a pull request. You do not need to know the author. See [CONTRIBUTING.md](CONTRIBUTING.md).

## A note from the author

I am new to this technology. I have my repeater, SkyNet, set up in Thousand Oaks, and I am still learning how the network works. I put this together because I would like the mesh to be useful, robust and efficient for everyone, and I think a little planning can help with that. I am not trying to step on anyone's toes. The people who built and run this network know far more about it than I do. If something here is wrong or already decided, please tell me.

The SkyNet operator (GitHub: bubbadog)

## What it proposes

1. Start with settings that need no agreement: the published WCMesh repeater settings, advert limits, a hop-limit trial and quieter bots.
2. Agree one set of region names before anyone tags a repeater. Four sets exist today.
3. Tag repeaters first, and leave their default scope alone until the neighbors are tagged too.
4. Scope machines (wardriving pings, bots) before asking people to change anything.
5. Measure airtime and delivery at every step, and stop when a step does not help.

## What is still unknown

Nobody who worked on this document has read the WCMesh Discord. That is the largest gap. The document lists 14 open research items (section 14) with who can close each one. If you can close one, an issue with the original words, a link or a command output is the most useful contribution there is.

## How this was made

One person worked with two AI systems. Readers should weigh the document with that in mind.

| Step | Who | What |
| --- | --- | --- |
| 1 | The operator, with Muse (believed to be the Spark 1.3 model) | Drafts v1 to v5 of the plan and the public web research |
| 2 | Claude from Anthropic (Fable 5.1) | Firmware read at its release tag, a claim-by-claim red-team review of Draft v3, analysis, the region names decoded from packets on air, and this consolidated edition |
| 3 | The community | Corrections, through issues and pull requests |

AI systems make confident mistakes. Every statement in the document carries a label (Fact, Calculation, Inference, Estimate, Opinion, Recommendation, Unverified) and facts carry a numbered source so they can be checked.

## What was checked for Draft v6

| Check | Result |
| --- | --- |
| Pinned GitHub file links that exist at their commit | 142 of 142, plus 3 commit links (`tools/check_links.py`, run against fresh clones from GitHub) |
| Internal links that resolve | 268 of 268 |
| Line references inside their files | 113 of 113 (`tools/check_quotes.py`) |
| Quotation fragments | 33: 16 matched by script to pinned source files, 14 matched by script to the unpublished Draft v5 file, 3 checked by hand (two against the MeshCore blog, one against a firmware format string) |
| Scope decoding | Reproduced by a second, independent implementation (`tools/decode_scope.py`) |
| New calculations in this edition | Recomputed by script |
| Independent read | A separate AI agent that had not seen the document being written checked the firmware claims, every command block and a sample of citations against the pinned sources. It found eleven errors; all are corrected (see [CHANGELOG.md](CHANGELOG.md)) |

What was **not** checked: the independent read did not reach the claims sourced to the MeshCore blog, the live analyzer and MeshMapper figures, the SkyNet counters or the terrain table. Some web pages were read through a tool that summarizes them. Analyzer figures are a snapshot from 13 October 2026 and the analyzer keeps about seven days of data, so they will not reproduce later. Links to web pages and to the analyzer were read on 13 October 2026 and are not rechecked by the scripts. The positions of mountain ranges on the terrain map are approximate.

## Repository layout

```
index.html            the plan, built (served by GitHub Pages)
review.html           the archived red-team review of Draft v3, built
src/doc/              the plan's source text, in HTML with a few macros
src/review/           the review's source text
src/refs.py           every source, with its pinned URL
src/figs.py           the map figures; src/geo.json holds the county outlines
src/build.py          builds index.html and review.html
tools/check_links.py  verifies every link in the built pages
tools/check_quotes.py verifies quotations and line references
tools/decode_scope.py finds the region name a scoped packet was sent under
```

Build with Python 3, standard library only:

```
python3 src/build.py doc
python3 src/build.py review
```

The build refuses to write a page that cites an unknown source or leaves a listed source uncited.

## Privacy

Names of individual mesh users are left out. Only packets sent by a repeater are reproduced. Please keep it that way in issues and pull requests: paraphrase what private people said in Discord unless they agree to be quoted.

## License

Text and figures: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Code in `src/` and `tools/`: MIT. See [LICENSE.md](LICENSE.md), which also credits the map data.
