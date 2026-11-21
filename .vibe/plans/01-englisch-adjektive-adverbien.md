---
# Read by the hooks, the review, the evals. Schema: @lernapps/tooling/guidance/plan-front-matter.v1.schema.json
# Written by `lernapps plan` and the hooks. Never change a key or a value by hand.
# Archetype, null until chosen in Explore. Allowed values: explainer, interactive, quiz.
archetype: explainer
# Current phase. Allowed values: explore, plan, code, commit.
phase: code
# prePushFailures: failed pre-push runs, written by the hook.
prePushFailures: 0
# failedChecks: failed rules and runs, written by lernapps check and the hooks.
failedChecks: {}
---

# Plan: englisch-adjektive-adverbien, first version

<!--
For you, the assistant. The process is in AGENTS.md; this plan holds the method.
- `npx --no -- lernapps plan next` prints the task to do now, `plan done` ticks it and prints the next one.
- You write only below Goal, Key decisions, Notes, Answers, Entry draft, Content method and Retrospective, in the
  creator's language. Delete the comment of a section once the section is filled.
- Work on the branch `work`, locally: push nothing before Commit.
-->

*Started 2026-11-21. Explore, Plan, Code, Commit.*

## Goal

Kinder der Klassen 5-6 (erstes und zweites Lernjahr Englisch) beschreiben und vergleichen Personen, Dinge und Handlungen aus Millbrook. Sie lernen, Adjektive und Adverbien zu setzen, zu steigern und zu unterscheiden. Erste Version: Stufe 5-6 (Kapitel 1 und 2 von Issue #476); Kapitel 3 und 4 (Stufe 7-8) kommen später als Inkremente.

## Key decisions

- Archetyp `explainer`: Die Kinder brauchen erst Erklärung mit Bildern (Anhänger, Treppe) und dann Übungen mit Rückmeldung. Quiz trägt keine Erklärung, interactive wäre ein Spiel oder Training (Issue und Konventionen verlangen einen Explainer).
- Strang-App `strand: englisch/grammatik`, Format 2, Sprache Deutsch, englische Beispiele, britisches Englisch, Anrede „du“ (Vorgabe Issue #476 und Konventionen #489).
- Zwei Kapitel, sechs Bausteinseiten und eine Sammel-Wiederholung (`recap: englisch/to-be`): Kapitel 1 `beschreiben-und-vergleichen`, Kapitel 2 `wie-jemand-etwas-tut` (Issue, Stufe 5-6).
- Leitbild: Mr Hill lässt die Klasse für den Schulflur die Ausstellung „Our Millbrook“ beschriften (Orte, Dinge und Leute der Kleinstadt). Es gibt Anhänger (Adjektiv-Anhänger blau am Nomen, Adverb-Anhänger orange mit -ly am Verb) und eine Steigerungstreppe (Grundform, Steigerung, Höchststufe). Nicht „Sports Day“: die Szene kommt schon in #471 vor (Hinweis des Orchestrators, 2026-11-21). Figuren bleiben wie in #470.
- Audio: Stimme `bf_emma`, nur ganze Sätze, Diktat und Nachsprechen je Seite (Konventionen §5).
- Keine Komponente, keine Datendateien (wie #472) (guess).

## Notes

- Fach/Strang: Englisch, Strang `grammatik`, Karte `https://lernapps.net/apps/map/englisch.json`, `explainerFocus: competency`, Band 5-6. Alle sechs Bausteine sind Lücken der Karte (`practisedBy` leer).
- Kapitel 1 · Beschreiben und vergleichen (Ich kann mit Adjektiven beschreiben, sie steigern und mit than und as … as vergleichen):
  - Wiederholung `recap: englisch/to-be` (Seite `das-brauchst-du`, ohne Übung). Das ist die einzige Voraussetzung von außen: `adjektive` verlangt `to-be`. Die Seite zeigt auch den leeren Anhängerstrang und die Treppe als Leitbild.
  - `adjektive` · Stellung der Adjektive (Schritt 3, öffnet 17): „Ich kann Adjektive vor ein Nomen (a big house) und nach „be“ (The house is big.) stellen.“
  - `adjektive-steigern` · Steigerung der Adjektive (Schritt 4, öffnet 4): „Ich kann Adjektive steigern, mit -er/-est, mit more/most und unregelmäßig (good – better – best).“
  - `vergleiche` · Vergleiche: than, as … as (Schritt 5, öffnet 2): „Ich kann mit than, as … as und not as … as vergleichen.“
- Kapitel 2 · Wie jemand etwas tut (Ich kann mit Adverbien sagen, wie jemand etwas tut, sie steigern und weiß, wann ich ein Adjektiv und wann ein Adverb brauche). Die Seiten bauen auf Kapitel 1 auf, `adjektive` und `adjektive-steigern` stehen dort:
  - `adverbien-art-und-weise` · Adverbien der Art und Weise (Schritt 4, öffnet 5): „Ich kann Adverbien der Art und Weise bilden (quick – quickly) und die Sonderformen well, fast und hard verwenden.“
  - `adjektiv-oder-adverb` · Adjektiv oder Adverb (Schritt 5, öffnet 1): „Ich kann entscheiden, ob ich ein Adjektiv oder ein Adverb brauche (a careful driver – she drives carefully).“
  - `adverbien-steigern` · Steigerung der Adverbien (Schritt 5, öffnet 0): „Ich kann Adverbien steigern und damit Handlungen vergleichen (She runs faster than I do.).“
- Karte der Seiten (Explainer-Design): Kapitel 1 `beschreiben-und-vergleichen`: `das-brauchst-du` (recap `englisch/to-be`) → `adjektive` → `adjektive-steigern` → `vergleiche`. Kapitel 2 `wie-jemand-etwas-tut`: `adverbien` (`adverbien-art-und-weise`) → `adjektiv-oder-adverb` → `adverbien-steigern`. Voraussetzungen, die die App nicht übt: nur `to-be` (aus #472, Recap am Anfang von Kapitel 1). Alle anderen `requires` liegen auf früheren Seiten der App (`adjektive` → `adjektive-steigern` → `vergleiche`; `adverbien-art-und-weise` → `adjektiv-oder-adverb`; `adverbien-steigern` braucht `adverbien-art-und-weise` und `adjektive-steigern`). Kein `ahead`. Gute Stufe auf die Karte: Kapitel 2 braucht kein eigenes Recap, die Treppe aus Kapitel 1 kommt auf `adverbien-steigern` als Rückblick.
- Ablauf der Seiten (Konvention aus #472): `einstieg`, `neu`, `uebung` (mindestens vier, leicht → schwer), `anwenden`, `weiter`; höchstens 350 Wörter Text, Bild oder Übung in den ersten vier Blöcken.
- Didaktik: Adjektiv-Anhänger hängen am Nomen oder nach be. Adverb-Anhänger tragen meist -ly und hängen am Verb. Frage zum Wählen: Beschreibt das Wort ein Ding oder eine Handlung? Treppe: kurz big – bigger – the biggest, lang interesting – more interesting – the most interesting, unregelmäßig good – better – the best, bad – worse – the worst; zweite Seite der Treppe für Adverbien (fast – faster – the fastest, carefully – more carefully – the most carefully, well – better – best).
- Wörter aus dem Grundwortschatz A1 und A2 (Karte, geöffnet 2026-11-21). Adjektive A1: big, small, tall, short, old, new, fast, slow, quick, quiet, loud, happy, sad, good, bad, easy, difficult, hard, careful, interesting, exciting, expensive, cheap, beautiful, funny, friendly, busy, tired, hot, cold. Adverbien A1: slowly, quickly, quietly, loudly, carefully, happily, easily, kindly, early, late, fast, hard, well; A2: badly, politely, patiently, safely, calmly. Was nicht in der Liste steht (Sports Day, race, Sportfest) steht auf der Seite mit Bedeutung und wird im Inhaltsführer gelistet.
- Grenzen (Scope): drin: Adjektive vor Nomen und nach be, Steigerung (-er/-est, more/most, unregelmäßig good/bad, Rechtschreibregeln y → ier, Verdoppeln big – bigger), than, as … as, not as … as, Adverbien auf -ly (auch -y → -ily), Sonderformen well, fast, hard, die Frage Adjektiv oder Adverb, Steigerung der Adverbien (faster, more carefully, better). Draußen: Häufigkeitsadverbien (#472), Wörter zum Beschreiben von Personen als Wortschatz (#477), Adjektive nach Sinnesverben, Stellung der Adverbien im Satz, Gradadverbien (very, quite), one, substantivierte Adjektive (Kapitel 3 und 4, später), less/least, Adjektivreihenfolge.
- Wie die Kinder dorthin kommen: Sie hängen Anhänger an Karten und Sätze, ordnen Treppenstufen, entscheiden mit der Frage „Ding oder Handlung?“, bilden Formen und schreiben eigene Karten. Typische Fehler mit eigener Meldung: Adjektiv nach Nomen (a house big), Mehrzahl-s am Adjektiv (bigs houses), more + -er (more bigger), -er bei langen Adjektiven (interestinger), good statt well (She sings good), -ly vergessen (She runs quick), more/most bei than vergessen (taller as), „then“ statt than, „as … than“, Adjektiv statt Adverb hinter dem Verb nach be (She is carefully), fast – fastly, hardly statt hard.
- Datenumfang: Adjektive nur aus A1/A2 der Liste (rund 30 Adjektive, 15 Adverbien, siehe Wörter), unregelmäßig nur good/bad (better/best, worse/worst) und well; keine Datendatei. Sprachen: Deutsch (Erklärungen), Englisch (Beispiele, Audio).
- Wie die Kinder dorthin kommen, und was die Rückmeldung fängt, je Baustein:
  - `adjektive`: Sie hängen den blauen Anhänger an ein Nomen und sehen, dass er davor und nach be steht, nie nach einem anderen Verb; sie leiten ab, dass der Anhänger nie ein -s trägt (a big house – two big houses). Fängt: a house big, bigs houses, The house big (be vergessen).
  - `adjektive-steigern`: Sie ordnen Adjektive auf der Treppe (kurz, lang, unregelmäßig) und leiten die Regel aus der Silbenzahl ab; sie bilden Formen mit Rechtschreibung (big – bigger, happy – happier). Fängt: more bigger, interestinger, gooder, the most big.
  - `vergleiche`: Sie legen zwei Dinge auf die Treppe und wählen than (Unterschied) oder as … as (gleich); not as … as dreht die Richtung. Fängt: taller then, taller as, as taller as, more tall than.
  - `adverbien-art-und-weise`: Sie hängen den orangen Anhänger -ly an das Verb und leiten die Sonderfälle ab (happy – happily, fast – fast, hard – hard, good – well). Fängt: She runs quick, fastly, hardly statt hard, She sings good, carefuly.
  - `adjektiv-oder-adverb`: Sie fragen „Ding oder Handlung?“ und entscheiden mit der Frage; nach be steht der Adjektiv-Anhänger. Fängt: She is carefully, a carefully driver, She drives careful, He is good at running – He runs good.
  - `adverbien-steigern`: Sie legen die Treppe für Handlungen und leiten ab: fast – faster, aber carefully – more carefully; well – better. Fängt: more fast, carefullier, She runs fastest than, better statt well in der Grundform.
- Quellen (nur Fakten, geöffnet 2026-11-21): Wikipedia „Degrees of comparison of adjectives and adverbs“ (-er/-est bei einer Silbe, more/most bei drei und mehr, unregelmäßige Formen, than und as … as, Doppelsteigerung als Fehler) und „Adverb“ (Adverbien der Art und Weise oft mit -ly, flat adverbs wie fast, Steigerung der Adverbien mit more/most, well – better – best). Nicht geprüft: Klexikon, deutsche Wikipedia. Beispielsätze sind eigene aus dem Alltag der Figuren; Material der Ersteller:in: keines. Vorbild: `lernapps/englisch-zeiten` (#472, Branch `work`): Inhaltsführer, Seitenaufbau, Aufgabenmuster, Audio-Skript.
- Audio: Umgebung geprüft (`lernapps_audio.py preflight` ok).
- Offene Fragen: keine.

## Explore

<!--
- Find out what the app teaches, for whom, how much and how it looks. Ask; write no code, run no `create`.
- An answer counts only in the creator's words under "Answers". At most 2 questions per message, one topic each.
-->

### Tasks

- [x] Check the start: the folder `.agents/skills/lernapps-app` exists (else stop and tell the creator that the folder
      was not started with `init`), and `git branch --show-current` prints `work` (else `git switch -c work`).
- [x] Load skill `lernapps-app`. Tell the creator in two sentences what a lernapps app is and where it will live: at
      their own address, free and public, and once listed as a copy on lernapps.net. Say that the technical part
      (GitHub) comes at the end and that you do it.
- [x] Interview: ask the topics "Goal" and "Learners" of "Answers".
- [x] Load skill `lernapps-map-assignment` and read the learning map of the subject as it says. The creator brings
      the content themselves (material, a word list, the pages): note under "Notes" which competencies of the map it
      covers. Else write the skill's assignment, with its story; the creator's yes answers the topics Content and
      Amount. A subject without a map: skip this task and say so.
- [x] Load skill `lernapps-exercise-patterns` and read its reference for the subject. Note under "Notes" how learners
      will practise what the goal names.
- [x] Choose the archetype as skill `lernapps-app` says: read the README of each archetype in question, then tell the
      creator in plain words what the chosen one can and cannot do. Write the archetype and its reason under "Key
      decisions".
- [x] Run `npx --no -- lernapps skills --archetype <name>` with the chosen archetype. It installs the archetype's
      skills and adds the archetype's tasks to this plan.
- [x] Load skill `lernapps-explainer-design`. An explainer has the look of the runtime: write "fixed by the
      archetype" under the topic "Look and feel" of "Answers".
- [x] Interview: ask every other topic of "Answers", in order. Leave out only a topic that an answer of the creator
      already covers, and note which answer. A topic nobody answered is asked once before you write an assumption
      with "(guess)".
- [x] Load skill `lernapps-content-research` and research as it says. Write under "Notes": the strand or subject, the
      competencies by chapter with their ids, the sources you opened.
- [x] Write under "Notes" which competency goes on which page and which pages form a chapter, as "Map the content" of
      skill `lernapps-explainer-design` says. Per page, name the prerequisites the app does not practise.
- [x] Write under "Notes", one line per competency: how learners get there (they derive it, they do not only read it
      off), and which misconception the feedback catches.
- [x] Write under "Notes" the scope: what is in, what is out and why, the data range (for example "all main-group
      elements", never a silent "1–20"), the languages.
- [x] **Checkpoint:** research. Show in plain words: the strand or why none, the competencies by chapter, the didactic
      approach, the scope, every "(guess)", the sources and what is unchecked, the archetype and its reason. Stop and
      wait. Changes: change them, then ask again.
      Creator: Ja, Plan so fortsetzen. Szene nicht Sports Day (kommt in #471 vor), andere Szene nehmen; Steigerungsformen vor dem Plan gegen den Grundwortschatz prüfen.

### Answers

<!-- The interview: per topic the creator's answer, in their words. Keep the topics. -->

Antworten der Ersteller:in: aus dem Auftrag (Issue #476, „unverändert“) und den Konventionen #489, die die Orchestrator-Session für sie vorgibt. Es gab kein Gespräch; wo der Auftrag schweigt, steht „(guess)“.

- Goal: „Ich kann Personen, Dinge und Handlungen genau beschreiben und vergleichen und weiß, ob ich ein Adjektiv oder ein Adverb brauche.“ Zwei Sorten Anhänger und eine Steigerungstreppe tragen den Explainer.
- Learners: Klassen 5-6, erstes und zweites Lernjahr Englisch, Vorwissen Hello, Millbrook! (#470), Personalpronomen (#471) und to-be (#472).
- Model and focus: Vorbilder `hello-millbrook`, #472 (`englisch-zeiten`), #471 und #480. Wichtig sind Übungen mit Rückmeldung und die Bilder von Anhängern und Treppe. Kein Spielgefühl.
- Hurdles: (guess) Adjektiv hinter dem Nomen, Mehrzahl-s am Adjektiv, doppelte Steigerung (more bigger), good statt well, -ly vergessen, then statt than.
- Content: aus Quellen, von mir geschrieben; kein eigenes Material.
- Amount: erste Version Kapitel 1 und 2 (Stufe 5-6, sechs Bausteine, drei Seiten je Kapitel); Kapitel 3 und 4 später als Inkremente.
- Languages: Deutsch, englische Beispiele.
- Look and feel: ruhig wie ein Arbeitsblatt (Vorgabe der Vorlage), Dunkelmodus folgt dem Gerät.
- Terms: Anhänger (Adjektiv-Anhänger, Adverb-Anhänger), Treppe (Stufe), „Ausdruck“, „Klassenzimmer-Poster“, „Schulkalender“ (Konventionen).
- Finding the app: (guess) englisch adjektive adverbien steigern vergleichen, Adverb oder Adjektiv, than as … as.

## Plan

<!--
- Map the confirmed content onto the archetype. No new content questions: a gap in the content goes back to Explore.
- The creator confirms the plan in one read. After the yes you work on your own.
-->

### Tasks

- [x] Map the content as "Map the content" of skill `lernapps-explainer-design` says, and write the result under
      "Content method".
- [x] Choose a pattern per competency as skill `lernapps-exercise-patterns` says, and add it to "Content method".
- [x] Add to "Content method" one line per page, as "Engagement" of skill `lernapps-explainer-design` says: the
      opening task, the change of activity, the reward, the story.
- [x] Add the tasks of Code, each one a piece of work that ends in a commit. First the pattern: one complete page or
      screen, `npx --no -- lernapps plan add --at pattern "<task>"`. Then the others, one call each:
      `npx --no -- lernapps plan add --at pages "<task>"`. Each task says what it builds and what it shows.
- [x] Draw a sketch of each screen, component or interactive exercise: a static SVG or image, or the steps with what
      learners see after each. Keep the files in `.vibe/sketches/`.
- [x] Show the creator, short: goal, competencies by chapter, the Code tasks, the sketches, and the content method in
      plain words (what learners see and do, what the app cannot do). At most 2 questions.
- [x] **Checkpoint:** confirm the plan and the content method. Stop and wait for an explicit yes. Changes: change
      them, then ask again.
      Creator: Ja, so bauen. Bedingungen: competencies auf Karten-Ids, Szene Our Millbrook melden, Steigerungsformen auf der Seite erklären und im Inhaltsführer listen, Lerner-Check mit Sub-Agent und Sprachprüfung vor Checkpoint Musterseite.

### Content method

Geschichte: Mr Hill lässt die Klasse für den Schulflur die Ausstellung „Our Millbrook“ aufbauen: Fotos und Zeichnungen von Orten, Dingen und Leuten der Stadt. Sophie, Ellie, Peter und Amir beschriften sie mit Anhängern. Kapitel 1 beschreibt und vergleicht Dinge und Leute, Kapitel 2 beschreibt, wie Leute etwas tun (die Kinder zeigen ein Stück vor: Peter läuft, Ellie malt, Amir liest). Tabellen: „Klassenzimmer-Poster · Anhänger und Treppe“ und „Schulkalender · …“ wachsen von Seite zu Seite. Figuren und Orte wie in #470 (nicht ändern).

Wörter: Quelle ist der Grundwortschatz A1/A2 (`https://lernapps.net/apps/map/englisch/grundwortschatz/`, geöffnet 2026-11-21, geprüft). A1: big, small, tall, short, old, new, fast, slow, quick, quiet, loud, happy, sad, good, bad, easy, difficult, hard, careful, interesting, exciting, expensive, cheap, beautiful, funny, friendly, busy, hot, cold, long, young, strong, clean, nice, clever, warm; Adverbien slowly, quickly, quietly, loudly, carefully, happily, easily, kindly, early, late, well. A2: heavy, dirty, tidy, polite, badly, politely, patiently, safely, calmly, gently, softly, sadly. Außerhalb der Liste, auf der Seite mit Bedeutung eingeführt und im Inhaltsführer gelistet: die Steigerungsformen bigger, biggest, better, best, worse, worst (Formen der Liste-Wörter), exhibition (A2), poster. Nicht verwendet, weil nicht in der Liste: bakery, bridge, brave, lazy, neatly, project, duck.

Muster (je mit `mistakes` und `hint`, leicht → schwer, mindestens vier je Seite, nicht überwiegend Raten):
1. Anhänger anheften: `choice`-Lücke (Adjektiv oder Platz) und `ordering` der Satzteile (Anhänger vor das Nomen, nach be). Fehler: a house big, bigs houses.
2. Treppe ordnen: `ordering` und `matching` (Adjektiv ↔ Stufe/Regel kurz, lang, unregelmäßig); `language-task` `table` für die Treppe eines Adjektivs (Grundform, Steigerung, Höchststufe).
3. Form bilden: `language-task` `write` mit `cue` (`cue: "big · Steigerung"`, englisch ohne deutsches Wort), Satz ergänzen.
4. Vergleichen: `choice` than / as … as, `write` mit Cue (Ellie · tall · Peter), `true-false` zu Aussagen über ein Bild mit Begründung.
5. Entscheiden mit Begründung: `single-choice` „Ding oder Handlung?“ mit Rückmeldung, die die Frage nennt.
6. Korrigieren: `language-task` Satz mit einem Fehler (She sings good → well).
7. Übersetzen: `write` mit `source` (deutsch) und `accepted`/`(a|b)`.
8. Hören: Diktat (höchstens drei ganze Sätze je Seite), Nachsprechen `speaking-task` (drei Sätze, andere als im Diktat). Je Seite sechs Sätze, 36 insgesamt, Namen am Satzende zweisilbig (Sophie, Ellie, Peter, Amir), erzeugt mit `regen_audio.py` aus #472.
9. Anwenden: `open-task` (eigene Karte oder Anhänger für die Ausstellung, mit Punkten zu Form und Inhalt).

Seiten, je eine Zeile Engagement (Opening / Wechsel / Belohnung / Geschichte):
- `das-brauchst-du` (recap `englisch/to-be`, ohne Übung, Tabelle am Poster, leere Anhängerleiste und leere Treppe): Wiederholung von am/is/are, die Ausstellung beginnt.
- `adjektive` (Musterseite; Opening: Foto-Karte, welcher Anhänger gehört an das Nomen; Wechsel: schauen, anheften, ordnen, schreiben; Belohnung: Karte hängt in der Ausstellung; weiter: Mr Hill fragt, wer größer ist).
- `adjektive-steigern`: Treppe mit drei Stufen, kurz/lang/unregelmäßig; Opening: Peter und Ellie stellen sich an die Messlatte (tall – taller – the tallest); Rechtschreibung als Merke-Kasten (big – bigger, happy – happier).
- `vergleiche`: Opening: Ellie ist größer als Peter; than und as … as legen zwei Dinge nebeneinander auf die Treppe; Rückblick des Kapitels am Ende.
- `adverbien` (`adverbien-art-und-weise`): Opening: Amir zeichnet langsam und vorsichtig, Frage „Wie?“; Adverb-Anhänger mit -ly (y → ily), Sonderformen well, fast, hard; Merke-Kasten.
- `adjektiv-oder-adverb`: Opening: a careful driver, she drives carefully; die Frage „Ding oder Handlung?“; nach be ein Adjektiv, good ↔ well.
- `adverbien-steigern`: zweite Seite der Treppe (fast – faster – the fastest, carefully – more carefully – the most carefully, well – better – the best); Rückblick: beide Treppen und beide Anhänger am Poster. Kapitelende mit Rückblick.

Bilder (eigene Zeichnung, CC-BY-4.0, `src/images/`, Hintergrund #f4efe2, Schrift mindestens 16 im 480er viewBox, 360 px tauglich, Skizzen in `.vibe/sketches/`): Figurenfamilie `anhaenger-<seite>.svg`: Adjektiv-Anhänger blau (#2c6fd8) rund mit Loch, hängt an einem Nomen-Karton oder nach „is“; Adverb-Anhänger orange (#d35400) mit -ly, hängt am Verbkarton; Treppe `treppe-<seite>.svg` aus drei Stufen (Grundform, Steigerung, Höchststufe), Adjektiv-Treppe grün (#138d75), Adverb-Treppe ebenso mit orangen Anhängern. Szenen `szene-<seite>.svg` mit den Figuren, kopiert als `<g id>` aus `millbrook-klassenzimmer.svg` von #470 (hello-millbrook) und gleich gelassen; `alt` verrät nie die Lösung.

Datendateien: keine. Komponenten: keine (`prefer-built-in-block`); eine Ziehen-Übung für Anhänger und Treppe wäre ein Wunsch für ein Inkrement.

Wie ein späterer Agent ein Kapitel anfügt (Kapitel 3 und 4, Stufe 7-8): Ordner `src/<kapitel>/` mit `chapter.yaml`, Seiten mit den Abschnitten `einstieg`, `neu`, `uebung`, `anwenden`, `weiter`; neue Anhänger-Zeichen und Treppenstufen in die Figurenfamilie, Zeilen in die Poster-Tabellen; Audio über `regen_audio.py`; `lernapps check`. Kapitel 3 legt die Satzkarten aus #473 an die Anhänger; Kapitel 4 nimmt dem Adjektiv-Anhänger das Nomen weg (one, the rich).
<!-- An explainer: per figure, model and component its learning action in two to four sentences
(`explainer-representation-explained`); per page its prerequisites the app does not practise, and which get a recap
page, which a link. -->

## Code

<!--
- Build the app, locally on `work`, on your own. After each task: `plan done`, then one commit with the work and this
  plan. The hooks check each commit; a failing check is fixed from its message, as skill `lernapps-cli` says.
- What you cannot decide: choose, write it under "Key decisions" with "(guess)", go on.
- The creator asks for a change: say your reading in one sentence first, then change every place it holds for
  (`feedback-applied-everywhere`).
-->

### Tasks

- [x] Load skill `lernapps-cli`. Create the app as its section "Create" says:
      `npx --no -- lernapps create --archetype explainer`.
- [x] Fill the content guide `.agents/skills/app-content/SKILL.md` from "Notes" and "Content method": every heading,
      no "FILL IN" left. Commit it before any content.
- [ ] Load skill `lernapps-explainer`.
- [ ] Load skill `lernapps-content-questions`. Read whole, with your file tool:
      `.agents/skills/lernapps-explainer/references/blocks.md` and
      `.agents/skills/lernapps-explainer/references/exercises.md`. A foreign language: also
      `references/language-tasks.md` in the same folder. A component in the plan: also `references/components.md`.
- [ ] Decide whether the app needs `scope`, as "`scope`" in
      `.agents/skills/lernapps-explainer/references/structure.md` says. Write the choice under "Key decisions".
- [ ] Musterseite kapitel 1 `adjektive`: Kapitel `beschreiben-und-vergleichen` mit `chapter.yaml` und der Seite `adjektive` (einstieg, neu, uebung, anwenden, weiter), Bilder `szene-adjektive` und `anhaenger-adjektive`, sechs Audiosätze (Diktat, Nachsprechen); zeigt Anhänger am Nomen und nach be.
<!-- tasks: pattern (1 added): the one page or screen that is the pattern for the others -->
- [ ] **Checkpoint:** the pattern page. Load skill `lernapps-learner-check` and do its learner check on the page. Fix
      what it finds. Then show the creator the page and ask whether the others may follow it. Stop and wait. A
      change: change the pattern first.
- [ ] Seite `das-brauchst-du` (Recap `englisch/to-be`, ohne Übung, mit leerer Anhängerleiste und leerer Treppe) und Tabelle `Klassenzimmer-Poster · Anhänger und Treppe`.
- [ ] Seite `adjektive-steigern` mit Treppenbild (kurz, lang, unregelmäßig), Merke-Kasten für Rechtschreibung, Übungen, sechs Audiosätze.
- [ ] Seite `vergleiche` (than, as … as, not as … as), Kapitel-Rückblick, Selbsteinschätzung des Kapitels, sechs Audiosätze.
- [ ] Kapitel `wie-jemand-etwas-tut` mit `chapter.yaml` und Seite `adverbien` (-ly, y → ily, well, fast, hard), Bilder, Übungen, sechs Audiosätze.
- [ ] Seite `adjektiv-oder-adverb` (Frage Ding oder Handlung, nach be, good ↔ well), Übungen, sechs Audiosätze.
- [ ] Seite `adverbien-steigern` (zweite Seite der Treppe, Rückblick beider Treppen), Kapitel-Rückblick, Selbsteinschätzung, sechs Audiosätze.
- [ ] `app.yaml` (Titel, intro, scope, chapters) und Audio-Liste `audio-texte.json`, `regen_audio.py` aus #472, alle 36 Sätze erzeugt und angehört (Ausklingen abgeschnitten).
<!-- tasks: pages (7 added): the other pages or screens, after the pattern -->
- [ ] Update the content guide so that it describes the app as built (`app-content-matches`).
- [ ] Run `npx --no -- lernapps check` until it passes.
- [ ] Look at every screen and state, at 360 px and on a desktop, as "Look at the app" of skill `lernapps-cli` says.
      Compare each with its sketch.
- [ ] Do the whole-app check of skill `lernapps-learner-check`. Fix what it finds and write under "Notes" what you
      fixed.

## Commit

<!--
- Put the app on GitHub, publish it with the creator's yes, then list it. A push to `main` publishes.
- Open the pull requests (to `main`, to the catalog) without asking: they publish nothing.
- The creator asked to stop before publishing (a trial): stop here and say so.
-->

### Tasks

- [ ] Load skill `lernapps-explainer-self-assessment`. Add the self-assessment as it says, or write under "Key
      decisions" why the app has none. Commit.
- [ ] Load skill `lernapps-github`. Set up the repository and Pages as it says. Ask for the repository's name and
      every click only the creator can make, in one message.
- [ ] Push `work`, open the preview pull request and see its checks to green, as skill `lernapps-github` says.
- [ ] **Checkpoint:** publish. Show what the app does and the preview link from the comment "Vorschau der App". Ask
      whether it may go online. Stop and wait for the yes.
- [ ] Load skill `lernapps-commit`. Publish as skill `lernapps-github` says: `work` into `main` as one squash commit,
      the run of `Pages` watched to its end.
- [ ] Open the address the job `deploy` printed and confirm that the app shows. Never use a derived address.
- [ ] Load skill `lernapps-listing`. Write the entry under "Entry draft" as it says, with the creator's answer to
      "Finding the app".
- [ ] Fill the retrospective.
- [ ] Commit this plan on `main` and push it: the listing check and the review read it there.
- [ ] **Checkpoint:** list. Open the listing pull request as skill `lernapps-listing` says, without asking first: the
      pull request is the review. See it to "bestanden", then show the creator the pull request and its result.
- [ ] If the plan changed since its last push, commit it on `main` and push again.

### Entry draft

<!-- YAML valid against the entry schema the listing skill names. Only known values, never invented. -->

```yaml
```

## Retrospective

<!-- At the end of Commit, before the listing pull request. Facts, short, no names. Read by review and evals. -->

### Phases reached

<!-- Last phase completed, checkpoints passed. E.g. "commit; confirmed, published". -->

### Creator turns after the plan

<!-- Number of creator messages after the confirmation, topic of each. Target: at most 3. -->

### Where I had to guess

<!-- Each gap in plan, skills, messages or answers, and your choice. "None" if none. -->
