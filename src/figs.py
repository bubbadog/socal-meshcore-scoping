"""Data-driven map figures. County outlines and area reference points come from the
matkam/meshcore-settings repository (MIT; boundaries are US Census TIGER, public domain)."""
import json, math, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
GEO = json.load(open(os.path.join(HERE, "geo.json")))
P = GEO["projection"]
VB = (312, 652, 562, 362)


def proj(lat, lon):
    return (P["k"] * (lon - P["lon0"]) * P["cos0"], P["k"] * (P["lat1"] - lat))


def centroid(d):
    subs = [s for s in d.split("M") if s.strip()]
    best = max(subs, key=len)
    nums = [float(x) for x in re.findall(r"-?\d+\.?\d*", best)]
    xs, ys = nums[0::2], nums[1::2]
    return (sum(xs) / len(xs), sum(ys) / len(ys))


CENT = {name: centroid(d) for name, d in GEO["shapes"].items()}


def base(extra, label):
    shapes = "".join(f'<path class="cty" d="{d}"/>' for d in GEO["shapes"].values())
    return (f'<svg viewBox="{VB[0]} {VB[1]} {VB[2]} {VB[3]}" role="img" aria-label="{label}">'
            f'{shapes}{extra}</svg>')


def pt(lat, lon, text, dx=7, dy=6, anchor="start", cls="dot", r=5.5, tcls="mlb"):
    x, y = proj(lat, lon)
    return (f'<circle class="{cls}" cx="{x:.1f}" cy="{y:.1f}" r="{r}"/>'
            f'<text class="{tcls}" x="{x + dx:.1f}" y="{y + dy:.1f}" text-anchor="{anchor}">{text}</text>')


# anchor points: airports from the analyzer where it publishes them, otherwise the generator's
# reference point for the area that contains the airport.
# value: lat, lon, label x, label y, anchor, leader (True draws a thin line from the point to the label)
AIR = {
    "sba": (34.4262, -119.8405, 390, 794, "middle", False), "oxr": (34.198, -119.177, 445, 722, "middle", True),
    "lax": (33.9425, -118.4081, 509, 722, "middle", True), "lgb": (33.77, -118.194, 492, 950, "middle", True),
    "sna": (33.746, -117.868, 548, 978, "middle", True), "ont": (34.064, -117.649, 582, 836, "start", False),
    "psp": (33.83, -116.545, 674, 874, "start", False), "san": (32.7338, -117.1933, 620, 977, "start", False),
}


def callout(x, y, lx, ly, text, anchor="middle", leader=True, tcls="mlb"):
    """A label at an absolute position, with an optional thin leader back to the point."""
    out = ""
    if leader:
        ey = ly + 6 if ly < y else ly - 20
        out += f'<line class="lead" x1="{x:.1f}" y1="{y:.1f}" x2="{lx:.1f}" y2="{ey:.1f}"/>'
    return out + f'<text class="{tcls}" x="{lx:.1f}" y="{ly:.1f}" text-anchor="{anchor}">{text}</text>'


def panel_airports(codes, label, upper=False):
    extra = ""
    for c in codes:
        lat, lon, lx, ly, a, lead = AIR[c]
        x, y = proj(lat, lon)
        extra += callout(x, y, lx, ly, c.upper() if upper else c, a, lead)
    for c in codes:
        x, y = proj(AIR[c][0], AIR[c][1])
        extra += f'<circle class="dot" cx="{x:.1f}" cy="{y:.1f}" r="5.5"/>'
    return base(extra, label)


def panel_generator():
    extra = ""
    for a in GEO["areas"]:
        x, y = proj(a["lat"], a["lon"])
        extra += f'<circle class="dot sm" cx="{x:.1f}" cy="{y:.1f}" r="3"/>'
    # county name: label x, label y, anchor, leader target (None for a label that sits on its county)
    lab = {"Santa Barbara": ("santabarbara", 318, 716, "start", (362, 752)), "Ventura": ("ventura", 448, 748, "middle", None),
           "Los Angeles": ("losangeles", 523, 797, "middle", None), "Orange": ("orangecounty", 440, 962, "start", (558, 893)),
           "San Bernardino": ("sanbernardino", 708, 760, "middle", None), "Riverside": ("riverside", 751, 880, "middle", None),
           "Imperial": ("imperial", 771, 934, "middle", None), "San Diego": ("sandiego", 642, 944, "middle", None)}
    for n, (code, lx, ly, anc, tgt) in lab.items():
        if tgt:
            ex = lx + (44 if anc == "start" else 0) if n == "Santa Barbara" else lx + 100
            ey = ly + 5 if n == "Santa Barbara" else ly - 12
            extra += f'<line class="lead" x1="{tgt[0]}" y1="{tgt[1]}" x2="{ex}" y2="{ey}"/>'
        extra += f'<text class="mlb cn" x="{lx}" y="{ly}" text-anchor="{anc}">{code}</text>'
    return base(extra, "County names and 52 local-area reference points from the generator")


