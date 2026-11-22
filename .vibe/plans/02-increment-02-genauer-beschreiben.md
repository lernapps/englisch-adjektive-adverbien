---
# Read by the hooks, the review, the evals. Schema: @lernapps/tooling/guidance/plan-front-matter.v1.schema.json
# Written by `lernapps plan` and the hooks. Never change a key or a value by hand.
# Archetype, as in the app's first plan. Allowed values: explainer, interactive, quiz.
archetype: explainer
# Current phase. Allowed values: explore, plan, code, commit.
phase: code
# prePushFailures: failed pre-push runs of this increment, written by the hook.
prePushFailures: 0
# failedChecks: failed rules and runs, written by lernapps check and the hooks.
failedChecks: { checks-pass: 1 }
---

# Increment: increment-02-genauer-beschreiben

<!--
For you, the assistant. One increment of a published app: new competencies, chapters, pages, rounds, questions, or a
correction. The process is in AGENTS.md; this plan holds the method.
- `npx --no -- lernapps plan next` prints the task to do now, `plan done` ticks it and prints the next one.
- You write only below Goal, Key decisions, Notes, Answers, Content method and Retrospective, in the creator's
  language. Delete the comment of a section once the section is filled.
- The first version's decisions stand: archetype, content method, content guide. Never change an earlier plan.
- Work on the branch `increment/<NN>-<short name>`. Until Commit everything is local: push nothing.
-->

*Started 2026-11-22. Explore, Plan, Code, Commit.*

## Goal

