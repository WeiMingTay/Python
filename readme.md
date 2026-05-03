# M3.1.1 Aussagen und Wahrheitswerte


## 👤 User Story 

Als IT-Azubi
möchte ich verstehen, was eine mathematische Aussage ist,
damit ich eindeutige Variablen für Systemkonfigurationen definieren kann.



## 🎉 Celebration Criteria (Lernziele) 

- Ich kann erklären, was eine logische Aussage von einem normalen Alltags-Satz unterscheidet. (K2)

- Ich kann Texten die Wahrheitswerte "Wahr" (1) oder "Falsch" (0) mathematisch zuordnen. (K3)

- Ich kann boolesche Variablen sauber und unmissverständlich für die IT benennen. (K3)


### 🚧 Typische Fallstricke & Impulsfragen 

Fallstrick: Befehle als Aussagen werten. "Drucke das Dokument" ist eine Aktion, kein messbarer Zustand.

Fallstrick: Subjektive Variablen. A = "Netzwerk ist schnell" ist nutzlos. Besser: A = "Ping < 50ms".

Impulsfrage: Stell dir vor, du fragst einen extrem dummen Roboter. Kann er auf deinen Satz nur mit "Ja" oder "Nein" antworten? Wenn nicht, ist es keine Aussage.

## 🔥 Freiwillige Zusatzaufgaben (Bloom K4 & K5) 

[Transfer] Übersetze die eher abstrakte mathematische Bedingung "x ist eine gerade Zahl" in eine konkrete Formulierung, die von einer Tabellenkalkulation eindeutig auf Wahr oder Falsch geprüft werden kann. (K4)
- [Bewertung] Bewerte kritisch die Variablen-Benennung A = "Türe ist nicht zu" und begründe detailliert, warum eine solche Negation direkt im Namen bei der späteren Verarbeitung zu massiven Denkfehlern führen wird. (K5)
- Tabellenkalkulation] Simuliere in Calc das Prinzip der "Fuzzy Logic" (Unscharfe Logik), indem du eine Zelle erstellst, die den Dezimalwert 0,7 annimmt, und berechne das logische Gegenteil durch die Operation 1 - Wert. (K5)
- [Datenbank] Vergleiche den binären Zustand False (Falsch) mit dem SQL-Wert NULL (Leer) und begründe fachlich, warum eine leere Datenbankzelle nicht einfach automatisch als logisch "falsch" gewertet werden darf. (K5)
### - [Programmierung] Schreibe ein kleines Python-Skript, das eine Eingabe vom Benutzer anfordert und mittels der Funktion bool() prüft, ob die Eingabe als Wahrheitswert interpretiert werden kann. (K5)