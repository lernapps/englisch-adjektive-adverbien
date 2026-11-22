---
name: app-content
description: Use for any content work in this app - researching, writing, extending, correcting or reviewing its competencies, chapters, pages, rounds, questions, exercises, figures, terms or sources. This app's own content decisions; they take precedence over the generic lernapps content skills. Load it before you change any content.
---

# Content guide of this app

„Beschreiben und vergleichen: Adjektive und Adverbien“: Explainer (Strang-App `englisch/grammatik`, Format 2, Sprache Deutsch, englische Beispiele). Auftrag: Issue lernapps/apps#476 (Epic lernapps/apps#489, Konventionen dort). Die erste Version baut nur Stufe 5-6 (Kapitel 1 und 2); Kapitel 3 und 4 (Stufe 7-8: Adjektive nach Sinnesverben, Stellung der Adverbien, Gradadverbien, one, substantivierte Adjektive) kommen als Inkremente `increment/<NN>-<name>`.

## Curriculum

Englisch als erste Fremdsprache, Klasse 5-6 (erstes und zweites Lernjahr, Stufe 5-6 der Karte). Kein Lehrplan: Reihenfolge und Bausteine kommen aus der Lernlandkarte `https://lernapps.net/apps/map/englisch.json` (Fokus `competency`; Strang-App des Strangs `grammatik`). Vorwissen: Hello, Millbrook! (#470) und to-be (#472). Nicht hier: Häufigkeitsadverbien (#472), Wörter zum Beschreiben von Personen als Wortschatz (#477), Fragen und Verneinung (#473), Kapitel 3 und 4 (spätere Inkremente).

## Competencies

Alle sechs sind Lücken der Karte, Band 5-6. Eine Seite je Baustein, Ordnung nach `requires`. Von außen braucht die Karte nur `to-be`.

1. Kapitel `beschreiben-und-vergleichen` („Beschreiben und vergleichen“)
   - Wiederholung `recap: englisch/to-be` → `beschreiben-und-vergleichen/das-brauchst-du` (ohne Übung, ohne `competencies`)
   - `adjektive` → `beschreiben-und-vergleichen/adjektive` (Musterseite): „Ich kann Adjektive vor ein Nomen (a big house) und nach „be“ (The house is big.) stellen.“
   - `adjektive-steigern` → `beschreiben-und-vergleichen/adjektive-steigern`: „Ich kann Adjektive steigern, mit -er/-est, mit more/most und unregelmäßig (good – better – best).“
   - `vergleiche` → `beschreiben-und-vergleichen/vergleiche`: „Ich kann mit than, as … as und not as … as vergleichen.“
2. Kapitel `wie-jemand-etwas-tut` („Wie jemand etwas tut“)
   - `adverbien-art-und-weise` → `wie-jemand-etwas-tut/adverbien`: „Ich kann Adverbien der Art und Weise bilden (quick – quickly) und die Sonderformen well, fast und hard verwenden.“
   - `adjektiv-oder-adverb` → `wie-jemand-etwas-tut/adjektiv-oder-adverb`: „Ich kann entscheiden, ob ich ein Adjektiv oder ein Adverb brauche (a careful driver – she drives carefully).“
   - `adverbien-steigern` → `wie-jemand-etwas-tut/adverbien-steigern`: „Ich kann Adverbien steigern und damit Handlungen vergleichen (She runs faster than I do.).“

Die „Ich kann“-Sätze stehen wie in der Karte in `src/<kapitel>/<seite>.yaml` (nicht umformulieren). Übungs-IDs: Präfix = Seite (`adjektive-form`), Diktat `<seite>-hoeren`, Nachsprechen `<seite>-nachsprechen`.

## Content structure

- Pfad: `src/<kapitel>/chapter.yaml`, Seiten `src/<kapitel>/<seite>.yaml`.
- Jede Seite hat dieselben Abschnitts-IDs in dieser Reihenfolge: `einstieg` (Szene der Figuren, erste leichte Aufgabe, „Das kannst du danach“), `neu` (Anhänger- oder Treppenbild, Bau-Karte, Merke-Kasten, Poster-Tabelle), `uebung` (mindestens vier Übungen, leicht → schwer), `anwenden` (`speaking-task` und `open-task`), `weiter` (nächster Schritt in der Ausstellung; am Kapitelende ein Rückblick). Titel sagen, was der Abschnitt tut. Die Wiederholungsseite hat nur Text und Tabelle.
- Länge: höchstens 350 Wörter Text, höchstens 4 Textblöcke hintereinander, Bild oder Übung in den ersten vier Blöcken. Jede Seite bringt einen neuen Schritt (`explainer-one-step`).
- Gebaut: alle sechs Seiten und die Wiederholungsseite, 36 Audiosätze (6 je Seite: 3 Diktat, 3 Nachsprechen, Liste `.agents/skills/app-content/scripts/audio-texte.json`), je Kapitel eine Selbsteinschätzung (`chapter.yaml`, zwei Übungen je Seite). Wiederholung: `das-brauchst-du` (ohne Übung, mit den Tabellen „Die Formen von be“ und „Anhänger und Treppe“).
- Geschichte: Mr Hill lässt die Klasse für den Schulflur die Ausstellung „Our Millbrook“ aufbauen: Fotos und Zeichnungen von Orten, Dingen und Leuten der Stadt. Sophie, Ellie, Peter und Amir beschriften sie mit Anhängern. Kapitel 1 beschreibt und vergleicht Dinge und Leute, Kapitel 2 beschreibt, wie Leute etwas tun. Figuren und Orte wie in #470 (nicht ändern): Sophie (blond, Zöpfe, grüne Jacke, aus Deutschland, wohnt bei den Parkers, 11 bis 12), Ellie Parker (11, roter Pferdeschwanz, rote Jacke), Peter Parker (9, kurze braune Haare, gelbe Jacke), Amir (11, schwarze Locken, Brille, blaue Jacke), Mr Hill (graue Haare, braune Jacke), Mrs Parker. Millbrook School, Schultag ab 8:45. Geburtstage: Peter 5. Mai, Ellie 10. Juli, Amir 12. Oktober, Sophie 14. Oktober. Tabellen heißen „Klassenzimmer-Poster · …“ und „Schulkalender · …“ und wachsen von Seite zu Seite.
- Anrede „du“.

## Terminology

- „Ausdruck“ (fester Ausdruck), nie „Wendung“. Fachbegriffe noun, verb, adjective, adverb, sentence (noun, verb, adjective, sentence gelten ab #470; adverb wird auf der Seite `adverbien` eingeführt).
- Anhänger-Wörter: Adjektiv-Anhänger (blau, hängt am Nomen oder nach be), Adverb-Anhänger (orange, meist -ly, hängt am Verb), Treppe, Stufe (Grundform, Steigerung, Höchststufe), Frage „Ding oder Handlung?“. Immer dieselben.
- Britisches Englisch (favourite, colour). Englische Aufgaben enthalten kein deutsches Wort. Englisches immer mit deutscher Bedeutung, wo ein Wort neu ist.
- Aussprache: keine Lesehilfe und keine Lautschrift hier (IPA gehört zu #482); Hörtexte nur als ganze Sätze.

## Exercise patterns

Aufbau leicht → schwer: wählen/zuordnen → Lücke → schreiben mit Cue → übersetzen/frei. Je Übung `mistakes` mit eigener Meldung und `hint`; gleichwertige Antworten mit `(a|b)`.

- Anhänger anheften: `language-task` mode `choice` (Lücke, `distractors`) und `ordering` (Satzteile, Platz des Anhängers).
- Treppe ordnen und füllen: `ordering`, `matching` (Adjektiv ↔ Stufenregel), `language-task` mode `table` (Grundform, Steigerung, Höchststufe).
- Form bilden: mode `write` mit `cue` (englisch, ohne deutsches Wort).
- Vergleichen: mode `choice` (than, as … as), `write` mit Cue, `true-false` mit Begründung.
- Entscheiden mit Begründung: `single-choice`; die Rückmeldung nennt die Frage („Beschreibt das Wort ein Ding oder eine Handlung?“).
- Korrigieren: mode `write`, ein Fehler im Satz.
- Übersetzen: mode `write` mit `source` und `accepted`.
- Hören und schreiben: `language-task` mit `audio` (Diktat, je Seite höchstens drei ganze Sätze); Nachsprechen: `speaking-task` (drei andere Sätze); Freies Schreiben: `open-task`.
- Typische Fehler (jeweils `mistakes`): a house big; bigs houses; more bigger; interestinger; the most big; gooder; taller then / taller as; as taller as; She runs quick; fastly; hardly statt hard; She sings good; She is carefully; a carefully driver; more fast; carefullier.
- Keine Komponente (`prefer-built-in-block`); eine Ziehen-Übung für Anhänger und Treppe wäre ein Wunsch für ein Inkrement.
- Keine Datendateien: jede Tatsache steht einmal in ihrer Seite.

## Figures

- Eigene Zeichnungen, `CC-BY-4.0`, Quelle „eigene Zeichnung“, `src/images/`. Hintergrund #f4efe2, Schrift mindestens 16 im 480er viewBox, bei 360 px lesbar. Skizzen in `.vibe/sketches/`.
- Familie `anhaenger-<seite>.svg`: Adjektiv-Anhänger blau (#2c6fd8), rund, mit Loch, hängt an einem Karton mit dem Nomen oder nach „is“; Adverb-Anhänger orange (#d35400), mit -ly, hängt an dem Karton mit dem Verb. Treppe `treppe-<seite>.svg`: drei Stufen grün (#138d75): Grundform, Steigerung, Höchststufe; die Adverb-Treppe trägt orange Anhänger.
- Szenen `szene-<seite>.svg`: die Figuren, kopiert als `<g id>` aus `millbrook-klassenzimmer.svg` von #470 (hello-millbrook) und gleich gelassen; keine Fotos, keine Figuren aus Büchern, Filmen oder Marken. `alt` sagt, was die Szene zeigt, nie die Lösung. Die Bildunterschrift nennt, wer wer ist (Sophie Zöpfe, Ellie roter Pferdeschwanz, Amir Brille, Peter gelbe Jacke).
- Gebaut (`src/images/`, erzeugt vom Skript `.agents/skills/app-content/scripts/make_images.py`, das die Kinder aus `millbrook-klassenzimmer.svg` von #470 kopiert): `anhaenger-leer`, `anhaenger-adjektive`, `treppe-adjektive-steigern` (kurz und lang), `vergleiche-diagramm`, `anhaenger-adverbien`, `entscheidung`, `treppe-adverbien-steigern` (orange) und je Seite eine Szene `szene-<seite>.svg` (`szene-adjektive`, `szene-adjektive-steigern`, `szene-vergleiche`, `szene-adverbien`, `szene-adjektiv-oder-adverb`, `szene-adverbien-steigern`). Ein neues Bild: Funktion in `make_images.py` ergänzen und das Skript starten, nie die SVG von Hand ändern.
- Poster und Kalender sind `table`-Blöcke, wachsen von Seite zu Seite: „Klassenzimmer-Poster · Die Formen von be“, „Der Adjektiv-Anhänger“, „Die Treppe der Adjektive“, „Vergleiche“, „Der Adverb-Anhänger“, „Blau oder orange“, „Die Treppe der Adverbien“ und je Seite „Wörter dieser Seite“; „Schulkalender · Rückblick Kapitel 1 und 2“.

## Sources

Karte `https://lernapps.net/apps/map/englisch.json`; Grundwortschatz `https://lernapps.net/apps/map/englisch/grundwortschatz/` (A1/A2, geöffnet 2026-11-21). Wörter der Übungen: Adjektive big, small, tall, short, old, new, fast, slow, quick, quiet, loud, happy, sad, good, bad, easy, difficult, hard, careful, interesting, exciting, expensive, cheap, beautiful, funny, friendly, busy, hot, cold, long, young, strong, clean, nice, clever, warm (A1), heavy, dirty, tidy, polite (A2); Adverbien slowly, quickly, quietly, loudly, carefully, happily, easily, kindly, early, late, well (A1), badly, politely, patiently, safely, calmly, gently, softly, sadly (A2). Außerhalb der Liste, jeweils mit Bedeutung auf der Seite eingeführt: die Steigerungs- und Höchstformen (bigger, taller, easier, better, best, worse, worst, faster, harder, earlier, more … und the most …; Formen von Wörtern der Liste), exhibition (A2, nur im Text), poster, two. Auf der Seite `vergleiche` stehen zusätzlich boring, rabbit, hamster, cake, test (alle in der Liste). Nicht verwendet: bakery, bridge, brave, lazy, neatly, project, duck. Fakten aus Wikipedia (nur Fakten, keine Sätze, CC BY-SA): `Degrees of comparison of adjectives and adverbs` (-er/-est bei einer Silbe, more/most bei drei und mehr, unregelmäßige Formen, than und as … as, Doppelsteigerung als Fehler) und `Adverb` (Adverbien der Art und Weise oft mit -ly, flat adverbs wie fast, Steigerung mit more/most, well – better – best), geöffnet am 2026-11-21. Nicht geprüft: deutsche Wikipedia, Klexikon. Beispielsätze sind eigene aus dem Alltag der Figuren. Audio: KI-Stimme `bf_emma` (britisch, weiblich), mit Skill `lernapps-audio` erzeugt und als KI-generiert markiert. Material der Ersteller:in: keines.

## Hörliste

Hörsätze, die auf ein einsilbiges Wort enden (nach dem Erzeugen hatte die Stimme dort ein leises Ausklingen, `regen_audio.py` schneidet es ab). Die Ersteller:in hört sie gezielt, bevor die App veröffentlicht wird. Kein Hörsatz hängt einen Namen nur wegen des Klangs an; ein Name am Satzende steht nur, wo der Satz ihn braucht (The tallest girl is Ellie, … than Sophie).

| Datei (`src/audio/`) | Satz |
|---|---|
| the-best-bike-is-new.mp3 | The best bike is new. |
| it-is-the-hottest-day.mp3 | It is the hottest day. |
| the-new-table-is-small.mp3 | The new table is small. |
| the-hamster-is-small.mp3 | The hamster is small. |
| the-jacket-is-old.mp3 | The jacket is old. |
| the-trees-are-tall.mp3 | The trees are tall. |
| the-new-house-is-tall.mp3 | The new house is tall. |
| the-garden-is-bigger-than-the-house.mp3 | The garden is bigger than the house. |
| the-pizza-is-not-as-cheap-as-the-cake.mp3 | The pizza is not as cheap as the cake. |
| the-old-house-is-as-big-as-the-new-house.mp3 | The old house is as big as the new house. |
| the-film-is-better-than-the-game.mp3 | The film is better than the game. |
| ellie-is-a-good-friend.mp3 | Ellie is a good friend. |
| peter-is-a-kind-boy.mp3 | Peter is a kind boy. |
| the-teacher-is-nice.mp3 | The teacher is nice. |
| ellie-is-a-nice-girl.mp3 | Ellie is a nice girl. |
| the-teacher-is-kind.mp3 | The teacher is kind. |
| sophie-writes-well.mp3 | Sophie writes well. |

Nach jedem neuen Hörsatz: einsilbiges Ende → hier eintragen.

## Adding a chapter or round

1. Baustein auf der Karte wählen; die Voraussetzungen müssen auf früheren Seiten stehen oder eine Wiederholungsseite bekommen.
2. Seite `src/<kapitel>/<seite>.yaml` mit den Abschnitten `einstieg`, `neu`, `uebung`, `anwenden`, `weiter` anlegen, in `chapter.yaml` eintragen, Competency-ID setzen.
3. Anhänger und Treppe in der Figurenfamilie erweitern (Kapitel 3: Satzkarten aus #473, Anhänger nach look, sound, taste, Regler für Gradadverbien; Kapitel 4: Anhänger ohne Nomen, one, the rich) und das Poster um die Zeilen der Seite.
4. Übungen aus den Mustern oben, je mit `mistakes` und `hint`; 1 bis 3 je Seite in `selfAssessment` (Skill `lernapps-explainer-self-assessment`).
5. Hörtexte: Datei `src/audio/<satz>.mp3` und Eintrag in `.agents/skills/app-content/scripts/audio-texte.json` (Datei → Satz, 6 je Seite: 3 für Diktat, 3 für Nachsprechen), erzeugt mit `regen_audio.py` (Skript aus #470/#472, schneidet das Ausklingen ab); anhören lassen; Sätze nicht zwischen Seiten wiederholen und nicht wörtlich (auch nicht mit getauschtem Namen) in Einstieg, Poster, Merke oder einer Übung derselben Seite; einsilbiges Ende in die Hörliste.
6. Wörter gegen den Grundwortschatz prüfen; `npx --no -- lernapps check`; committen.

## Rules learned from mistakes

Aus #470 und #472 übernommen:
- Jede Übung fragt nur Wörter ab, die vorher auf der Seite stehen.
- Eine Tabelle, die eine Übung beantwortet, steht nicht direkt über ihr; die Antwort einer Frage steht nie im Absatz direkt darüber.
- Englische Aufgaben enthalten kein deutsches Wort; der Cue ist englisch, der deutsche Hinweis steht in `source` oder in der Aufgabe.
- Mit `(a|b)` gleichwertige richtige Antworten zulassen; `case: wrong` nur dort, wo die Seite Großschreibung unterrichtet.
- Audio: das Ausklingen der Stimme am Satzende abschneiden (`regen_audio.py`), keinen Namen nur für den Klang anhängen, Hörlisten-Sätze (einsilbiges Ende) im Inhaltsführer führen; ein Name am Satzende nur, wo der Satz ihn braucht (zweisilbig: Sophie, Peter, Ellie, Amir).
- Bilder: Beschriftungen innerhalb des `viewBox`; `alt` verrät nie die Lösung; die Bildunterschrift nennt, wer wer ist.
- Der Merke-Kasten nennt andere Wörter als die Übungen, sonst schreiben die Kinder nur ab.
- Als Auswahl nur echte Lernerfehler (more bigger, taller then), keine Unwörter.
- Eine Übung für die Selbsteinschätzung nennt in Hinweis und Meldung weder „Spalte“ noch „Poster“ noch „oben“.
Aus dem Checkpoint „Musterseite“ dieser App:
- Fremde Bausteine (has got/have got, Kurzformen) nicht in die Items einer Seite mischen: höchstens eine Erwähnung in der Wörter-Tabelle, die Items nehmen be-Sätze und Nomen mit Adjektiv.
- Als Distraktor im `choice` nur echte Lernerfehler (a house big, The house old, are old), keine Unwörter (news); jeder Distraktor-Satz steht als `mistakes`-Eintrag mit eigener Meldung.
- Die Regel steht einmal im Merke-Kasten; Hinweise der Übungen verweisen auf das Bild, sie wiederholen die Regel nicht.
- Der Pluralcue nennt die Mehrzahl (`trees`), sonst muss das Kind raten; big und tall sind nie beide richtig für dieselbe Aufgabe (hoch für Bäume nur tall).