Lernende der Klassen 7-8 beschreiben genauer: Sie setzen nach look, sound, feel und taste ein Adjektiv, stellen Adverbien an die richtige Stelle, stufen mit Gradadverbien ab, ersetzen ein Nomen mit one und ones und nennen Gruppen von Menschen mit dem Adjektiv allein (the rich). Der Inkrement baut die Kapitel 3 „Genauer beschreiben“ und 4 „Adjektive ohne Nomen“ (Issue #476, Stufe 7-8) mit je einem Lesestück als Kern der Seite.

## Key decisions

- Kapitel und Seiten (Vorgabe Issue #476 und Konventionen Abschnitt 8): Kapitel 3 `genauer-beschreiben` mit Wiederholung (`englisch/wortstellung`), `sinnesverben`, `adverbien-stellung`, `gradadverbien`; Kapitel 4 `adjektive-ohne-nomen` mit Wiederholung (`englisch/artikel`), `one`, `substantivierte-adjektive`. Die Wiederholungsseiten stehen am Kapitelanfang, weil `wortstellung` und `artikel` nicht in dieser App geübt werden.
- Form: Sophie ist 13 bis 14, sie bleibt in England; Chat-Verläufe, Blog- und Tagebucheinträge, ein Interview, ein kurzer Zeitungsartikel; ein Bild nur wo es etwas zeigt (Konventionen §2 und §8). Die Anhänger und die Treppe aus Stufe 5-6 kehren als Zeichen wieder (blau, orange, Treppe; neu: Regler für Gradadverbien, ein Anhänger ohne Nomen).
- Lesestücke sind eigene Texte der Figuren, 150 bis 300 Wörter, nach Fakten aus geöffneten Quellen; keine fremden Sätze (Konventionen §8). Keine VOA-, Wikinews- oder African-Storybook-Texte: Das Thema ist Grammatik an eigenen Alltagstexten (guess).
- Szenen: Die Ausstellung „Our Millbrook“ ist vorbei; neue Szenen aus dem Schuljahr (Schul-Radio, Kochclub, Wohltätigkeits-Basar, Schulzeitung). Neue Orte und Personen nur, wo ein Text sie braucht, und dann mit Eintrag in `konventionen.md` (guess).
- Aufbau jeder Seite: Vorwissen-Frage, Lesestück in Abschnitten mit Randglossar, Aufgaben in drei Stufen (Verstehen, Belegen mit Zeile, Meinung), danach die Grammatik-Übungen und ein Schreib- oder Sprechauftrag, höchstens etwa 25 Items (Konventionen §8).
- Audio: `bf_emma`, nur kurze Abschnitte des Lesestücks und Diktat und Nachsprechen als ganze Sätze; Hörliste im Inhaltsführer; nichts Ungehörtes als „geprüft“ ausgeben.

## Notes

- Strang `englisch/grammatik`, Band 7-8, alle fünf Bausteine Lücken der Karte (`practisedBy` leer), Karte geöffnet 2026-11-22.
- Kapitel 3 · Genauer beschreiben (Ich kann nach Sinnesverben das Adjektiv setzen, Adverbien an die richtige Stelle im Satz stellen und mit Gradadverbien abstufen):
  - `adjektive-nach-sinnesverben` (Schritt 1): „Ich kann nach Verben wie look, sound, feel und taste ein Adjektiv verwenden (It tastes good.).“ Braucht `adjektiv-oder-adverb` (Kapitel 2 dieser App).
  - `adverbien-stellung` (Schritt 1): „Ich kann Adverbien an die richtige Stelle im Satz setzen, zum Beispiel nach dem ersten Hilfsverb.“ Braucht `adverbien-art-und-weise` (Kapitel 2) und `wortstellung` (Stufe 5-6, #473: „Ich kann Aussagesätze in der Reihenfolge Subjekt – Verb – Objekt bilden und Ortsangaben vor Zeitangaben stellen.“): Wiederholungsseite `das-brauchst-du` am Anfang von Kapitel 3, `recap: englisch/wortstellung`.
  - `gradadverbien` (Schritt 1): „Ich kann Adjektive und Adverbien mit Wörtern wie very, quite, rather, extremely und too genauer abstufen.“ Braucht `adverbien-art-und-weise`.
- Kapitel 4 · Adjektive ohne Nomen (Ich kann mit one ein Nomen ersetzen (the red one) und Adjektive wie the rich für eine Gruppe von Menschen verwenden):
  - `stuetzwort-one` (Schritt 1): „Ich kann mit one und ones ein Nomen ersetzen, um Wiederholungen zu vermeiden (the red one).“ Braucht `adjektive` (Kapitel 1).
  - `substantivierte-adjektive` (Schritt 1): „Ich kann Adjektive als Nomen für Gruppen von Menschen verwenden (the rich, the elderly).“ Braucht `adjektive` und `artikel` (Stufe 5-6: „Ich kann die Artikel a, an und the richtig verwenden und „the“ vor Vokalen richtig aussprechen.“): Wiederholungsseite am Anfang von Kapitel 4, `recap: englisch/artikel`.
- Sprachlich kein Fehler der Karte; Hinweis: Die Karte führt `wortstellung` und `artikel` auf Stufe 5-6 (Explainer #473 bzw. #470 und #475 üben sie); die Wiederholungsseiten verweisen auf die Karte.
- Didaktik je Baustein: `sinnesverben`: Der Adjektiv-Anhänger geht nach look, sound, feel, taste zum Subjekt wie nach be; die Frage „Ding oder Handlung?“ wird zu „Beschreibt es, wie das Subjekt ist (blau), oder was jemand tut (orange)?“ (She looks tired. – She looks at me carefully.). `adverbien-stellung`: Satzkarten (S – V – O aus der Wortstellung) legen und den orangefarbenen Anhänger an Anfang, Mitte (vor dem Verb, nach dem ersten Hilfsverb) oder Ende hängen; nie zwischen Verb und Objekt (He ate quickly his lunch ist falsch). `gradadverbien`: Ein Regler von not bis extremely (quite, rather, very, extremely), too als Warnzeichen (too cold = zu kalt); Gradadverbien stehen vor dem Adjektiv oder Adverb, nicht vor Verben (nicht: I very like it). `one`: Der Anhänger bleibt hängen, wenn das Nomen weggeht (the red one, the red ones); nach a steht one (a red one), nicht nach „my/this“ allein ohne Adjektiv (this one geht). `substantivierte-adjektive`: the + Adjektiv allein meint alle Menschen dieser Art und steht im Plural (The rich are …), nicht -s anhängen, kein a davor.
- Scope: drin die fünf Bausteine (look, sound, feel, taste, seem und smell mit Adjektiv; Stellung am Anfang, in der Mitte und am Ende; very, quite, rather, extremely, too; one und ones; the rich, the poor, the elderly, the young), je Seite ein Lesestück. Draußen: Adjektivreihenfolge, enough, so … that, Steigerung mit Gradadverbien (much better), Zahlwort one, Possessivpronomen mit one, substantivierte Adjektive für Nationalitäten und Abstraktes (the unknown), Satzadverbien (fortunately). Datenumfang: höchstens etwa 25 Items je Seite, 150 bis 300 Wörter je Lesestück.
- Typische Fehler (je eine eigene Meldung): It tastes well; She looks happily; I feel badly (aber I feel bad); He very quickly ate … ist korrekt, He ate quickly his lunch / He ate his lunch very-quickly falsch; I very like pizza; It is too good = zu gut (Missverständnis mit very); the red (ohne one), a red ones, the rich is …, the riches, a rich.
- Quellen (nur Fakten, 2026-11-22 geöffnet): Wikipedia „Copula (linguistics)“ (look, sound, feel, taste verbinden das Subjekt mit einem Adjektiv und fügen Bedeutung hinzu), „Intensifier“ (very, quite, rather, extremely, too als Verstärker und Abschwächer vor Adjektiven und Adverbien), „Adverb“ (Stellung und Funktion), „One (pronoun)“ (Stützwort, one und ones ersetzen ein Nomen) und „Nominalized adjective“ (the poor, the rich als Gruppenbezeichnung mit Plural). Nicht geprüft: deutsche Wikipedia, Klexikon, Simple English Wikipedia. Alle Lesestücke sind eigene Texte der Figuren; Material der Ersteller:in: keines.
- Wörter: Grundwortschatz A1/A2 plus B1-Wörter, wo das Lesestück sie braucht (Randglossar, Inhaltsführer listet sie).

## Explore

<!--
- All content questions belong here; Plan maps the answers onto the app. Ask; write no code.
- Skip what earlier answers or the app already tell. At most 2 questions per message, one topic each.
-->

### Tasks

- [x] Read the README of the archetype's template (its path is in skill `lernapps-app`): what the app can do now.
      Tell the creator what is new, if it matters for this increment.
- [x] Load the content guide `.agents/skills/app-content/SKILL.md` and read the earlier plans in `.vibe/plans/`: what
      the app teaches, how its content is made, what is open.
- [x] Interview, one topic per question, the creator's words under "Answers": which competencies, chapters or rounds,
      for which school years; hurdles and examples; the amount; any change of look and feel or of terms. No answer:
      ask once more, then write your assumption with "(guess)".
- [x] Load skill `lernapps-content-research`. Research what the content guide does not cover. Write under "Notes":
      the new competencies by chapter with their ids, the sources you opened.
- [x] Write under "Notes" the didactic approach per competency and the scope (in, out, data range).
- [x] The increment needs a kind of content the guide does not cover (a new page structure, screen, component or kind
      of exercise): load skills `lernapps-explainer-design` and `lernapps-exercise-patterns`. Else skip this task.
- [x] **Checkpoint:** research. Show in plain words: the new competencies by chapter, the didactic approach, the
      scope, every "(guess)", the sources and what is unchecked. Stop and wait. Changes: change them, then ask again.
      Creator: Ja, Plan so fortsetzen (zwei Kapitel, fünf Seiten, Lesestück je Seite, Regler für Gradadverbien). Neue Nebenfiguren nur nach Rückfrage. Push des Inkrement-Branches erst nach Erlaubnis, bis dahin lokal.

### Answers

- Aus dem Auftrag der Orchestrator-Session vom 2026-11-22 (Mensch: keine Antwort): Kapitel 3 und 4 als Inkrement in dasselbe Repository, Konventionen Abschnitt 8, `lernapps update`, Branch `increment/02-genauer-beschreiben`, Regeln aus Abschnitt 7, Vorschau-Pull-Request offen, nichts nach `main`, kein Katalogeintrag.
- Look, Begriffe, Sprache, Zielgruppe: wie die erste Version (Inhaltsführer); Alter der Figuren 13 bis 14.

## Plan

<!--
- Map the new content onto the app with the guide's patterns. The creator confirms the plan in one read.
- After the yes you work on your own.
-->

### Tasks

- [x] Load skill `lernapps-content-growth`. Add the tasks of Code as slices, one per competency, in the guide's
      order, one call each: `npx --no -- lernapps plan add --at slices "<task>"`. Say in each which sub-agent may
      write it in parallel, if any.
- [x] Write "Content method": the guide's patterns, figures and components per slice. Anything new: map it as skill
      `lernapps-explainer-design` says, and say why the guide's patterns do not fit.
- [x] Draw a sketch of each new component or interactive exercise, in `.vibe/sketches/`.
- [x] Show the creator, short: goal, new competencies by chapter, slices; in plain words what learners see and do and
      what is new. At most 2 questions.
- [x] **Checkpoint:** confirm the plan and the content method. Stop and wait for an explicit yes. Changes: change
      them, then ask again.
      Creator: Ja, so bauen. Zuschnitt und Lesestück-Muster passen. Musterseite sinnesverben mit Lerner-Check und Sprachprüfung. Push erst nach Erlaubnis der Ersteller:in.

### Content method

Die Muster der ersten Version gelten weiter (Inhaltsführer: Anhänger blau und orange, Treppe, `language-task` in den Modi `choice`, `write`, `table`, `gap`, Diktat `language-task` mit `audio`, `speaking-task`, `open-task`; Wörter aus A1/A2). Neu für die Stufe 7-8 ist **das Lesestück als Kern der Seite**. Warum die Muster der ersten Version nicht reichen: Dort erklärt kurzer Text mit Szenenbild; ab Stufe 7-8 lernen die Kinder an einem zusammenhängenden Text (Konventionen §8).

Neues Muster „Lesestück“ (kommt in der Slice 1 in den Inhaltsführer, mit Beispiel):
- Abschnitte der Seite in dieser Reihenfolge: `vorwissen` (eine `single-choice` zu etwas, das die Kinder schon können), `lesen` (das Lesestück: 2 bis 3 `text`-Blöcke je Abschnitt des Lesestücks, nach jedem Abschnitt eine `table` „Randglossar“ mit den schweren Wörtern), `verstehen` (drei Stufen: Verstehen mit `single-choice` oder `true-false`; Belegen mit einer `single-choice`, deren Optionen Zeilen des Textes mit Zeilenangabe sind; Meinung als `open-task` am Ende der Seite), `neu` (die Regel, aus dem Text abgeleitet: „Schau in den Text“, Bild, Poster-Tabelle, Merke), `uebung` (Grammatik-Übungen, leicht → schwer), `anwenden` (`speaking-task`, `open-task`), `weiter`.
- Lesestück: 150 bis 300 Wörter, eigener Text nach Fakten der geöffneten Quellen, Sorten: Chat (Sophie, Ellie, Amir, Peter), Blog- und Tagebucheintrag, Interview, kurzer Zeitungsartikel. Chat-Zeilen als `text` mit fettem Namen, jede Zeile eine Nummer (Zeilenangabe). Höchstens ein Lesestück je Seite, höchstens etwa 25 Items. Die Länge des Lesestücks zählt nicht zu den 350 Wörtern Erklärtext (der Check meldet es als Hinweis).
- Hörtext: nur kurze Abschnitte als Hörsätze (Diktat und Nachsprechen, ganze Sätze), `bf_emma`, Hörliste im Inhaltsführer; keine Sätze des Lesestücks, die in einer Übung derselben Seite wörtlich stehen.
- Keine Lösung im Text darüber: Poster, Merke und Bild nennen andere Beispiele als die Übungen; Distraktoren sind echte Lernerfehler; je Fehler eine eigene Meldung (Modus `choice` zeigt `mistakes` nicht: dort Fehler im Modus `write` fragen); `punctuation: ok`.

Je Slice:
- Slice 1 `sinnesverben`: Lesestück „Kochclub-Chat“ (Sophie, Ellie, Amir, Peter planen und probieren eine Suppe). Bild `anhaenger-sinnesverben` (Adjektiv-Anhänger hängt nach tastes zum Subjekt zurück, wie nach is); Szene `szene-sinnesverben` (Kochclub). Übungen: Anhänger wählen (`choice`: nach taste, look, feel, sound das Adjektiv), Handlung oder Zustand (look at me carefully – she looks tired) als `single-choice`, Satz bilden (`write`), Korrigieren (It tastes well, I feel badly), Übersetzen, Diktat. Fehler: tastes well, looks happily, feels badly.
- Slice 2 `adverbien-stellung`: Lesestück „Sophies Blog“ (Eintrag über das Schul-Radio). Bild `satzkarten-stellung` (Satzkarten Subjekt, Verb, Objekt aus der Wortstellung, drei Haken für den orangefarbenen Anhänger: Anfang, Mitte, Ende; zwischen Verb und Objekt gesperrt). Übungen: Haken wählen (`choice`), Satzteile ordnen (`ordering`), Satz bilden (`write`), Korrigieren (He ate quickly his lunch), Übersetzen, Diktat.
- Slice 3 `gradadverbien`: Lesestück „Interview für die Schulzeitung“ (Amir interviewt Mr Hill). Bild `regler-gradadverbien` (Regler von not über quite, rather, very bis extremely, too als rotes Warnzeichen am Ende). Übungen: Regler einstellen (`matching` Satz ↔ Stufe), Wort wählen (`choice`), Satz bilden (`write`), Korrigieren (I very like it, It is too good), Übersetzen, Diktat.
- Slice 4 `stuetzwort-one`: Lesestück „Basar-Chat“ (Sophie und Ellie sortieren Spenden). Bild `anhaenger-one` (der blaue Anhänger bleibt hängen, das Nomen fehlt, `one` steht als Platzhalter). Übungen: one oder ones (`choice`), Satz kürzen (`write`), Korrigieren (the red, a red ones), Übersetzen, Diktat.
- Slice 5 `substantivierte-adjektive`: Lesestück „Zeitungsartikel der Schulzeitung“ (Hilfsaktion für ältere Nachbarn: eigene Fakten, keine echte Statistik). Bild `anhaenger-gruppe` (der Anhänger hängt allein an `the`, daneben eine Gruppe Menschen). Übungen: the + Adjektiv oder Nomen (`choice`), Plural-Verb wählen (are statt is), Satz bilden (`write`), Korrigieren (the riches, a rich), Übersetzen, Diktat.
- Alle Bilder: eigene Zeichnung, `CC-BY-4.0`, erzeugt von `make_images.py` (Funktionen ergänzen), Kinder aus `millbrook-klassenzimmer.svg` von #470 kopiert. Kein Mrs Parker, kein Mr Hill gezeichnet.
- Wiederholungsseiten: `das-brauchst-du` (Kapitel 3, `recap: englisch/wortstellung`, Satzkarten Subjekt – Verb – Objekt, Ort vor Zeit; Text nennt die Karteneintrag-Beschreibung) und `das-brauchst-du` (Kapitel 4, `recap: englisch/artikel`, a, an, the); ohne Übung.
- Prerequisites, die die App nicht übt: `wortstellung` (Recap Kapitel 3), `artikel` (Recap Kapitel 4). Alle anderen `requires` stehen auf früheren Seiten dieser App.
- Daten: keine Datendateien, keine Komponenten (`prefer-built-in-block`): Regler und Satzkarten sind Bilder; ein Ziehen-Regler wäre ein Wunsch für ein späteres Inkrement.

## Code

<!--
- Build locally on the branch, on your own. After each task: `plan done`, then one commit with the work and this
  plan. The hooks check each commit; a failing check is fixed from its message, as skill `lernapps-cli` says.
- What you cannot decide: choose, write it under "Key decisions" with "(guess)", go on.
- The creator asks for a change: say your reading in one sentence first.
-->

### Tasks

- [x] `git switch -c increment/<NN>-<short name>` from `main`. Commit this plan on it.
- [x] Load skill `lernapps-cli`. Update the app as its section "Update" says. Commit the update alone and fix its
      findings before any content. The update replaces the `lernapps-*` skills: read again those you use.
- [x] Load skill `lernapps-explainer` and the content guide.
- [x] Load skill `lernapps-content-questions`. Read whole, with your file tool:
      `.agents/skills/lernapps-explainer/references/blocks.md` and
      `.agents/skills/lernapps-explainer/references/exercises.md`. A foreign language: also
      `references/language-tasks.md` in the same folder. A component in the plan: also `references/components.md`.
- [x] Decide whether the app needs `scope`, as "`scope`" in
      `.agents/skills/lernapps-explainer/references/structure.md` says. Write the choice under "Key decisions".
- [x] Slice 1 (Musterseite, ich allein): Kapitel `genauer-beschreiben` mit `chapter.yaml`, Wiederholung `das-brauchst-du` (recap `englisch/wortstellung`) und Seite `sinnesverben` (`adjektive-nach-sinnesverben`): Lesestück als Chat (150 bis 300 Wörter, Randglossar), Aufgaben in drei Stufen, Grammatik-Übungen, Schreibauftrag, Bilder, Audio; neues Muster „Lesestück“ in den Inhaltsführer.
- [x] Slice 2 (ich allein, Sub-Agent nur für das Lesestück möglich): Seite `adverbien-stellung` (`adverbien-stellung`) mit Blog-/Tagebuch-Lesestück, Satzkarten-Bild für Anfang, Mitte und Ende, Übungen, Audio.
- [x] Slice 3 (ich allein): Seite `gradadverbien` (`gradadverbien`) mit Interview-Lesestück, Bild „Regler“ von not bis extremely und too als Warnzeichen, Übungen, Audio.
- [x] Slice 4 (ich allein): Kapitel `adjektive-ohne-nomen` mit `chapter.yaml`, Wiederholung `das-brauchst-du` (recap `englisch/artikel`) und Seite `stuetzwort-one` (`stuetzwort-one`) mit Chat-Lesestück (Basar), Anhänger-ohne-Nomen-Bild, Übungen, Audio.
- [x] Slice 5 (ich allein): Seite `substantivierte-adjektive` (`substantivierte-adjektive`) mit Zeitungsartikel-Lesestück (Schulzeitung, eigene Fakten), Bild, Übungen, Audio; `app.yaml` (`chapters`, `scope`, `intro`), Selbsteinschätzung der Kapitel 3 und 4.
<!-- tasks: slices (5 added): one per competency, as written in Plan -->
- [x] **Checkpoint:** the pattern page, after the first slice. A slice in a pattern the app already has: show it to
      the creator and go on. A new pattern: load skill `lernapps-learner-check`, do its learner check, fix what it
      finds, then ask the creator whether the others may follow it, and wait.
      Creator: Ja, die anderen vier Seiten dürfen nach dem Muster folgen. Vorlagenpunkte nicht beheben, Seiten etwas kürzer (bis etwa 20 Aufgaben), kein Push bis zur Erlaubnis der Ersteller:in.
- [x] Update the content guide so that it describes the app as it is now (`app-content-matches`).
- [x] Run `npx --no -- lernapps check` until it passes.
- [ ] Look at every changed screen, at 360 px and on a desktop, as "Look at the app" of skill `lernapps-cli` says.

## Commit

<!--
- Publish with the creator's yes. A push to `main` publishes.
- Open the pull requests (to `main`, to the catalog) without asking: they publish nothing.
-->

### Tasks

- [ ] If pages or exercises changed, load skill `lernapps-explainer-self-assessment` and update the self-assessment
      as it says. Commit.
- [ ] Load skill `lernapps-github`. Push the branch, open the preview pull request and see its checks to green, as it
      says.
- [ ] **Checkpoint:** publish. Show what the increment adds and the preview link. Ask whether it may go online. Stop
      and wait for the yes.
- [ ] Load skill `lernapps-commit`. Publish as skill `lernapps-github` says: the pull request squash-merged into
      `main`, the run of `Pages` watched to its end.
- [ ] Open the address the job `deploy` printed and confirm the new content. Never use a derived address.
- [ ] The app is listed and its entry changes (school years, summary): load skill `lernapps-listing` and write the
      changed entry. Else skip this task.
- [ ] Fill the retrospective.
- [ ] Commit this plan on `main` and push it. A push of only `.vibe/` publishes nothing.
- [ ] **Checkpoint:** list. The entry changed: open the pull request to the catalog as skill `lernapps-listing`
      says, without asking first, see it to "bestanden", then show the creator the pull request and its result. The
      entry did not change: tell the creator that the catalog updates the app by itself.
- [ ] If the plan changed since its last push, commit it on `main` and push again.

- Lerner-Check der Musterseite `sinnesverben` (Sub-Agent, Kind Klasse 7-8, 1280 und 360 px, 2026-11-22) und Sprachprüfung Englisch/Deutsch: behoben: Randglossar um die Sinnesverben (look, sound, feel, taste, smell) und weitere Wörter ergänzt, das Zitat aus Zeile 4 wörtlich, „nervös“ statt „aufgeregt“, Handlungsfall mit smell/taste/feel im Merke und in der Übung (Amir smells the cake carefully), die Probe mit is nur „ungefähr“ (I feel bad), Subjekt erklärt, Bild mit Bogen an beiden Sätzen und Legende, Poster-Beispiele anders als die Lösungen der Übungen, Wörtertabelle auf schwere Wörter gekürzt, Chat-Ton mit Kurzformen und haha, Hinweis „hinter das Verb“, Punkt der Meinungsaufgabe „kein Adverb auf -ly (nicht tastes sweetly)“, Wiederholungsseite erinnert an die Anhänger. Nicht behoben: Standardmeldung „Deine Fassung kann trotzdem richtig sein“ bei Tippfehlern, unvollständigen Sätzen und Hördiktaten und „1: nicht richtig.“ bei `choice` (Vorlage, bekannt); die Seite ist mit etwa zehn Aufgaben lang (Nachsprechen und Meinung sind der Anwendungsteil); „Zeile“ statt „Nachricht“ bleibt wie im Muster der Konventionen.

- Auftrag der Ersteller:in (über die Orchestrator-Session, 2026-11-22): `lernapps update` (app-templates 0.14.0, tooling 0.18.4) und alle reinen Vokabel-Tabellen (Randglossare, „Wörter dieser Seite“) durch den Block `vocabulary` ersetzen: 20 Tabellen in 11 Dateien umgestellt (Seiten der ersten Version und des Inkrements); `definition`-Blöcke gibt es in der App nicht. `lernapps check`: 0 Fehler.

- Gesamtcheck der neuen Seiten (Sub-Agent, Kind Klasse 7-8, 360 und 1280 px, 2026-11-22; er lief teils gegen einen älteren Stand, ohne die Vokabelblöcke) und Sprachprüfung Englisch/Deutsch: behoben: Kapitelnummern durch Kapiteltitel ersetzt, Peters „little sister“ durch „cousin“, Ende von `sinnesverben` passt zum Blog, Anfangsstellung und Zeitformen in den Stellungs-Aufgaben zugelassen, mehrere richtige Lösungen genannt, Regelsätze präzisiert (Adverbien auf -ly, Hilfsverb, one nur zählbar), „not too bad“ und Namen im Interview entfernt, Gradadverbien mit Bedeutungen (ziemlich, sehr, äußerst, zu), Glossare ergänzt (clearly, easily, almost, elderly, a few …), Doppelungen zwischen Auswahl und Korrektur sowie Merke und Aufgabe aufgelöst, sensible Hörsätze durch neutrale ersetzt, Höflichkeitshinweis zu the elderly/the old, Wiederholungsseite Kapitel 3 als zweispaltige Tabelle (360 px), Sophies Alter im Artikel gestrichen. Nicht behoben, Vorlage: Standardmeldung „Deine Fassung kann trotzdem richtig sein“, `choice` ohne Fehlerhinweis, Auswahl-Sortierfelder. Beobachtung: Der Vokabelblock zeigt jedes Wort als eigene Karte und macht die Seiten bei 360 px länger (rund 12 800 px bei `sinnesverben`).

## Retrospective

<!-- At the end of Commit. Facts, short, no names. Read by review and evals. -->

### Phases reached

<!-- Last phase completed, checkpoints passed. E.g. "commit; confirmed, published". -->

### Creator turns after the plan

<!-- Number of creator messages after the confirmation, topic of each. Target: at most 3. -->

### Where I had to guess

<!-- Each gap in plan, skills, content guide, messages or answers, and your choice. "None" if none. -->
