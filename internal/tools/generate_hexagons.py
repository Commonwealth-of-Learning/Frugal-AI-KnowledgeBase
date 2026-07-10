#!/usr/bin/env python3
"""Generate the Frugal AI hexagon graphics in docs/.gitbook/assets/.

Emits seven SVGs from one geometry so they stay in step:

- frugal-ai-hexagon.svg — the landing-page hexagon: three goals (solid dots,
  top arc), three practices (ring dots, bottom arc), each practice on the axis
  opposite the goal it makes real, hue shared per axis.
- frugal-ai-hexagon-<node>.svg — six variants, one per node: the node is
  emphasised, the rest dim to slate, the node's axis keeps its hue, and the
  legend row is replaced by the node's one-line explanation (for embedding on
  the node's own page, or for slides).

The card background is self-contained (light, bordered) so the figures read
correctly on both GitBook themes. Run after any change to node names,
one-liners, or colours: python3 internal/tools/generate_hexagons.py
"""

from pathlib import Path

OUT_DIR = Path(__file__).resolve().parents[2] / "docs" / ".gitbook" / "assets"

# Cropped to the drawn content; geometry below uses the original 760x560 space.
VIEWBOX = "0 64 760 466"
WIDTH, HEIGHT = 760, 466
CARD = '<rect x="1.5" y="65.5" width="757" height="463" rx="16" fill="#f8fafc" stroke="#d3d9e1" stroke-width="1.5"/>'

NODES = [
    dict(key="frugality", label="Frugality", kind="goal",
         pos=(380, 135), lab=(380, 106, "middle"),
         hue="#059669", dark="#047857",
         one_liner="Capable AI on modest, already-owned hardware, at a predictable cost."),
    dict(key="sovereignty", label="Sovereignty", kind="goal",
         pos=(509.9, 210), lab=(534, 216, "start"),
         hue="#4f46e5", dark="#3730a3",
         one_liner="Data, governance, and the agent loop stay under institutional control."),
    dict(key="openness", label="Openness", kind="goal",
         pos=(250.1, 210), lab=(226, 216, "end"),
         hue="#d97706", dark="#92400e",
         one_liner="Open, inspectable components throughout; every part of the stack can be swapped."),
    dict(key="local-first", label="Local first", kind="practice",
         pos=(380, 435), lab=(380, 470, "middle"),
         hue="#059669", dark="#047857",
         one_liner="Runs on machines the institution owns and keeps working offline."),
    dict(key="teacher-in-the-loop", label="Teacher-in-the-loop", kind="practice",
         pos=(250.1, 360), lab=(226, 366, "end"),
         hue="#4f46e5", dark="#3730a3",
         one_liner="Teachers review, adapt, and approve AI output before it reaches learners."),
    dict(key="capacity-building", label="Capacity building", kind="practice",
         pos=(509.9, 360), lab=(534, 366, "start"),
         hue="#d97706", dark="#92400e",
         one_liner="The local team gains the skills to run, recover, and extend the stack."),
]

AXES = [("frugality", "local-first"), ("sovereignty", "teacher-in-the-loop"),
        ("openness", "capacity-building")]

DIM = "#cbd5e1"
DIM_LABEL = "#94a3b8"
FONT = "system-ui, sans-serif"

# Perimeter order: top, upper-right, lower-right, bottom, lower-left, upper-left.
PERIMETER = ["frugality", "sovereignty", "capacity-building",
             "local-first", "teacher-in-the-loop", "openness"]


def node_by_key(key):
    return next(n for n in NODES if n["key"] == key)


def open_svg(title):
    return (f'<svg width="{WIDTH}" height="{HEIGHT}" viewBox="{VIEWBOX}" '
            f'xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="hex-title">\n'
            f'  <title id="hex-title">{title}</title>\n  {CARD}\n')


def centre_disc():
    return ('  <circle cx="380" cy="285" r="64" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>\n'
            f'  <text x="380" y="281" text-anchor="middle" font-family="{FONT}" '
            'font-size="22" font-weight="700" fill="#0f172a">Frugal AI</text>\n'
            f'  <text x="380" y="305" text-anchor="middle" font-family="{FONT}" '
            'font-size="12.5" letter-spacing="0.5" fill="#64748b">goals &amp; practices</text>\n')


def hexagon_outline(stroke, fill_opacity):
    points = " ".join(f'{node_by_key(k)["pos"][0]},{node_by_key(k)["pos"][1]}'
                      for k in PERIMETER)
    return (f'  <polygon points="{points}" fill="#eef2f7" fill-opacity="{fill_opacity}" '
            f'stroke="{stroke}" stroke-width="2"/>\n')


