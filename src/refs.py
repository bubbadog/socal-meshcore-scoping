# Works cited for the red-team report. Order here is the numbering order.
# (key, group, citation_html, url, kind)   kind: 'gh' = GitHub blob (line pins become #L anchors), '' = plain

FW = "https://github.com/meshcore-dev/MeshCore/blob/d92964352441e53b93e8667b802e04f6e072b39e/"
WC = "https://github.com/chrisdavis2110/WCMesh-Docs/blob/f447a3bcc7653634fd760bb5341f587c812509e2/"
MK = "https://github.com/matkam/meshcore-settings/blob/331ffd284381cd3b2db5b763a9e15f3defe8948f/"
CS = "https://github.com/Kpa-clawbot/CoreScope/blob/8d2ae405e8f2ba4b9bdb09866f563053375a908b/"
API = "https://corescope.wcmesh.com/api/"
SKY = "88ea9dfd8cdd8f50a6402afa3d58054340775fcad0a7c15e5be1ad9470697d56"

GROUPS = [
    ("A", "The document under review"),
    ("B", "MeshCore firmware source, release tag repeater-v1.17.1 (commit d929643, 14 Aug 2026) unless another tag is named"),
    ("C", "MeshCore project posts and releases"),
    ("D", "West Coast Mesh documentation (repository chrisdavis2110/WCMesh-Docs at commit f447a3b, 16 Aug 2026)"),
    ("E", "matkam California scheme and generator (repository matkam/meshcore-settings at commit 331ffd2, 12 Sep 2026)"),
    ("F", "Other communities' rollout documents"),
    ("G", "Live analyzer data: CoreScope, WCMesh instance, software v3.12.0, fetched 13 Oct 2026 between 07:30 and 07:50 UTC"),
    ("H", "MeshMapper"),
    ("I", "Geography (Wikipedia; tertiary sources, used only for terrain layout)"),
    ("J", "This review's own measurements and calculations"),
    ("L", "Material supplied during the review"),
    ("K", "Other items from the plan's reference list"),
]

