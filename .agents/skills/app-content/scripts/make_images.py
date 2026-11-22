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
    b += frame(60, 15, 190, 115, tree(155, 38, .85)) + frame(290, 15, 190, 115, house(385, 62, .85))
    b += text(155, 160, "tree", 26) + text(385, 160, "house", 26)
    b += kid("sophie", 510, 110, .85) + kid("ellie", 40, 165, .7) + kid("amir", 140, 165, .7) + kid("peter", 300, 185, .55)
    return svg(640, 340, "Vier Kinder hängen Karten an die Ausstellung im Flur der Millbrook School", b)

@image
def anhaenger_adjektive():
    b = card(20, 30, 70, 50, "a", 26) + card(100, 30, 130, 50, "house", 26) + tag(95, 80, "big")
    b += card(260, 30, 130, 50, "The house", 24) + card(400, 30, 60, 50, "is", 26) + tag(462, 80, "big")
    b += text(95, 225, "vor dem Nomen", 20) + text(430, 225, "nach is", 20)
    return svg(540, 250, "Ein blauer Anhänger hängt vor dem Nomen und nach is", b)

def stairs(x0, y0, labels, colour=GREEN, w=130, step=40, size=22):
    """Three steps rising to the right; labels are the texts on the steps (empty string = blank step).
    A label of more than 12 characters is split into two lines at its last space."""
    b = ""
    for i, l in enumerate(labels):
        h = 64 + i * step
        b += f'  <rect x="{x0 + i * w}" y="{y0 - h}" width="{w}" height="{h}" fill="{colour}" stroke="{INK}" stroke-width="2"/>\n'
        if l:
            cx = x0 + i * w + w / 2
            if len(l) > 12 and " " in l:
                a, c = l.rsplit(" ", 1)
                b += text(cx, y0 - h + 26, a, size, fill="#fff", weight="bold") + text(cx, y0 - h + 26 + size + 4, c, size, fill="#fff", weight="bold")
            else:
                b += text(cx, y0 - h + 36, l, size, fill="#fff", weight="bold")
    return b

@image
def anhaenger_leer():
    b = tag(90, 20, "blau", BLUE, 34, 20) + text(90, 140, "Adjektiv-Anhänger", 20)
    b += tag(290, 20, "orange", ORANGE, 34, 18) + text(290, 140, "Adverb-Anhänger", 20)
    b += stairs(400, 150, ["", "", ""], w=70, step=30)
    b += text(505, 190, "Treppe", 20)
    return svg(640, 200, "Ein blauer und ein orangefarbener Anhänger und eine leere Treppe mit drei Stufen", b)

@image
def szene_adjektive_steigern():
    b = wall()
    # height chart on the wall
    b += '  <rect x="300" y="20" width="26" height="240" fill="#fff" stroke="#7a5a35" stroke-width="3"/>\n'
    for i in range(1, 6): b += f'  <line x1="300" y1="{20 + i * 40}" x2="326" y2="{20 + i * 40}" stroke="#7a5a35" stroke-width="2"/>\n'
    b += kid("ellie", 190, 90, .85) + kid("peter", 350, 150, .7)
    b += kid("sophie", 30, 110, .85) + kid("amir", 470, 110, .85)
    return svg(640, 340, "Ellie und Peter stehen neben der Messlatte an der Wand, Sophie und Amir schauen zu", b)

@image
def treppe_adjektive_steigern():
    b = text(320, 30, "kurzes Wort", 26)
    b += stairs(80, 190, ["tall", "taller", "the tallest"], w=160, step=30)
    b += text(320, 242, "langes Wort", 26)
    b += stairs(5, 400, ["interesting", "more interesting", "the most interesting"], w=210, step=30)
    return svg(640, 420, "Zwei Treppen mit drei Stufen: tall, taller, the tallest und interesting, more interesting, the most interesting", b)