def panel_wiki():
    lab = {"sb": (357, 762, None), "vta": (440, 772, None), "la": (523, 800, None), "ie": (600, 830, None),
           "oc": (562, 894, None), "sd": (640, 962, None)}
    extra = ""
    for code, (lx, ly, tgt) in lab.items():
        if tgt:
            extra += f'<line class="lead" x1="{tgt[0]}" y1="{tgt[1]}" x2="{lx + 6}" y2="{ly - 22}"/>'
        extra += f'<text class="mlb big" x="{lx}" y="{ly}" text-anchor="middle">{code}</text>'
    return base(extra, "Short county codes from the withdrawn March 2026 wiki draft")


def fig_names():
    panels = [
        ("Drafts v3 to v5 of this plan", "Eight airport-code metros, plus <code>&lt;metro&gt;-&lt;place&gt;</code> sub-regions",
         panel_airports(["sba", "oxr", "lax", "lgb", "sna", "ont", "psp", "san"], "Eight airport-code metros proposed in drafts v3 to v5")),
        ("matkam generator, since Aug 2026", "Eight county names and 52 local areas under <code>us</code>, <code>west</code>, <code>california</code>, <code>socal</code>", panel_generator()),
        ("MeshMapper zones", "Five zones. Zone boundaries are not published, so only the codes are placed.",
         panel_airports(["sba", "oxr", "lax", "psp", "san"], "Five MeshMapper zones", upper=True)),
        ("WCMesh wiki draft, 3 to 4 Mar 2026", "Six short codes under <code>us</code>, <code>ca</code>, <code>socal</code>. Withdrawn after about 22 hours.", panel_wiki()),
    ]
    out = ['<div class="maps">']
    for title, sub, svg in panels:
        out.append(f'<div class="mapp"><h4>{title}</h4>{svg}<p class="small">{sub}</p></div>')
    out.append("</div>")
    return "".join(out)


OBS = """SAN,32.74,-116.91
SAN,32.74,-117.23
LAX,33.73,-117.86
SAN,33.23,-117.11
OXR,34.23,-118.99
SAN,33.23,-117.11
LAX,34.55,-117.14
LGB,33.72,-118.05
LAX,33.83,-118.29
LAX,33.88,-118.37
SNA,33.75,-117.87
OXR,34.17,-119.04
LAX,33.83,-118.29
OXR,34.25,-119.17
LAX,33.80,-118.36
LAX,34.18,-118.13
ONT,33.94,-117.52
SBA,34.61,-120.19
SBA,34.44,-119.72
LAX,33.84,-118.39
SAN,33.16,-117.05
LAX,34.57,-117.94
LAX,33.94,-117.38
ONT,34.04,-117.17
SAN,33.01,-117.18
LAX,34.14,-118.10
LAX,34.15,-117.84
SAN,32.90,-117.16
SAN,33.21,-117.21
PSP,33.77,-116.45
LAX,34.17,-118.16
SAN,32.97,-117.04
SBA,34.44,-119.92
SAN,32.92,-117.23
LAX,33.83,-118.29
ONT,33.94,-117.52
ONT,33.94,-117.52"""