REFS = [
    # A
    ("plan", "A", "<i>SoCal MeshCore Scoping Plan</i>, working draft 3 (internal), \"topography review\", dated 13 October 2026, marked \"Not yet adopted\", produced by the author with Muse. Reviewed from the HTML file the author supplied (1.56 MB). Section numbers (&sect;01 to &sect;10) and RT numbers refer to that file. Claude's tools could not fetch the hosted copy.", "https://muse.ai/s/socal-meshcore-scoping-plan-xkxl6s4xvxlkcoxy", ""),
    ("plan5", "A", "<i>SoCal MeshCore Scoping Plan</i>, working draft 5 (internal), \"public-records review\", dated 13 October 2026, produced with Muse and supplied by the author as an HTML file (1.58 MB). Section numbers and RT numbers refer to that file.", "", ""),
    # B
    ("fw-regionmap-h", "B", "<code>src/helpers/RegionMap.h</code>. Region table size, deny flag, name buffer.", FW + "src/helpers/RegionMap.h", "gh"),
    ("fw-regionmap", "B", "<code>src/helpers/RegionMap.cpp</code>. Name rules, key selection, scope matching, prefix lookup, removal.", FW + "src/helpers/RegionMap.cpp", "gh"),
    ("fw-tks", "B", "<code>src/helpers/TransportKeyStore.cpp</code> and <code>.h</code>. Transport code calculation and key derivation.", FW + "src/helpers/TransportKeyStore.cpp", "gh"),
    ("fw-routing", "B", "<code>src/helpers/RoutingPolicy.h</code>. Hop limits and reply-scope policy.", FW + "src/helpers/RoutingPolicy.h", "gh"),
    ("fw-rep", "B", "<code>examples/simple_repeater/MyMesh.cpp</code>. Repeater forwarding gate, loop detection, defaults, scoped adverts and replies.", FW + "examples/simple_repeater/MyMesh.cpp", "gh"),
    ("fw-cli", "B", "<code>src/helpers/CommonCLI.cpp</code>. <code>region</code> and <code>set</code> command handlers.", FW + "src/helpers/CommonCLI.cpp", "gh"),
    ("fw-comp", "B", "<code>examples/companion_radio/MyMesh.cpp</code>. Companion scope selection and app commands.", FW + "examples/companion_radio/MyMesh.cpp", "gh"),
    ("fw-chat", "B", "<code>src/helpers/BaseChatMesh.cpp</code> and <code>.h</code>. Message length limit, channel text prefix, path returns.", FW + "src/helpers/BaseChatMesh.cpp", "gh"),
    ("fw-packet", "B", "<code>src/Packet.h</code> and <code>src/Packet.cpp</code>. Route types and on-air transport code bytes.", FW + "src/Packet.cpp", "gh"),
    ("fw-tables", "B", "<code>src/helpers/SimpleMeshTables.h</code>. Duplicate-detection table size.", FW + "src/helpers/SimpleMeshTables.h", "gh"),
    ("fw-dispatcher", "B", "<code>src/Dispatcher.cpp</code>. Receive airtime accounting.", FW + "src/Dispatcher.cpp", "gh"),
    ("fw-radio", "B", "<code>src/helpers/radiolib/RadioLibWrappers.h</code>. Preamble length by spreading factor.", FW + "src/helpers/radiolib/RadioLibWrappers.h", "gh"),
    ("fw-stats", "B", "<code>src/helpers/StatsFormatHelper.h</code>. Fields returned by the stats commands.", FW + "src/helpers/StatsFormatHelper.h", "gh"),
    ("fw-docs-cli", "B", "<code>docs/cli_commands.md</code>. The CLI reference the plan cites.", FW + "docs/cli_commands.md", "gh"),
    ("fw-docs-faq", "B", "<code>docs/faq.md</code>. The FAQ the plan cites. It contains no occurrence of the word \"scope\" and no 137 or 127 figure.", FW + "docs/faq.md", "gh"),
    ("fw-v111", "B", "<code>src/helpers/RegionMap.cpp</code> at tag repeater-v1.11.0 (commit 6d32193, 30 Nov 2025). Only names starting with <code>#</code> receive an automatic key.", "https://github.com/meshcore-dev/MeshCore/blob/6d3219329fc1170106a355fed942a3e032e38efb/src/helpers/RegionMap.cpp", "gh"),
    ("fw-v112", "B", "<code>src/helpers/RegionMap.cpp</code> at tag repeater-v1.12.0 (commit e738a74, 29 Jan 2026). Plain names get an implicit <code>#</code>.", "https://github.com/meshcore-dev/MeshCore/blob/e738a7477737964464038a87b3113a7a0ce7ebbc/src/helpers/RegionMap.cpp", "gh"),
    ("fw-v1141", "B", "<code>examples/simple_repeater/MyMesh.cpp</code> at tag repeater-v1.14.1 (commit 467959c, 20 Mar 2026). <code>region put</code> leaves a new region denied; no <code>region default</code>.", "https://github.com/meshcore-dev/MeshCore/blob/467959cc3bfc884e5f3425caac89453a450151b6/examples/simple_repeater/MyMesh.cpp", "gh"),
    ("fw-v115", "B", "<code>src/helpers/CommonCLI.cpp</code> at tag repeater-v1.15.0 (commit dee3e26, 19 Apr 2026). First release with <code>region default</code> and allow-by-default <code>region put</code>; no <code>region def</code>.", "https://github.com/meshcore-dev/MeshCore/blob/dee3e26ac081a5c668c69b66c16a6544a44ddc5b/src/helpers/CommonCLI.cpp", "gh"),
    # C
    ("blog-region", "C", "Powell, S. \"Region Filtering.\" MeshCore Blog, 20 Jan 2026, with edits dated 25 Jan and 20 Feb 2026.", "https://blog.meshcore.io/2026/01/20/region-filtering", ""),
    ("blog-default", "C", "Powell, S. \"Default Scope Region.\" MeshCore Blog, 17 Apr 2026.", "https://blog.meshcore.io/2026/04/17/default-scope", ""),
    ("blog-116", "C", "\"Release v1.16.0.\" MeshCore Blog, 6 Jun 2026.", "https://blog.meshcore.io/2026/06/06/release-1-16-0", ""),
    ("gh-tags", "C", "MeshCore release tags and dates, read from the repository: v1.10.0 (13 Nov 2025), v1.11.0 (30 Nov 2025), v1.12.0 (29 Jan 2026), v1.14.1 (20 Mar 2026), v1.15.0 (19 Apr 2026), v1.16.0 (6 Jun 2026), v1.17.1 (14 Aug 2026, newest repeater tag on 13 Oct 2026).", "https://github.com/meshcore-dev/MeshCore/releases", ""),
    # D
    ("wc-q2", "D", "\"State of the Mesh, Q2 2026\", dated 7/26/2026. <code>docs/state-of-the-mesh/q2-2026.md</code>.", WC + "docs/state-of-the-mesh/q2-2026.md?plain=1", "gh"),
    ("wc-q1", "D", "\"State of the Mesh, Q1 2026\", dated 4/12/2026. <code>docs/state-of-the-mesh/q1-2026.md</code>.", WC + "docs/state-of-the-mesh/q1-2026.md?plain=1", "gh"),
    ("wc-radio", "D", "\"Radio Settings\". <code>docs/radio-settings.md</code>. Regional presets and the recommended repeater settings.", WC + "docs/radio-settings.md?plain=1", "gh"),
    ("wc-setup", "D", "\"Setting up a repeater\". <code>docs/getting-started/setting-up-repeater.md</code>.", WC + "docs/getting-started/setting-up-repeater.md?plain=1", "gh"),
    ("wc-multibyte", "D", "Multi-byte path guidance. <code>docs/multibyte.md</code>.", WC + "docs/multibyte.md?plain=1", "gh"),
    ("wc-channels", "D", "\"Public Channels\". <code>docs/public-channels.md</code>.", WC + "docs/public-channels.md?plain=1", "gh"),
    ("wc-regions-old", "D", "\"SoCal Regions\", the region guide added to the WCMesh docs on 3 Mar 2026 (commit 883ed05) and removed on 4 Mar 2026 (commit d25e1dc, message \"removed regions\"). Recovered from git history.", "https://github.com/chrisdavis2110/WCMesh-Docs/blob/883ed059f0b05b55407bdbb2a6755c9acc997439/docs/regions/socal-regions.md?plain=1", "gh"),
    ("wc-regions-index", "D", "\"Regions\" explainer page from the same withdrawn guide, <code>docs/regions/index.md</code> at commit 883ed05.", "https://github.com/chrisdavis2110/WCMesh-Docs/blob/883ed059f0b05b55407bdbb2a6755c9acc997439/docs/regions/index.md?plain=1", "gh"),
    ("wc-log", "D", "Commit history of the WCMesh docs repository up to commit f447a3b. Five commits since 26 Jul 2026: \"added sotm q2\", \"fixed a tag warnings\" and \"renamed docs\" (26 Jul), \"added recommended settings\" (3 Aug), \"added mqtt\" (16 Aug). The region guide's commits are timed 2 Mar 13:29, 3 Mar 22:40 and 4 Mar 20:50, Pacific time.", "https://github.com/chrisdavis2110/WCMesh-Docs/commits/f447a3bcc7653634fd760bb5341f587c812509e2/", ""),
    ("wc-regions-rm", "D", "Commit d25e1dc, \"removed regions\", 4 Mar 2026.", "https://github.com/chrisdavis2110/WCMesh-Docs/commit/d25e1dc0b8b6084fe43ef2a085e6e5d8fd0527ef", ""),
    # E
    ("mk-data", "E", "<code>data/regions.yaml</code>. The data file that drives the generator: root chain, levels, tags and places.", MK + "data/regions.yaml", "gh"),
    ("mk-outlines", "E", "<code>data/outlines.json</code>. County outline shapes used for the maps in this document. Its notice reads: boundaries from US Census TIGER/Line via the click_that_hood project (MIT); Census boundary data is in the public domain.", MK + "data/outlines.json", "gh"),
    ("mk-readme", "E", "<code>README.md</code>. Still describes <code>socal</code> as a tag.", MK + "README.md?plain=1", "gh"),
    ("mk-c1", "E", "Commit 9274a00, \"updated socal regions\", author chrisdavis2110, 3 Aug 2026.", "https://github.com/matkam/meshcore-settings/commit/9274a003bdc41b716806662e7b1a19e7867d9c8b", ""),
    ("mk-c2", "E", "Commit f23e76c, \"fine tuned socal - lowest is areas within counties\", author chrisdavis2110, 24 Aug 2026.", "https://github.com/matkam/meshcore-settings/commit/f23e76c78c837f3c69a000ddba84e9588e2fcc64", ""),
    # F
    ("ca-onqc", "F", "MeshCore Canada. \"ON/QC scopes\" proposal, status experimental, last reviewed 24 Sep 2026. <code>docs/proposals/onqc-scopes.md</code> at commit fe3a82e (26 Sep 2026).", "https://github.com/meshcore-ca/meshcore-canada/blob/fe3a82ec2a7154ee626d594e8aed1c7d2be9aef8/docs/proposals/onqc-scopes.md?plain=1", "gh"),
    ("scot-regions", "F", "ScotMesh wiki. <code>MeshCore/regions.md</code> at commit 1f931bb (30 Aug 2026).", "https://github.com/jamiephonic/scotmesh-wiki/blob/1f931bb1b2732b4abae32a23982f9135494b3dd0/MeshCore/regions.md?plain=1", "gh"),
    ("scot-channels", "F", "ScotMesh wiki. <code>MeshCore/channels.md</code> at commit 1f931bb.", "https://github.com/jamiephonic/scotmesh-wiki/blob/1f931bb1b2732b4abae32a23982f9135494b3dd0/MeshCore/channels.md?plain=1", "gh"),
    ("nl-guide", "F", "Meshcore Netherlands settings guide. <code>src/en/index.md</code> at commit 90d38a7 (27 Aug 2026).", "https://github.com/greentown0/meshcore-settings-site/blob/90d38a7c89a34439164a4b0b5afa0ac2b56a61f5/src/en/index.md?plain=1", "gh"),
    ("nl-commits", "F", "Commit history of the Netherlands guide: \"Added step 8 to enable strict regions in June instead of May\" (27 Apr 2026); \"Postpone Phase 8 to 18 July 2026, add delay explanation\" (10 Jun 2026).", "https://github.com/greentown0/meshcore-settings-site/commits/90d38a7c89a34439164a4b0b5afa0ac2b56a61f5/", ""),
    ("pnw-rollout", "F", "Gessaman, A. \"PNW MeshCore regions rollout\". <code>pnw-meshcore-regions-rollout.md</code> at commit 47c3aed (6 Sep 2026).", "https://github.com/agessaman/meshcore-regions/blob/47c3aedc0e3f182a4f0e339d09ce1cba826021e7/pnw-meshcore-regions-rollout.md?plain=1", "gh"),
    ("pnw-strategy", "F", "Gessaman, A. \"PNW MeshCore regions\" strategy document. <code>pnw-meshcore-regions.md</code> at commit 47c3aed.", "https://github.com/agessaman/meshcore-regions/blob/47c3aedc0e3f182a4f0e339d09ce1cba826021e7/pnw-meshcore-regions.md?plain=1", "gh"),
    # G
    ("cs-stats", "G", "<code>/api/stats</code>. Node, repeater and observer totals.", API + "stats", ""),
    ("cs-regions", "G", "<code>/api/config/regions</code>. The eleven region labels.", API + "config/regions", ""),
    ("cs-scope", "G", "<code>/api/scope-stats</code>, windows 24h and 7d.", API + "scope-stats?window=24h", ""),
    ("cs-audit", "G", "<code>/api/scope-audit?window=7d</code>. Regions each audited repeater declares.", API + "scope-audit?window=7d", ""),
    ("cs-rf", "G", "<code>/api/analytics/rf</code>. Transmissions by payload type over 168 hours.", API + "analytics/rf", ""),
    ("cs-airtime", "G", "<code>/api/analytics/relay-airtime-share?window=24h</code>. Time on air multiplied by distinct relays, by payload type.", API + "analytics/relay-airtime-share?window=24h", ""),
    ("cs-retx", "G", "<code>/api/analytics/retransmissions?window=7d&amp;bucket=1d</code>. Flood events and distinct relays per flood.", API + "analytics/retransmissions?window=7d&bucket=1d", ""),
    ("cs-topo", "G", "<code>/api/analytics/topology</code>. Hop-count distribution.", API + "analytics/topology", ""),
    ("cs-channels", "G", "<code>/api/channels</code>. Message count per decodable channel in the retained window.", API + "channels", ""),
    ("cs-observers", "G", "<code>/api/observers</code>. The 58 observers, their positions and region tags (server time 2026-10-13T07:49:16Z).", API + "observers", ""),
    ("cs-hash", "G", "<code>/api/analytics/hash-sizes</code>. Path hash size by packet and by repeater.", API + "analytics/hash-sizes", ""),
    ("cs-skynet", "G", "<code>/api/nodes/88ea9dfd...7d56</code> with <code>/neighbors</code> and <code>/hop_analytics</code>. SkyNet node record.", API + "nodes/" + SKY, ""),
    ("cs-advert", "G", "<code>/api/packets/1146777</code>. SkyNet flood advert of 2026-10-11T00:40:47Z, hash b726bf9b17d24bda, 64 observations.", API + "packets/1146777", ""),
    ("cs-packets", "G", "<code>/api/packets?route=0</code>, with <code>type=4</code> and <code>type=5</code> pages. Transport-route packets with raw bytes.", API + "packets?route=0&limit=60", ""),
    ("cs-rancho", "G", "<code>/api/nodes/search?q=Rancho%20North</code>. Node record for Rancho North (key ae229b60..., 33.8006, -116.3969).", API + "nodes/search?q=Rancho%20North", ""),
    ("cs-highest", "G", "<code>/api/nodes/search?q=Highest</code>, fetched later the same day, at about 15:40 UTC. Position of the repeater \"Highest in the Neighbor\".", API + "nodes/search?q=Highest", ""),
    ("cs-conejo", "G", "<code>/api/nodes/search</code> for NP, RASN, Green R1 and COMT, fetched 13 Oct 2026 at about 17:10 UTC. Positions of the repeaters near SkyNet.", API + "nodes/search?q=NP", ""),
    ("cs-iata", "G", "<code>/api/iata-coords</code>, fetched 13 Oct 2026 at about 17:10 UTC. Airport positions for LAX, SAN and SBA; the other SoCal codes are not in it.", API + "iata-coords", ""),
    ("cs-src-db", "G", "CoreScope source, <code>cmd/server/db.go</code> at commit 8d2ae40 (13 Oct 2026). How the scoped and unscoped totals are computed.", CS + "cmd/server/db.go", "gh"),
    ("cs-src-cfg", "G", "CoreScope source, <code>config.example.json</code>. The <code>hashRegions</code> setting.", CS + "config.example.json", "gh"),
    ("cs-readme", "G", "CoreScope source, <code>README.md</code> and <code>cmd/ingestor/observer_fields.go</code>. Region codes come from each observer's own configuration.", CS + "README.md?plain=1", "gh"),
    # H
    ("mm-socal", "H", "MeshMapper, SoCal region map, software v1.5.142, as rendered on 13 Oct 2026. Read through an automated page summary, not the raw page.", "https://socal.meshmapper.net/", ""),
    ("mm-board", "H", "MeshMapper, global leaderboard, marked \"Last Updated: Oct 13, 09:33\". Claude's fetch returned only part of the page: it confirmed the multibyte figures for Los Angeles and San Diego and did not reach the other SoCal rows or the scope columns.", "https://meshmapper.net/global_leaderboard.php", ""),
    ("mm-admin", "H", "MeshMapper wiki, \"Admins\". Wardriving Scope, Scopes to Monitor, scope discovery, ping interval.", "https://wiki.meshmapper.net/admins/", ""),
    ("mm-start", "H", "MeshMapper wiki, \"Getting started\" for the app. How a wardriving ping is sent.", "https://wiki.meshmapper.net/app_getting_started/", ""),
    # I
    ("geo-smm", "I", "\"Santa Monica Mountains.\"", "https://en.wikipedia.org/wiki/Santa_Monica_Mountains", ""),
    ("geo-simi", "I", "\"Simi Hills.\"", "https://en.wikipedia.org/wiki/Simi_Hills", ""),
    ("geo-susana", "I", "\"Santa Susana Mountains.\"", "https://en.wikipedia.org/wiki/Santa_Susana_Mountains", ""),
    ("geo-scv", "I", "\"Santa Clarita Valley.\"", "https://en.wikipedia.org/wiki/Santa_Clarita_Valley", ""),
    ("geo-sgm", "I", "\"San Gabriel Mountains.\"", "https://en.wikipedia.org/wiki/San_Gabriel_Mountains", ""),
    ("geo-grade", "I", "\"Conejo Grade.\"", "https://en.wikipedia.org/wiki/Conejo_Grade", ""),
    ("geo-pomona", "I", "\"Pomona Valley.\"", "https://en.wikipedia.org/wiki/Pomona_Valley", ""),
    ("geo-sac", "I", "\"Santa Ana Canyon.\"", "https://en.wikipedia.org/wiki/Santa_Ana_Canyon", ""),
    ("geo-east", "I", "\"East County, San Diego.\"", "https://en.wikipedia.org/wiki/East_County,_San_Diego", ""),
    ("geo-cajon", "I", "\"Cajon Pass.\"", "https://en.wikipedia.org/wiki/Cajon_Pass", ""),
    ("geo-gorgonio", "I", "\"San Gorgonio Pass.\"", "https://en.wikipedia.org/wiki/San_Gorgonio_Pass", ""),
    ("geo-ynez", "I", "\"Santa Ynez Mountains.\"", "https://en.wikipedia.org/wiki/Santa_Ynez_Mountains", ""),
    # J
    ("own-telemetry", "J", "SkyNet repeater counters read by the author from the repeater's admin screen on 10 Oct 2026: a lifetime snapshot at about 4:30 pm PDT and a second about 46 minutes later. The figures are as transcribed from the author's screenshots that day. The screenshots are not published.", "", ""),
    ("own-decode", "J", "Scope decoding performed by Claude for the red-team review. The method, a reproducible script and the repeater packets are in the appendix.", "#app-b", ""),
    ("own-toa", "J", "Time-on-air calculation for this review, in Appendix C. It reproduces the arithmetic of RadioLib's <code>SX126x::calculateTimeOnAir</code>, the routine the firmware calls for airtime estimates.", "https://github.com/jgromes/RadioLib/blob/4df94a9adb71e0fdeee8d15efed75c8ac4511544/src/modules/SX126x/SX126x.cpp", ""),
    ("own-image", "J", "My inspection of the plan's embedded terrain map (one 1520 by 1760 pixel PNG, 1.49 MB of the 1.56 MB file).", "", ""),
    # L
    ("memo", "L", "Public-source research memo written on 13 October 2026 by Muse at the author's request. Unpublished. It states that it could not join the Discord server. It was treated as a list of leads to check, and it is cited only for what it reports that Claude could not confirm independently.", "", ""),
    # K
    ("k7cfo", "K", "k7cfo/wcmesh, <code>README.md</code> at commit e2ad731 (28 May 2026). A 64-line overview of West Coast Mesh; nothing on regions or scopes.", "https://github.com/k7cfo/wcmesh/blob/e2ad731e5cb654824445d9467fc400af488b3565/README.md", "gh"),
    ("wc-start", "K", "WCMesh docs, \"Getting started\". <code>docs/getting-started/index.md</code> at commit f447a3b. Carries the same radio settings table.", WC + "docs/getting-started/index.md?plain=1", "gh"),
    ("bot-release", "K", "agessaman/meshcore-bot, release v1.1.0.", "https://github.com/agessaman/meshcore-bot/releases/tag/v1.1.0", ""),
    ("yt-1", "K", "LDSPrepper. \"URGENT, DO THIS NOW! - How &amp; Why To Set Regions for a MeshCore Repeater in the Intermountain West.\" YouTube. Title confirmed through the oEmbed record; the video itself was not watched.", "https://www.youtube.com/watch?v=qzr_fOs1UoQ", ""),
    ("yt-2", "K", "Ham Radio 2.0. \"Meshcore 1.16.0 - New Flood Traffic Controls for Repeater Operators.\" YouTube. Title confirmed through the oEmbed record; the video itself was not watched.", "https://www.youtube.com/watch?v=uHpPU0agA0U", ""),
]
