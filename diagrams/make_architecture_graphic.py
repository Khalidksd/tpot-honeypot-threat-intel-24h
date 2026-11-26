"""Operation Honeycomb: illustrated architecture graphic (1920x1080)."""
import math

W, H = 1920, 1080
F = "Inter, 'DejaVu Sans', sans-serif"
o = []
a = o.append

RED, ORANGE, AMBER, TEAL, BLUE, PURPLE, GREEN = "#e11d48", "#f59e0b", "#fbbf24", "#0d9488", "#2563eb", "#7c3aed", "#16a34a"
INK, MUTED, DARK = "#0f172a", "#475569", "#1e293b"

def T(x, y, s, size=16, w=400, fill=INK, anchor="start", ls=0):
    a(f'<text x="{x}" y="{y}" font-family="{F}" font-size="{size}" font-weight="{w}" fill="{fill}" '
      f'text-anchor="{anchor}" letter-spacing="{ls}">{s}</text>')

def rect(x, y, w, h, fill, r=12, stroke="none", sw=0, op=1, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    a(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" opacity="{op}"{d}/>')

def shadow_card(x, y, w, h, fill="#fff", stroke="#e2e8f0", r=18):
    rect(x, y + 5, w, h, "#0f172a", r, op=0.07)
    rect(x, y, w, h, fill, r, stroke, 1.5)

def badge(cx, cy, n, col):
    a(f'<circle cx="{cx}" cy="{cy}" r="19" fill="{col}" stroke="#fff" stroke-width="3"/>')
    T(cx, cy + 7, str(n), 19, 800, "#fff", "middle")

def arrow(d, col, w=5, dash=None, mk="aI"):
    ds = f' stroke-dasharray="{dash}"' if dash else ""
    a(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"{ds} marker-end="url(#{mk})"/>')

# ---------- icons ----------
def hacker(cx, cy, s=1.0):
    # hood
    a(f'<path d="M{cx-48*s} {cy+52*s} C{cx-52*s} {cy-10*s} {cx-34*s} {cy-58*s} {cx} {cy-60*s} '
      f'C{cx+34*s} {cy-58*s} {cx+52*s} {cy-10*s} {cx+48*s} {cy+52*s} Z" fill="{DARK}"/>')
    a(f'<ellipse cx="{cx}" cy="{cy-8*s}" rx="{24*s}" ry="{29*s}" fill="#0b1120"/>')
    # glowing eyes
    a(f'<ellipse cx="{cx-9*s}" cy="{cy-10*s}" rx="{5*s}" ry="{2.6*s}" fill="{RED}"/>')
    a(f'<ellipse cx="{cx+9*s}" cy="{cy-10*s}" rx="{5*s}" ry="{2.6*s}" fill="{RED}"/>')
    # laptop
    a(f'<path d="M{cx-44*s} {cy+30*s} H{cx+44*s} L{cx+56*s} {cy+62*s} H{cx-56*s} Z" fill="#334155"/>')
    a(f'<rect x="{cx-38*s}" y="{cy+6*s}" width="{76*s}" height="{28*s}" rx="{3*s}" fill="#475569"/>')
    a(f'<rect x="{cx-33*s}" y="{cy+10*s}" width="{66*s}" height="{20*s}" rx="{2*s}" fill="{RED}" opacity="0.85"/>')
    T(cx, cy + 25 * s, "&gt;_ attack", 11 * s, 700, "#fff", "middle")

def robot(cx, cy, s=1.0, col="#64748b"):
    a(f'<line x1="{cx}" y1="{cy-26*s}" x2="{cx}" y2="{cy-16*s}" stroke="{col}" stroke-width="{3*s}"/>')
    a(f'<circle cx="{cx}" cy="{cy-28*s}" r="{4*s}" fill="{RED}"/>')
    a(f'<rect x="{cx-20*s}" y="{cy-16*s}" width="{40*s}" height="{30*s}" rx="{8*s}" fill="{col}"/>')
    a(f'<circle cx="{cx-8*s}" cy="{cy-2*s}" r="{4.5*s}" fill="#fff"/><circle cx="{cx+8*s}" cy="{cy-2*s}" r="{4.5*s}" fill="#fff"/>')
    a(f'<circle cx="{cx-8*s}" cy="{cy-2*s}" r="{2*s}" fill="{RED}"/><circle cx="{cx+8*s}" cy="{cy-2*s}" r="{2*s}" fill="{RED}"/>')
    a(f'<rect x="{cx-14*s}" y="{cy+16*s}" width="{28*s}" height="{14*s}" rx="{4*s}" fill="{col}"/>')

def globe(cx, cy, r, col, sw=3):
    a(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="{sw}"/>')
    a(f'<ellipse cx="{cx}" cy="{cy}" rx="{r*0.45}" ry="{r}" fill="none" stroke="{col}" stroke-width="{sw*0.8}"/>')
    a(f'<line x1="{cx-r}" y1="{cy}" x2="{cx+r}" y2="{cy}" stroke="{col}" stroke-width="{sw*0.8}"/>')
    a(f'<path d="M{cx-r*0.86} {cy-r*0.5} H{cx+r*0.86} M{cx-r*0.86} {cy+r*0.5} H{cx+r*0.86}" stroke="{col}" stroke-width="{sw*0.6}"/>')

def brick_wall(x, y, w, h):
    rect(x, y, w, h, "#7c2d12", 8)
    bh = h / 9
    for row in range(9):
        off = 0 if row % 2 == 0 else -w / 4
        bx = x + off
        while bx < x + w:
            x0, x1 = max(bx, x) + 2, min(bx + w / 2, x + w) - 2
            if x1 - x0 > 4:
                col = "#ea580c" if (row + int(bx)) % 3 else "#c2410c"
                a(f'<rect x="{x0:.1f}" y="{y + row*bh + 2:.1f}" width="{x1-x0:.1f}" height="{bh-4:.1f}" rx="2" fill="{col}"/>')
            bx += w / 2

def server(x, y, w, h):
    rect(x, y, w, h, DARK, 12)
    units = 4
    uh = (h - 24) / units
    for i in range(units):
        uy = y + 12 + i * uh
        rect(x + 12, uy + 3, w - 24, uh - 6, "#334155", 6)
        for k in range(3):
            a(f'<rect x="{x + 26 + k*22}" y="{uy + uh/2 - 3}" width="14" height="6" rx="2" fill="#475569"/>')
        a(f'<circle cx="{x + w - 40}" cy="{uy + uh/2}" r="4.5" fill="#22c55e"/>')
        a(f'<circle cx="{x + w - 26}" cy="{uy + uh/2}" r="4.5" fill="{AMBER}"/>')

def hexagon(cx, cy, r, fill, op=1):
    pts = " ".join(f"{cx + r*math.cos(math.radians(60*i+30)):.1f},{cy + r*math.sin(math.radians(60*i+30)):.1f}" for i in range(6))
    a(f'<polygon points="{pts}" fill="{fill}" opacity="{op}"/>')

def mini_icon(kind, cx, cy, col):
    if kind == "terminal":
        a(f'<rect x="{cx-15}" y="{cy-11}" width="30" height="22" rx="4" fill="{col}"/>')
        a(f'<path d="M{cx-9} {cy-4} l5 4 l-5 4" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/>'
          f'<line x1="{cx}" y1="{cy+5}" x2="{cx+8}" y2="{cy+5}" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/>')
    elif kind == "ports":
        for i in range(3):
            for j in range(2):
                a(f'<rect x="{cx-14 + i*10}" y="{cy-9 + j*10}" width="8" height="8" rx="1.5" fill="{col}"/>')
    elif kind == "phone":
        a(f'<path d="M{cx-11} {cy-12} c-3 0 -4 3 -4 5 c0 11 9 20 20 20 c2 0 5 -1 5 -4 l0 -4 l-7 -3 l-3 3 c-4 -2 -7 -5 -9 -9 l3 -3 l-3 -7 z" fill="{col}"/>')
    elif kind == "folder":
        a(f'<path d="M{cx-15} {cy-10} h10 l4 4 h16 v16 h-30 z" fill="{col}"/>')
    elif kind == "factory":
        a(f'<path d="M{cx-15} {cy+11} V{cy-2} l8 -5 v5 l8 -5 v5 l8 -5 V{cy-12} h6 V{cy+11} Z" fill="{col}"/>')
    elif kind == "web":
        globe(cx, cy, 12, col, 2.2)
    elif kind == "mail":
        a(f'<rect x="{cx-15}" y="{cy-10}" width="30" height="20" rx="3" fill="{col}"/>'
          f'<path d="M{cx-15} {cy-9} l15 11 l15 -11" fill="none" stroke="#fff" stroke-width="2"/>')
    elif kind == "db":
        a(f'<ellipse cx="{cx}" cy="{cy-8}" rx="12" ry="4" fill="{col}"/><rect x="{cx-12}" y="{cy-8}" width="24" height="16" fill="{col}"/>'
          f'<ellipse cx="{cx}" cy="{cy+8}" rx="12" ry="4" fill="{col}"/><path d="M{cx-12} {cy} a12 4 0 0 0 24 0" fill="none" stroke="#fff" stroke-width="1.6"/>')

def eye(cx, cy, s=1):
    a(f'<path d="M{cx-34*s} {cy} Q{cx} {cy-28*s} {cx+34*s} {cy} Q{cx} {cy+28*s} {cx-34*s} {cy} Z" fill="#fff" stroke="{BLUE}" stroke-width="{3.5*s}"/>')
    a(f'<circle cx="{cx}" cy="{cy}" r="{12*s}" fill="{BLUE}"/><circle cx="{cx}" cy="{cy}" r="{5*s}" fill="{DARK}"/>'
      f'<circle cx="{cx+4*s}" cy="{cy-4*s}" r="{2.5*s}" fill="#fff"/>')

def gear(cx, cy, r, col):
    for k in range(8):
        ang = math.radians(45 * k)
        a(f'<rect x="{cx - 5}" y="{cy - r - 6}" width="10" height="12" rx="2" fill="{col}" transform="rotate({45*k} {cx} {cy})"/>')
    a(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{col}"/><circle cx="{cx}" cy="{cy}" r="{r*0.42}" fill="#fff"/>')

def big_db(cx, cy, col):
    a(f'<ellipse cx="{cx}" cy="{cy-22}" rx="28" ry="9" fill="{col}"/>')
    a(f'<rect x="{cx-28}" y="{cy-22}" width="56" height="44" fill="{col}"/>')
    a(f'<ellipse cx="{cx}" cy="{cy+22}" rx="28" ry="9" fill="{col}"/>')
    for dy in (-7, 8):
        a(f'<path d="M{cx-28} {cy+dy} a28 9 0 0 0 56 0" fill="none" stroke="#fff" stroke-width="2.5" opacity="0.9"/>')
    a(f'<ellipse cx="{cx}" cy="{cy-22}" rx="28" ry="9" fill="none" stroke="#fff" stroke-width="2" opacity="0.5"/>')

def monitor_chart(cx, cy, col):
    rect(cx - 36, cy - 28, 72, 48, DARK, 6)
    rect(cx - 31, cy - 23, 62, 38, "#f0fdfa", 3)
    for k, hh in enumerate([12, 22, 16, 30]):
        a(f'<rect x="{cx - 24 + k*13}" y="{cy + 11 - hh}" width="9" height="{hh}" rx="1.5" fill="{col}"/>')
    a(f'<rect x="{cx-6}" y="{cy+20}" width="12" height="9" fill="{DARK}"/><rect x="{cx-20}" y="{cy+28}" width="40" height="5" rx="2" fill="{DARK}"/>')

def desktop_pc(cx, cy, s=1.0):
    # monitor
    rect(cx - 70*s, cy - 62*s, 140*s, 92*s, DARK, 10*s)
    rect(cx - 62*s, cy - 54*s, 124*s, 72*s, "#0b1120", 4*s)
    # screen content: mini dashboard
    for k, (hh, col) in enumerate([(22, TEAL), (38, BLUE), (28, PURPLE), (46, ORANGE), (32, TEAL)]):
        a(f'<rect x="{cx - 50*s + k*20*s}" y="{cy + 10*s - hh*s}" width="{13*s}" height="{hh*s}" rx="{2*s}" fill="{col}"/>')
    T(cx - 54*s, cy - 40*s, "kibana", 10*s, 700, "#94a3b8")
    a(f'<rect x="{cx-10*s}" y="{cy+30*s}" width="{20*s}" height="{16*s}" fill="#334155"/>'
      f'<rect x="{cx-40*s}" y="{cy+44*s}" width="{80*s}" height="{8*s}" rx="{3*s}" fill="#334155"/>')
    # tower
    rect(cx + 82*s, cy - 50*s, 40*s, 100*s, "#334155", 8*s)
    a(f'<circle cx="{cx + 102*s}" cy="{cy - 30*s}" r="{5*s}" fill="#22c55e"/>')
    for k in range(3):
        a(f'<rect x="{cx + 90*s}" y="{cy - 10*s + k*12*s}" width="{24*s}" height="{4*s}" rx="2" fill="#475569"/>')
    # keyboard
    a(f'<path d="M{cx-66*s} {cy+60*s} H{cx+66*s} L{cx+74*s} {cy+74*s} H{cx-74*s} Z" fill="#475569"/>')

def padlock(cx, cy, col):
    a(f'<path d="M{cx-9} {cy-2} V{cy-9} a9 9 0 0 1 18 0 V{cy-2}" fill="none" stroke="{col}" stroke-width="4"/>')
    rect(cx - 13, cy - 3, 26, 20, col, 4)
    a(f'<circle cx="{cx}" cy="{cy+6}" r="3" fill="#fff"/>')

def magnifier_globe(cx, cy, col):
    globe(cx - 6, cy - 6, 26, col, 3.5)
    a(f'<circle cx="{cx+14}" cy="{cy+14}" r="16" fill="#fff" stroke="{col}" stroke-width="5"/>')
    a(f'<line x1="{cx+26}" y1="{cy+26}" x2="{cx+40}" y2="{cy+40}" stroke="{col}" stroke-width="8" stroke-linecap="round"/>')

def report_doc(cx, cy, col):
    a(f'<path d="M{cx-34} {cy-44} H{cx+18} L{cx+34} {cy-28} V{cy+44} H{cx-34} Z" fill="#fff" stroke="{col}" stroke-width="4" stroke-linejoin="round"/>')
    a(f'<path d="M{cx+18} {cy-44} V{cy-28} H{cx+34}" fill="none" stroke="{col}" stroke-width="4" stroke-linejoin="round"/>')
    for k in range(4):
        a(f'<line x1="{cx-22}" y1="{cy-20 + k*14}" x2="{cx+(20 if k%2 else 10)}" y2="{cy-20 + k*14}" stroke="#cbd5e1" stroke-width="4" stroke-linecap="round"/>')
    a(f'<circle cx="{cx+28}" cy="{cy+36}" r="17" fill="{col}"/><path d="M{cx+20} {cy+36} l6 6 l11 -12" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>')

# ---------- canvas ----------
a(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
a('<defs>')
for nm, col in [("aI", INK), ("aR", RED), ("aB", BLUE), ("aT", TEAL), ("aP", PURPLE), ("aG", GREEN)]:
    a(f'<marker id="{nm}" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="4" markerHeight="4" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="{col}"/></marker>')
a('<linearGradient id="hdr" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#0f172a"/><stop offset="1" stop-color="#1e3a8a"/></linearGradient>')
a('<linearGradient id="cloud" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fffbeb"/><stop offset="1" stop-color="#fff7ed"/></linearGradient>')
a('<pattern id="dots" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1.2" fill="#cbd5e1" opacity="0.5"/></pattern>')
a('</defs>')
a(f'<rect width="{W}" height="{H}" fill="#f8fafc"/><rect width="{W}" height="{H}" fill="url(#dots)"/>')

# header
a(f'<rect width="{W}" height="104" fill="url(#hdr)"/>')
for i, (hx, hy) in enumerate([(1700, 30), (1740, 52), (1780, 30), (1820, 52), (1860, 30), (1740, 8), (1820, 8), (1780, 74), (1860, 74)]):
    hexagon(hx, hy, 22, AMBER, 0.18 + 0.07 * (i % 3))
hexagon(62, 52, 28, AMBER)
T(62, 61, "T", 24, 800, INK, "middle")
T(108, 50, "How my honeypot works: from attack to report", 32, 700, "#fff")
T(108, 82, "Operation Honeycomb  ·  T-Pot on AWS  ·  about 7,000 attacks caught in 24 hours (23 to 24 November 2026)", 17, 400, "#cbd5e1")

# ---------- 1. Attackers ----------
shadow_card(36, 140, 330, 560, "#fff1f2", "#fecdd3")
badge(66, 170, 1, RED)
T(96, 177, "ATTACKERS", 15, 800, RED, ls=1.5)
globe(200, 300, 92, "#fecdd3", 3)
hacker(200, 300, 1.25)
robot(92, 446, 1.0)
robot(200, 470, 1.0, "#94a3b8")
robot(308, 446, 1.0)
T(201, 540, "Hackers and bots scan the", 17, 600, INK, "middle")
T(201, 563, "whole internet looking for", 17, 600, INK, "middle")
T(201, 586, "weak servers to break into", 17, 600, INK, "middle")
rect(56, 610, 290, 72, "#fff", 12, "#fecdd3", 1.5)
T(72, 638, "Top attacker: 77.239.124.64", 15, 700, INK)
T(72, 662, "2,674 attacks · 10+ countries", 14, 500, MUTED)

# ---------- AWS cloud ----------
CX0, CY0, CX1, CY1 = 420, 132, 1440, 940
cloud = (f'M{CX0+80} {CY1} H{CX1-80} C{CX1-10} {CY1} {CX1+10} {CY1-120} {CX1-30} {CY1-170} '
         f'C{CX1+20} {CY1-260} {CX1-10} {CY0+90} {CX1-110} {CY0+70} '
         f'C{CX1-150} {CY0-10} {CX1-300} {CY0-10} {CX1-360} {CY0+40} '
         f'C{CX1-430} {CY0-20} {CX0+420} {CY0-20} {CX0+360} {CY0+40} '
         f'C{CX0+300} {CY0-10} {CX0+150} {CY0-10} {CX0+110} {CY0+70} '
         f'C{CX0+10} {CY0+90} {CX0-20} {CY1-260} {CX0+30} {CY1-170} '
         f'C{CX0-10} {CY1-120} {CX0+10} {CY1} {CX0+80} {CY1} Z')
a(f'<path d="{cloud}" fill="#0f172a" opacity="0.06" transform="translate(0 6)"/>')
a(f'<path d="{cloud}" fill="url(#cloud)" stroke="{ORANGE}" stroke-width="4"/>')
rect(760, 118, 340, 40, ORANGE, 20)
T(930, 145, "AWS CLOUD  ·  Stockholm (eu-north-1)", 16, 800, "#fff", "middle")

# ---------- 2. Firewall ----------
brick_wall(480, 250, 70, 360)
badge(515, 230, 2, ORANGE)
T(515, 640, "Firewall", 18, 800, INK, "middle")
T(515, 662, "(security group)", 14, 500, MUTED, "middle")
rect(448, 676, 134, 56, "#fff", 10, "#fde68a", 1.5)
T(515, 699, "lets attacks in", 13, 700, RED, "middle")
T(515, 719, "keeps admin locked", 13, 700, BLUE, "middle")

# ---------- 3. Honeypot server ----------
shadow_card(600, 190, 560, 420, "#fff", "#fde68a")
badge(630, 220, 3, ORANGE)
T(660, 227, "HONEYPOT SERVER (T-Pot)", 15, 800, "#b45309", ls=1.3)
T(660, 252, "Fake services pretend to be real and record everything", 15, 500, MUTED)
server(624, 280, 120, 190)
T(684, 498, "EC2 server", 14, 700, INK, "middle")
T(684, 518, "public IP hidden", 13, 500, MUTED, "middle")
tiles = [("terminal", "Fake SSH login", "~3,000", "Cowrie"),
         ("ports", "Any open port", "~2,000", "Honeytrap"),
         ("phone", "Fake phone system", "965", "Sentrypeer"),
         ("folder", "Fake Windows share", "438", "Dionaea"),
         ("factory", "Fake factory controls", "80", "ConPot"),
         ("web", "Fake websites", "50", "Tanner + H0neytr4p")]
tw, th = 184, 96
for i, (ic, lab, cnt, name) in enumerate(tiles):
    r_, c_ = divmod(i, 2)
    x, y = 764 + c_ * (tw + 12), 280 + r_ * (th + 10)
    rect(x, y, tw, th, "#fffbeb", 12, "#fde68a", 1.5)
    mini_icon(ic, x + 30, y + 30, "#d97706")
    T(x + 54, y + 28, cnt, 22, 800, "#b45309" if i < 2 else INK)
    T(x + 54, y + 47, "attacks", 12, 500, MUTED)
    T(x + 14, y + 72, lab, 13.5, 700, INK)
    T(x + 14, y + 88, name, 12, 500, MUTED)

# ---------- 4. Sensors ----------
shadow_card(600, 630, 560, 92, "#eff6ff", "#bfdbfe")
badge(630, 660, 4, BLUE)
eye(700, 676, 0.95)
T(752, 668, "Security camera for the network (Suricata IDS)", 16, 700, INK)
T(752, 694, "Caught 1,445 DoublePulsar exploit attempts and 8 CVEs", 14, 500, MUTED)

# ---------- 5. Data pipeline ----------
shadow_card(480, 760, 900, 150, "#f0fdfa", "#99f6e4")
badge(510, 790, 5, TEAL)
T(540, 797, "DATA PIPELINE (ELK STACK)", 15, 800, TEAL, ls=1.3)
steps = [(640, "Logstash", "sorts and labels", "each log"),
         (930, "Elasticsearch", "stores every", "attack"),
         (1220, "Kibana", "turns data into", "charts")]
for i, (sx, n, l1, l2) in enumerate(steps):
    if i == 0:
        gear(sx - 80, 855, 22, TEAL)
    elif i == 1:
        big_db(sx - 80, 855, TEAL)
    else:
        monitor_chart(sx - 80, 852, TEAL)
    T(sx - 36, 845, n, 18, 800, INK)
    T(sx - 36, 868, l1, 14, 500, MUTED)
    T(sx - 36, 887, l2, 14, 500, MUTED)
    if i < 2:
        arrow(f"M{sx + 110} 855 H{sx + 150}", TEAL, 5, mk="aT")

# ---------- right side ----------
# 6. My PC
shadow_card(1480, 140, 404, 330, "#eff6ff", "#bfdbfe")
badge(1510, 170, 6, BLUE)
T(1540, 177, "MY PC (KALI LINUX)", 15, 800, BLUE, ls=1.5)
desktop_pc(1650, 290, 1.05)
padlock(1830, 254, BLUE)
T(1682, 400, "I log in to manage the server and", 15, 600, INK, "middle")
T(1682, 421, "read the dashboards. Only my IP", 15, 600, INK, "middle")
T(1682, 442, "address is allowed in.", 15, 600, INK, "middle")

# 7. Threat intel
shadow_card(1480, 500, 404, 190, "#f5f3ff", "#ddd6fe")
badge(1510, 530, 7, PURPLE)
T(1540, 537, "THREAT INTEL CHECKS", 15, 800, PURPLE, ls=1.5)
magnifier_globe(1560, 610, PURPLE)
T(1630, 590, "Cisco Talos: is this IP bad?", 15, 600, INK)
T(1630, 616, "CVEdetails: how serious", 15, 600, INK)
T(1630, 637, "is this vulnerability?", 15, 600, INK)
T(1630, 668, "3 IPs and 1 CVE checked", 13, 500, MUTED)

# 8. Report
shadow_card(1480, 720, 404, 220, "#f0fdf4", "#bbf7d0")
badge(1510, 750, 8, GREEN)
T(1540, 757, "THE REPORT", 15, 800, GREEN, ls=1.5)
report_doc(1560, 840, GREEN)
for k, s in enumerate(["Q1. Who are the attackers?", "Q2. What are the common attacks?", "MITRE ATT&amp;CK mapping", "How to defend against them"]):
    a(f'<circle cx="{1624}" cy="{798 + k*30}" r="4.5" fill="{GREEN}"/>')
    T(1634, 803 + k * 30, s, 14, 600, INK)

# ---------- arrows ----------
arrow("M372 420 H470", RED, 7, mk="aR")
T(421, 404, "attacks", 14, 800, RED, "middle")
arrow("M556 330 H594", RED, 6, mk="aR")
arrow("M880 614 V626", BLUE, 4, mk="aB")
arrow("M930 726 V752", TEAL, 5, mk="aT")
# Kibana -> PC (admin, two way)
arrow("M1384 835 H1440 V300 H1474", BLUE, 4, dash="10 8", mk="aB")
a(f'<text x="1462" y="560" font-family="{F}" font-size="13" font-weight="800" fill="{BLUE}" text-anchor="middle" transform="rotate(-90 1462 560)">only my IP</text>')
arrow("M1682 476 V494", PURPLE, 4, mk="aP")
arrow("M1682 696 V714", GREEN, 4, mk="aG")

# ---------- footer key ----------
rect(36, 966, W - 72, 74, "#fff", 16, "#e2e8f0", 1.5)
T(64, 1010, "KEY", 14, 800, INK, ls=1.5)
items = [(RED, "Attack traffic", False, 140), (BLUE, "My admin access (my IP only)", True, 380),
         (TEAL, "Data moving through the pipeline", False, 730), (PURPLE, "Threat intel lookups", False, 1100), (GREEN, "Report", False, 1370)]
for col, lab, dash, x in items:
    ds = ' stroke-dasharray="10 8"' if dash else ""
    a(f'<line x1="{x}" y1="{1004}" x2="{x+44}" y2="{1004}" stroke="{col}" stroke-width="6" stroke-linecap="round"{ds}/>')
    T(x + 56, 1010, lab, 15, 600, INK)
T(W - 64, 1010, "Usman Khalid Jibrin  ·  24 November 2026", 13, 500, "#94a3b8", "end")
a('</svg>')
open("architecture-graphic.svg", "w").write("\n".join(o))
print("ok")
