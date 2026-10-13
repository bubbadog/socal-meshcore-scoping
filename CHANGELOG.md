# Changelog

## Public draft 1 (internal draft 6), 13 October 2026

First public, consolidated edition. It merges the operator's working draft 5 (written with Muse) with the red-team review of working draft 3 (written by Claude), and answers every finding of that review.

Changed from working draft 5:

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

Revised the same evening, after a read-only search of the WCMesh Discord (1,501 messages matched, 52 cited by message link; Discord sources are group M of the works cited):

- Names: the airport-code metros of working drafts 3 to 5 are withdrawn. The plan follows the direction the SoCal administrator and the config generator's maintainer have already set: `us`, `west`, `california`, `socal`, then county names, with local areas as optional tags. The administrator argued against three-letter codes, and his August survey (about 30 responses) found city level too granular. No names are proposed; two points from the withdrawn options are put as questions.
- Names: a prefix check of the generator's SoCal list found `west` before `westside` and `westernriverside`, and `imperial` before `imperialvalley` and `imperialborder`. Harmless on a repeater that holds the full chain; raised as a question for the generator's maintainer, not a change.
- Names: a fifth vocabulary is forming on the air (`psp` from the Coachella Valley administrator, an `le` scope, `rsc` proposed on 12 October), which is the plan's argument for publishing the county list soon.
- Commands: every block uses the generator's own lines. The 1.16 form is `region def us west california socal ventura`; on 1.15 and 1.12 to 1.14 the same tree is built with `region put name parent`. The first pass of this revision wrote `region def us|* west|* ...`, which would have placed every name under the root as a flat set; corrected against the firmware source and recorded in the red-team table. Roles: wide-only `region def us west california socal`; overlap `... socal ventura|socal santabarbara`; local tag `region put conejovalley ventura`.
- Rollout: step 1 names the bot asks already on record (the administrator's June request, meshcore-bot's rate limits, Sacramento's draft bot policy). Step 4 sets `region default socal` first, per the administrator's July guidance (default set, home unset, default at a higher level); county defaults only with his agreement. Step 6 notes that strict forwarding is already in use at the Bear Mountain bridge.
- Answer to the Q2 report: "frequency is the boundary" is now "most of the boundary". A SoCal to Central Valley bridge has run on Bear Mountain near Tehachapi since at least March and has blocked unscoped traffic since 10 August. The plan proposes no new bridges.
- Why now: members' own load figures added (a March week's Public and bot counts, an under-10-percent duty-cycle report, Seattle's thresholds, a February advert-airtime measurement).
- How scoping works: the first-mover and firmware claims are set beside community statements ("region default is a loaded gun"; "anything before 1.12 drops scoped packets"; pre-1.10 repeaters forward scoped packets unchecked).
- Research still needed: a Status column. R1, R3 and R6 closed (R3 by inference: the SoCal administrator also administers the MeshMapper SoCal zones); R4, R5 and R11 partly closed; R15 (Cascadia and Bay Area boundaries) and R16 (whether the operators already using `psp`, `le` and `rsc` move to the county names) added.
- How this was made: a fifth step for the Discord read, with its limits (a search, not a full read; Claude read the memo, not the messages; members cited by role, not handle).
- Review page: the errata banner notes that its naming discussion is superseded.
- Works cited: group M (WCMesh Discord), 44 message links, plus the memo and the generator's `assets/app.js`.

Not yet reflected: a full read of the coordination thread; the SoCal administrator's own corrections.

## Earlier drafts

Working drafts 1 to 5 are not published here. The review of working draft 3 is archived as `review.html`, with the names of individual users withheld.