def axis_line(a, b, stroke, width, opacity):
    na, nb = node_by_key(a), node_by_key(b)
    return (f'  <line x1="{na["pos"][0]}" y1="{na["pos"][1]}" '
            f'x2="{nb["pos"][0]}" y2="{nb["pos"][1]}" '
            f'stroke="{stroke}" stroke-width="{width}" opacity="{opacity}"/>\n')


def dot(n, dim=False, highlight=False):
    x, y = n["pos"]
    parts = []
    if highlight:
        parts.append(f'  <circle cx="{x}" cy="{y}" r="22" fill="none" '
                     f'stroke="{n["hue"]}" stroke-width="4" opacity="0.25"/>\n')
        if n["kind"] == "goal":
            parts.append(f'  <circle cx="{x}" cy="{y}" r="15" fill="{n["hue"]}" '
                         'stroke="#ffffff" stroke-width="3"/>\n')
        else:
            parts.append(f'  <circle cx="{x}" cy="{y}" r="13" fill="#ffffff" '
                         f'stroke="{n["hue"]}" stroke-width="4.5"/>\n')
    elif n["kind"] == "goal":
        fill = DIM if dim else n["hue"]
        parts.append(f'  <circle cx="{x}" cy="{y}" r="12" fill="{fill}" '
                     'stroke="#ffffff" stroke-width="3"/>\n')
    else:
        stroke = DIM if dim else n["hue"]
        parts.append(f'  <circle cx="{x}" cy="{y}" r="10" fill="#ffffff" '
                     f'stroke="{stroke}" stroke-width="3.5"/>\n')
    return "".join(parts)


def label(n, dim=False, highlight=False):
    x, y, anchor = n["lab"]
    if highlight:
        fill, size, weight = n["dark"], "19", "750"
    elif dim:
        fill, size, weight = DIM_LABEL, "17", "600"
    else:
        fill, size, weight = n["dark"], "17", "650"
    return (f'  <text x="{x}" y="{y}" text-anchor="{anchor}" font-family="{FONT}" '
            f'font-size="{size}" font-weight="{weight}" fill="{fill}">{n["label"]}</text>\n')


def render_main():
    parts = [open_svg(
        "The Frugal AI hexagon: three goals (Frugality, Sovereignty, Openness) "
        "and three practices (Local first, Teacher-in-the-loop, Capacity building), "
        "each practice opposite the goal it serves")]
    for a, b in AXES:
        parts.append(axis_line(a, b, node_by_key(a)["hue"], "2", "0.35"))
    parts.append(hexagon_outline("#94a3b8", "0.4"))
    parts.append(centre_disc())
    for n in NODES:
        parts.append(dot(n))
    for n in NODES:
        parts.append(label(n))
    parts.append(
        f'  <g font-family="{FONT}" font-size="12.5" fill="#64748b">\n'
        '    <circle cx="182" cy="508" r="6" fill="#475569"/>\n'
        '    <text x="194" y="512.5" text-anchor="start">Goals — what the system optimises for</text>\n'
        '    <circle cx="450" cy="508" r="6" fill="#ffffff" stroke="#475569" stroke-width="2.5"/>\n'
        '    <text x="462" y="512.5" text-anchor="start">Practices — how the goals are applied</text>\n'
        '  </g>\n')
    parts.append("</svg>\n")
    return "".join(parts)


def render_variant(highlight_key):
    hl = node_by_key(highlight_key)
    parts = [open_svg(
        f'The Frugal AI hexagon with {hl["label"]} highlighted '
        f'({hl["kind"]}): {hl["one_liner"]}')]
    for a, b in AXES:
        if highlight_key in (a, b):
            parts.append(axis_line(a, b, hl["hue"], "2.5", "0.45"))
        else:
            parts.append(axis_line(a, b, "#e2e8f0", "2", "0.9"))
    parts.append(hexagon_outline(DIM, "0.3"))
    parts.append(centre_disc())
    for n in NODES:
        parts.append(dot(n, dim=(n["key"] != highlight_key),
                         highlight=(n["key"] == highlight_key)))
    for n in NODES:
        parts.append(label(n, dim=(n["key"] != highlight_key),
                           highlight=(n["key"] == highlight_key)))
    parts.append(
        f'  <text x="380" y="513" text-anchor="middle" font-family="{FONT}" '
        f'font-size="14.5" fill="#475569">'
        f'<tspan font-weight="700" fill="{hl["dark"]}">{hl["label"]}</tspan>'
        f'<tspan> — {hl["one_liner"]}</tspan></text>\n')
    parts.append("</svg>\n")
    return "".join(parts)


def main():
    out = OUT_DIR / "frugal-ai-hexagon.svg"
    out.write_text(render_main(), encoding="utf-8")
    print(out)
    for node in NODES:
        out = OUT_DIR / f'frugal-ai-hexagon-{node["key"]}.svg'
        out.write_text(render_variant(node["key"]), encoding="utf-8")
        print(out)


if __name__ == "__main__":
    main()
