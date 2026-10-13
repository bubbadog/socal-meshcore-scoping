# Changelog

## Draft v6, 13 October 2026

First public, consolidated edition. It merges the operator's Draft v5 (written with Muse) with the red-team review of Draft v3 (written by Claude), and answers every finding of that review.

Changed from Draft v5:

- Load is now the stated reason for the plan. The claim that "99.5% of observed transport routes were unscoped" is dropped, because the analyzer's unscoped total counts every ordinary flood and direct packet.
- No region names are ratified. The four existing sets of names are shown side by side with three ways to converge.
- Rollout reordered: settings that need no agreement first, then names, then tags only, then default scope, then machines before people.
- Default scope is separated from tagging. A repeater that sets a default scope before its neighbors hold the name stops being heard beyond one hop.
- Commands split by firmware generation (1.12 to 1.14, 1.15, 1.16 and newer). The strict and gentle containment options no longer share one block.
- The single-repeater pilot is replaced by two pilots with controls.
- The 24 candidate sub-regions and the schematic terrain map are withdrawn. The terrain table is corrected and kept as background.
- The WCMesh repeater settings are quoted as published.
- Every GitHub source is pinned to a commit.
- Added: maps of the four name sets, forwarding and first-mover diagrams, a neighbor map for the pilot, search, a feedback form, an author's note, an account of how the document was made, and a list of 14 open research items.

Corrections made the same day, after an independent read against the pinned sources:

- Command block 0: on firmware older than 1.16, `get flood.max.unscoped` and `get flood.max.advert` answer with the plain `flood.max` value. The earlier caption said an error would reveal the firmware generation. Go by `ver`.
- Names, option C: `san` is the beginning of generator area names such as `santaclarita`, so the option breaks the prefix rule until the San Diego metro has another name.
- The three `psp` adverts were each relayed once. The relaying repeater either holds `psp` or runs firmware too old to filter.
- An overlap repeater does retransmit each metro's floods one hop into the other metro.
- The generator has declared no tags since 24 August, where the text said 3 August.
- "About 22 hours" is the life of the SoCal region list. The regions section that held it lasted about 55 hours.
- `socal` is one of two names the lists share (`us` is the other, between the generator and the wiki draft).
- The Q2 report describes tunneling (injected traffic), which the text had called a replay attack. The conclusion is relabeled as inference.
- Emergency and alert channels: the rollout and the channel table now agree (unscoped until the gate for people is passed, then `socal`).
- The `us` scope rests on a single packet and is now marked probable. The different counts of scoped packets (64 of 65, 12 of 58, 13 decoded) are explained.
- Small fixes: county channels are about 1.1 percent of relay airtime; the duplicate counter's source is cited; one line range and one caption corrected.

Added: a terrain map of the mountain barriers and passes, drawn on real county outlines at approximate positions.

Not yet reflected: anything said in the WCMesh Discord.

## Earlier drafts

Drafts v1 to v5 were working drafts and are not published here. The review of Draft v3 is archived as `review.html`, with the names of individual users withheld.