def fig_observers():
    extra = ""
    rows = [r.split(",") for r in OBS.splitlines()]
    seen = set()
    for tag, lat, lon in rows:
        key = (tag, lat, lon)
        if key in seen:
            continue
        seen.add(key)
        x, y = proj(float(lat), float(lon))
        if tag == "LAX":
            extra += f'<circle class="dot" cx="{x:.1f}" cy="{y:.1f}" r="6"><title>Tagged LAX at {lat}, {lon}</title></circle>'
        else:
            extra += (f'<circle class="ring" cx="{x:.1f}" cy="{y:.1f}" r="6"><title>Tagged {tag} at {lat}, {lon}</title></circle>'
                      f'<text class="mlb tiny" x="{x + 9:.1f}" y="{y + 5:.1f}">{tag}</text>')
    for lat, lon, text, dx, dy, anc in ((34.55, -117.14, "LAX tag, Victor Valley", 10, 5, "start"), (33.94, -117.38, "LAX tag, Riverside", 10, 16, "start"),
                                        (33.73, -117.86, "LAX tag, Santa Ana", -10, 22, "end"), (34.57, -117.94, "LAX tag, Antelope Valley", 0, -12, "middle")):
        x, y = proj(lat, lon)
        extra += f'<text class="mlb tiny em" x="{x + dx:.1f}" y="{y + dy:.1f}" text-anchor="{anc}">{text}</text>'
    n_lax = len({(t, a, o) for t, a, o in map(tuple, rows) if t == "LAX"})
    return base(extra, "Observer positions by self-assigned region tag; LAX-tagged observers appear in Orange, Riverside and San Bernardino counties"), len(seen), n_lax


def fig_conejo():
    lat0, lon0 = 34.30, -119.07
    kx = math.cos(math.radians(34.2)) * 111.32
    ky = 110.9
    s = 20.0  # px per km

    def xy(lat, lon):
        return ((lon - lon0) * kx * s, (lat0 - lat) * ky * s)

    W, H = (-118.71 - lon0) * kx * s, (lat0 - 34.14) * ky * s
    sky = (34.19, -118.89)
    # name, lat, lon, observations, label dx, label dy, anchor, leader
    nb = [("NP Valley Spare", 34.18057, -118.92192, 209, -10, 8, "end", False), ("Highest in the Neighbor", 34.27404, -118.79211, 160, -12, -6, "end", False),
          ("COMT", 34.18836, -118.98423, 71, 0, -11, "middle", False), ("NP 700 ASL", 34.17329, -118.92032, 71, -10, 14, "end", False),
          ("Green R1", 34.19194, -118.90236, 42, 30, -30, "end", True), ("RASN", 34.167854, -118.909474, 9, 4, 22, "middle", False),
          ("NP-CAM Grade", 34.20107, -118.95309, 5, 8, -11, "end", False)]
    sx, sy = xy(*sky)
    out = ""
    for name, lat, lon, obs, dx, dy, a, lead in nb:
        x, y = xy(lat, lon)
        w = 1.2 + 5.0 * obs / 209
        out += f'<line class="lnk" x1="{sx:.1f}" y1="{sy:.1f}" x2="{x:.1f}" y2="{y:.1f}" stroke-width="{w:.1f}"/>'
    for name, lat, lon, obs, dx, dy, a, lead in nb:
        x, y = xy(lat, lon)
        if lead:
            out += f'<line class="lead" x1="{x:.1f}" y1="{y - 5:.1f}" x2="{x + dx - 22:.1f}" y2="{y + dy + 4:.1f}"/>'
        out += (f'<circle class="ring fillbg" cx="{x:.1f}" cy="{y:.1f}" r="5"/>'
                f'<text class="mlb tiny" x="{x + dx:.1f}" y="{y + dy:.1f}" text-anchor="{a}">{name} ({obs})</text>')
    out += f'<circle class="dot" cx="{sx:.1f}" cy="{sy:.1f}" r="7"/><text class="mlb tiny em" x="{sx + 12:.1f}" y="{sy + 5:.1f}">SkyNet</text>'
    for name, lat, lon, dx, dy, a in (("Conejo Valley", 34.17, -118.838, 11, 4, "start"), ("Simi Valley", 34.269, -118.781, 11, 4, "start")):
        x, y = xy(lat, lon)
        out += (f'<rect class="sq" x="{x - 5:.1f}" y="{y - 5:.1f}" width="10" height="10"/>'
                f'<text class="mlb tiny" x="{x + dx:.1f}" y="{y + dy:.1f}" text-anchor="{a}">{name}</text>')
    for lat, lon in ((34.23, -118.99),):
        x, y = xy(lat, lon)
        out += (f'<path class="tri" d="M{x:.1f} {y - 7:.1f} L{x + 7:.1f} {y + 6:.1f} L{x - 7:.1f} {y + 6:.1f}Z"/>'
                f'<text class="mlb tiny" x="{x:.1f}" y="{y - 13:.1f}" text-anchor="middle">Observer tagged OXR</text>')
    bx, by = 14, H - 16
    out += (f'<line class="lnk" x1="{bx}" y1="{by}" x2="{bx + 5 * s}" y2="{by}" stroke-width="2"/>'
            f'<text class="mlb tiny" x="{bx}" y="{by - 7}">5 km</text>')
    return (f'<svg viewBox="0 0 {W:.0f} {H:.0f}" role="img" aria-label="SkyNet and its seven analyzer-resolved neighbors. '
            f'Line weight shows observation count. Highest in the Neighbor sits beside the Simi Valley reference point.">{out}</svg>')


