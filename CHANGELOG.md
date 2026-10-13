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

Not yet reflected: anything said in the WCMesh Discord.

## Earlier drafts

Drafts v1 to v5 were working drafts and are not published here. The review of Draft v3 is archived as `review.html`, with the names of individual users withheld.
