# Draws the figures of this app (scenes with the four children, tags, stairs) into src/images/.
# Run from the app folder: python3 .agents/skills/app-content/scripts/make_images.py [name ...]
# The children are the <g id> of millbrook-klassenzimmer.svg of hello-millbrook (#470), copied unchanged.
import re, sys, os, urllib.request
SRC = "https://raw.githubusercontent.com/lernapps/hello-millbrook/main/src/images/millbrook-klassenzimmer.svg"
CACHE = "/tmp/millbrook-klassenzimmer.svg"
if not os.path.exists(CACHE):
    open(CACHE, "wb").write(urllib.request.urlopen(SRC).read())
DEFS = re.search(r"<defs>.*?</defs>", open(CACHE, encoding="utf-8").read(), re.S).group(0)
BG = "#f4efe2"; BLUE = "#2c6fd8"; ORANGE = "#d35400"; GREEN = "#138d75"; INK = "#333"
OUT = "src/images/"

def svg(w, h, title, body, desc=None):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img">\n  <title>{title}</title>\n  {DEFS}\n'
            f'  <rect width="{w}" height="{h}" fill="{BG}"/>\n{body}\n</svg>\n')

def kid(name, x, y, s=0.85): return f'  <use href="#{name}" transform="translate({x},{y}) scale({s})"/>\n'
def text(x, y, t, size=24, anchor="middle", fill=INK, weight="normal"):
    return f'  <text x="{x}" y="{y}" text-anchor="{anchor}" font-family="sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}">{t}</text>\n'
def wall(): return f'  <rect y="262" width="640" height="78" fill="#c9a77a"/>\n  <rect width="640" height="262" fill="#efe7d3"/>\n'
def frame(x, y, w, h, inner=""):
    return f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="#fff" stroke="#7a5a35" stroke-width="6"/>\n{inner}'
def card(x, y, w, h, t, size=24, fill="#fff"):
    return (f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="{INK}" stroke-width="2"/>\n'
            + text(x + w / 2, y + h / 2 + size / 3, t, size))
def tag(x, y, t, colour=BLUE, r=30, size=22):
    """A round tag on a string hanging from (x, y)."""
    return (f'  <line x1="{x}" y1="{y}" x2="{x}" y2="{y+22}" stroke="{INK}" stroke-width="2"/>\n'
            f'  <circle cx="{x}" cy="{y+22+r}" r="{r}" fill="{colour}" stroke="{INK}" stroke-width="2"/>\n'
            f'  <circle cx="{x}" cy="{y+28}" r="3" fill="{BG}"/>\n'
            + text(x, y + 22 + r + size / 3, t, size, fill="#fff", weight="bold"))
def tree(x, y, s=1.0):
    return (f'  <g transform="translate({x},{y}) scale({s})" stroke="{INK}" stroke-width="2"><rect x="-8" y="30" width="16" height="50" fill="#8a5a2b"/>'
            f'<circle cx="0" cy="10" r="38" fill="#3a9a5b"/></g>\n')
def house(x, y, s=1.0, col="#e8c9a0"):
    return (f'  <g transform="translate({x},{y}) scale({s})" stroke="{INK}" stroke-width="2"><rect x="-45" y="0" width="90" height="60" fill="{col}"/>'
            f'<path d="M-55 0 L0 -40 L55 0 Z" fill="#b5501e"/><rect x="-10" y="25" width="20" height="35" fill="#7a5a35"/></g>\n')

IMAGES = {}
def image(f):
    IMAGES[f.__name__.replace("_", "-")] = f; return f

@image
def szene_adjektive():
    b = wall()
    b += frame(60, 20, 190, 140, tree(155, 55, 1.1)) + frame(290, 20, 190, 140, house(385, 75, 1.0))
    b += text(155, 152, "tree", 22) + text(385, 152, "house", 22)
    b += kid("sophie", 500, 100, .85) + kid("ellie", 40, 150, .75) + kid("amir", 140, 150, .75) + kid("peter", 300, 180, .6)
    return svg(640, 340, "Vier Kinder hängen Karten an die Ausstellung im Flur der Millbrook School", b)

@image
def anhaenger_adjektive():
    b = card(20, 30, 70, 50, "a", 26) + card(100, 30, 130, 50, "house", 26) + tag(95, 80, "big")
    b += card(260, 30, 130, 50, "The house", 24) + card(400, 30, 60, 50, "is", 26) + tag(500, 55, "big")
    b += text(95, 225, "vor dem Nomen", 20) + text(450, 225, "nach is", 20)
    return svg(540, 250, "Ein blauer Anhänger hängt vor dem Nomen und nach is", b)

def stairs(x0, y0, labels, colour=GREEN, w=130, step=40):
    """Three steps rising to the right; labels are the texts on the steps (empty string = blank step)."""
    b = ""
    for i, l in enumerate(labels):
        h = 50 + i * step
        b += f'  <rect x="{x0 + i * w}" y="{y0 - h}" width="{w}" height="{h}" fill="{colour}" stroke="{INK}" stroke-width="2"/>\n'
        if l: b += text(x0 + i * w + w / 2, y0 - h + 34, l, 22, fill="#fff", weight="bold")
    return b

@image
def anhaenger_leer():
    b = tag(90, 20, "blau", BLUE, 34, 20) + text(90, 140, "Adjektiv-Anhänger", 20)
    b += tag(290, 20, "orange", ORANGE, 34, 18) + text(290, 140, "Adverb-Anhänger", 20)
    b += stairs(400, 150, ["", "", ""], w=70, step=30)
    b += text(505, 190, "Treppe", 20)
    return svg(640, 200, "Ein blauer und ein oranger Anhänger und eine leere Treppe mit drei Stufen", b)

if __name__ == "__main__":
    names = sys.argv[1:] or list(IMAGES)
    for n in names:
        open(OUT + n + ".svg", "w", encoding="utf-8").write(IMAGES[n]())
        print("wrote", OUT + n + ".svg")