# Ranges as straight strokes at approximate positions (lat, lon), for orientation only.
# label: text x, y, anchor, then an optional leader line (x1, y1, x2, y2) in map units
RANGES = [
    ("Santa Ynez Mtns", [(34.50, -120.25), (34.50, -119.75), (34.47, -119.45)], (389, 789, "middle", None)),
    ("Santa Susana Mtns", [(34.37, -118.85), (34.34, -118.55)], (425, 728, "middle", (479, 811, 432, 734))),
    ("San Gabriel Mtns", [(34.40, -118.45), (34.33, -118.05), (34.27, -117.60)], (522, 792, "middle", None)),
    ("Simi Hills", [(34.235, -118.78), (34.21, -118.65)], (462, 900, "middle", (484, 829, 466, 889))),
    ("Santa Monica Mtns", [(34.09, -119.05), (34.10, -118.75), (34.13, -118.40)], (452, 876, "end", (462, 843, 440, 865))),
    ("San Bernardino Mtns", [(34.27, -117.40), (34.20, -117.00), (34.10, -116.72)], (666, 828, "start", None)),
    ("San Jacinto Mtns", [(33.87, -116.75), (33.62, -116.58)], (672, 884, "start", None)),
    ("Santa Ana Mtns", [(33.95, -117.75), (33.78, -117.60), (33.55, -117.42)], (560, 944, "end", (588, 893, 550, 932))),
    ("Cuyamaca and Laguna Mtns", [(33.10, -116.62), (32.80, -116.45)], (684, 966, "start", None)),
]
PASSES = [("A", "Conejo Grade", 34.205, -118.99, -9, -5), ("B", "Santa Susana Pass", 34.27, -118.63, -3, -7), ("C", "Newhall Pass", 34.335, -118.51, 6, -6),
          ("D", "Sepulveda Pass", 34.115, -118.475, -4, 14), ("E", "Cahuenga Pass", 34.125, -118.345, 7, 12), ("F", "Santa Ana Canyon", 33.87, -117.72, -12, 4),
          ("G", "Cajon Pass", 34.31, -117.47, 1, -8), ("H", "San Gorgonio Pass", 33.925, -116.85, -4, -8)]


def fig_terrain():
    extra = ""
    for name, pts, (lx, ly, anc, lead) in RANGES:
        xy = [proj(a, b) for a, b in pts]
        extra += '<polyline class="rng" points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in xy) + '"/>'
    for name, pts, (lx, ly, anc, lead) in RANGES:
        if lead:
            extra += f'<line class="lead" x1="{lead[0]}" y1="{lead[1]}" x2="{lead[2]}" y2="{lead[3]}"/>'
        extra += f'<text class="mlb rg" x="{lx}" y="{ly}" text-anchor="{anc}">{name}</text>'
    for letter, name, lat, lon, dx, dy in PASSES:
        x, y = proj(lat, lon)
        extra += (f'<path class="pass" d="M{x:.1f} {y - 4.5:.1f} L{x + 4.5:.1f} {y:.1f} L{x:.1f} {y + 4.5:.1f} L{x - 4.5:.1f} {y:.1f}Z"><title>{name}</title></path>'
                  f'<text class="mlb ps" x="{x + dx:.1f}" y="{y + dy:.1f}" text-anchor="middle">{letter}</text>')
    svg = base(extra, "Southern California counties with nine mountain barriers drawn as strokes and eight passes marked by letters")
    key = " ".join(f"<span><b>{letter}</b> {name}</span>" for letter, name, *_ in PASSES)
    return svg, key