@image
def szene_vergleiche():
    b = wall()
    b += frame(70, 15, 230, 150, house(185, 70, 1.25, "#e8c9a0")) + frame(340, 15, 230, 150, house(455, 95, .7, "#b9d3e8"))
    b += text(185, 195, "old house", 24) + text(455, 195, "new house", 24)
    b += kid("sophie", 30, 185, .65) + kid("amir", 290, 195, .6) + kid("ellie", 540, 185, .65)
    return svg(640, 340, "Drei Kinder stehen vor zwei Fotos: ein großes altes Haus und ein kleines neues Haus", b)

@image
def vergleiche_diagramm():
    b = house(80, 70, 1.0, "#e8c9a0") + house(330, 90, .6, "#b9d3e8")
    b += f'  <line x1="150" y1="70" x2="270" y2="70" stroke="{INK}" stroke-width="2"/>\n'
    b += text(210, 55, "bigger than", 22)
    b += house(80, 250, .75, "#e8c9a0") + house(330, 250, .75, "#b9d3e8")
    b += f'  <line x1="150" y1="260" x2="270" y2="260" stroke="{INK}" stroke-width="2" stroke-dasharray="6 4"/>\n'
    b += text(210, 245, "as big as", 22)
    b += text(455, 120, "Unterschied: than", 20, "start") + text(455, 290, "gleich: as … as", 20, "start")
    return svg(640, 330, "Oben ein großes Haus und ein kleines Haus mit bigger than, unten zwei gleich große Häuser mit as big as", b)

@image
def szene_adverbien():
    b = wall()
    # easel with a drawing for Amir, a running line for Peter
    b += '  <g stroke="#333" stroke-width="3"><line x1="120" y1="262" x2="150" y2="120"/><line x1="220" y1="262" x2="190" y2="120"/><rect x="110" y="40" width="120" height="90" fill="#fff"/></g>\n'
    b += '  <path d="M130 100 Q150 50 170 90 T210 80" fill="none" stroke="#2c6fd8" stroke-width="4"/>\n'
    b += kid("amir", 235, 120, .85) + kid("sophie", 20, 110, .85) + kid("ellie", 480, 110, .85)
    b += kid("peter", 410, 150, .7)
    for i, y in enumerate((200, 225, 250)):
        b += f'  <line x1="{345 - i * 6}" y1="{y}" x2="{385 - i * 6}" y2="{y}" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>\n'
    return svg(640, 340, "Amir malt vorsichtig an einer Staffelei, Peter rennt vorbei, Sophie und Ellie schauen zu", b)

@image
def anhaenger_adverbien():
    b = card(10, 30, 90, 50, "Peter", 24) + card(110, 30, 90, 50, "runs", 24) + tag(155, 80, "quickly", ORANGE, 40, 17)
    b += card(250, 30, 90, 50, "Peter", 24) + card(350, 30, 90, 50, "runs", 24) + tag(395, 80, "fast", ORANGE, 40, 20)
    b += card(470, 30, 70, 50, "He", 24) + card(550, 30, 100, 50, "sings", 24) + tag(600, 80, "well", ORANGE, 40, 20)
    b += text(155, 205, "quick + ly", 20) + text(395, 205, "bleibt gleich", 20) + text(580, 205, "good wird well", 20)
    return svg(680, 230, "Drei Kartenpaare mit orangefarbenem Anhänger am Verb: runs quickly, runs fast und sings well", b)

@image
def szene_adjektiv_oder_adverb():
    b = wall()
    b += card(70, 15, 200, 70, "", 22) + tag(170, 85, "", BLUE, 24, 18)
    b += card(370, 15, 200, 70, "", 22) + tag(470, 85, "", ORANGE, 24, 18)
    b += kid("sophie", 40, 175, .65) + kid("ellie", 190, 175, .65) + kid("amir", 400, 175, .65) + kid("peter", 540, 190, .5)
    return svg(640, 340, "Zwei leere Karten an der Wand, an der linken hängt ein blauer, an der rechten ein orangefarbener Anhänger, davor stehen vier Kinder", b)

@image
def entscheidung():
    b = text(160, 30, "Ding oder Person?", 22) + text(480, 30, "Handlung?", 22)
    b += card(60, 55, 80, 50, "a", 24) + card(150, 55, 100, 50, "boy", 24) + tag(145, 105, "", BLUE, 30, 18)
    b += card(380, 55, 100, 50, "Amir", 24) + card(490, 55, 110, 50, "draws", 24) + tag(545, 105, "", ORANGE, 30, 18)
    b += text(160, 215, "blauer Anhänger", 22) + text(480, 215, "orangefarbener Anhänger", 22)
    return svg(640, 240, "Links ein blauer Anhänger an einem Nomen für ein Ding oder eine Person, rechts ein orangefarbener Anhänger an einem Verb für eine Handlung", b)

@image
def szene_adverbien_steigern():
    b = wall()
    b += '  <rect x="20" y="238" width="600" height="8" fill="#fff" opacity=".7"/>\n'
    b += kid("peter", 330, 150, .7) + kid("amir", 150, 120, .85) + kid("ellie", 480, 120, .85) + kid("sophie", 570, 150, .6)
    for i, y in enumerate((200, 220, 240)):
        b += f'  <line x1="{285 - i * 8}" y1="{y}" x2="{325 - i * 8}" y2="{y}" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>\n'
    for i, y in enumerate((200, 225)):
        b += f'  <line x1="{110 - i * 8}" y1="{y}" x2="{135 - i * 8}" y2="{y}" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>\n'
    return svg(640, 340, "Peter rennt vor Amir her, Ellie und Sophie schauen zu", b)

@image
def treppe_adverbien_steigern():
    b = text(320, 30, "kurzes Adverb", 26)
    b += stairs(80, 190, ["fast", "faster", "the fastest"], w=160, step=30, colour=ORANGE)
    b += text(320, 242, "langes Adverb mit -ly", 26)
    b += stairs(5, 400, ["carefully", "more carefully", "the most carefully"], w=210, step=30, colour=ORANGE)
    return svg(640, 420, "Zwei Treppen mit drei Stufen: fast, faster, the fastest und carefully, more carefully, the most carefully", b)

@image
def szene_sinnesverben():
    b = wall()
    b += '  <rect x="220" y="170" width="200" height="14" fill="#7a5a35"/>\n'
    b += '  <g stroke="#333" stroke-width="3"><path d="M250 120 h140 v50 h-140 z" fill="#c0392b"/><rect x="240" y="110" width="160" height="12" rx="6" fill="#999"/></g>\n'
    b += '  <path d="M290 95 q-10 -20 0 -40 M320 95 q-10 -20 0 -40 M350 95 q-10 -20 0 -40" fill="none" stroke="#bbb" stroke-width="5" stroke-linecap="round"/>\n'
    b += kid("sophie", 400, 120, .8) + kid("ellie", 40, 120, .8) + kid("amir", 130, 120, .8) + kid("peter", 520, 150, .65)
    return svg(640, 340, "Vier Kinder stehen um einen Topf mit dampfender Suppe in der Schulküche", b)

@image
def anhaenger_sinnesverben():
    b = card(10, 40, 130, 50, "The soup", 24) + card(150, 40, 110, 50, "tastes", 24) + tag(205, 90, "sweet", BLUE, 40, 20)
    b += f'  <path d="M180 190 C150 215 90 215 75 95" fill="none" stroke="{BLUE}" stroke-width="3" stroke-dasharray="7 5"/>\n'
    b += card(330, 40, 90, 50, "She", 24) + card(430, 40, 110, 50, "looks", 24) + tag(485, 90, "tired", BLUE, 40, 20)
    b += f'  <path d="M440 190 C410 215 380 215 365 95" fill="none" stroke="{BLUE}" stroke-width="3" stroke-dasharray="7 5"/>\n'
    b += text(205, 245, "wie ist die Suppe?", 20) + text(485, 245, "wie ist sie?", 20) + text(280, 25, "blau = Adjektiv, Bogen = gehört zum Subjekt", 18)
    return svg(560, 270, "Zwei Kartenpaare, an jedem hängt ein blauer Anhänger nach dem Verb, der zum Subjekt zurückzeigt", b)

if __name__ == "__main__":
    names = sys.argv[1:] or list(IMAGES)
    for n in names:
        open(OUT + n + ".svg", "w", encoding="utf-8").write(IMAGES[n]())
        print("wrote", OUT + n + ".svg")
