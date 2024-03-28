# ---------------------------------------------------------------------------------------------
# auto_complete.py
# ---------------------------------------------------------------------------------------------
# Implementierung der Klasse AutoComplete mit den Operationen
#   AutoComplete(filename)      erzeugt AutoComplete-Objekt mit alphabetisch geordneter Term-Liste
#   .match(prefix)              gibt eine nach Gewichten sortierte Liste der Begriffe zurück, die mit prefix beginnen
#   .matches(prefix)            gibt die Anzahl der Begriffe zurück, die mit prefix beginnen
#   len(...)                    gibt die Anzahl der in ... gespeicherten Begriffe zurück
#   str(...)                    gibt AutoComplete-Objekt als String zurück
# ---------------------------------------------------------------------------------------------

import sys
from term import Term


# === Definition der Klasse AutoComplete ======================================================

class AutoComplete:

    # -----------------------------------------------------------------------------------------
    # Konstruktor
    # Begriffe mit zugehörigen Gewichten werden aus der Datei filename eingelesen
    # und jeweils als Term alphabetisch sortiert in einer Liste abgespeichert.
    def __init__(self, filename):
        self.term_list = []
        data = open(filename, 'r', encoding='utf-8')
        next(data)

        for line in data:
            term = Term(int(line[:14]), line[15:])
            self.term_list += [term]

        self.term_list.sort(key=lambda e: e.word)

    # -----------------------------------------------------------------------------------------
    # match(prefix) gibt eine nach den Gewichten sortierte Liste der Begriffe zurück, die mit prefix beginnen.
    # Sucht dabei zunächst binär die Wörter raus und sortiert sie anschließend nach ihren Gewichten.
    def match(self, prefix):
        match_list = []

        left = 0
        right = len(self.term_list) - 1
        while left <= right:
            center = left + (right - left) // 2

            # wenn prefix alphabetisch nach Wort kommt
            if self.term_list[center].word_is_smaller_then(prefix):
                # linke Schranke eins über center → nur noch rechte Hälfte zum Suchen
                left = center + 1
            # sonst
            else:
                # wenn prefix gleich Präfix mit gleicher Länge des Wortes ist
                if self.term_list[center].subword_equals_or_is_smaller_then(prefix, len(prefix)) == "equal":
                    # füge aktuelles Wort zu match_list hinzu
                    match_list += [self.term_list[center]]
                    n = 1
                    # laufe nach rechts bis Präfixe nicht mehr gleich
                    while right >= center + n and self.term_list[center + n].subword_equals_or_is_smaller_then(prefix, len(prefix)) == "equal":
                        # Wörter hinzufügen, solange Präfixe gleich
                        match_list += [self.term_list[center + n]]
                        n += 1

                    degr = -1
                    # laufe nach links bis Präfixe nicht mehr gleich
                    while self.term_list[center + degr].subword_equals_or_is_smaller_then(prefix, len(prefix)) == "equal":
                        # Wörter hinzufügen, solange Präfixe gleich
                        match_list += [self.term_list[center + degr]]
                        degr -= 1

                    break

                # sonst, rechte Schranke eins unter center → nur noch linke Hälfte zum Suchen
                right = center - 1

        # Sortierung der passenden Wörter nach Gewichten in umgekehrter Reihenfolge (höchstes Gewicht an 1. Stelle)
        match_list.sort(key=lambda e: e.weight, reverse=True)

        return match_list

    # -----------------------------------------------------------------------------------------
    # matches(prefix) gibt die Anzahl der Begriffe zurück, die mit prefix beginnen.
    # Es wird das gleiche Prinzip wie in match(prefix) angewandt nur ohne Sortierung am Ende
    # und nur Abspeicherung der Anzahl der Treffer.
    def matches(self, prefix):
        n = 0
        left = 0
        right = len(self.term_list)-1
        while left <= right:
            center = left + (right - left) // 2

            # wenn prefix alphabetisch nach Wort kommt
            if self.term_list[center].word_is_smaller_then(prefix):
                # linke Schranke eins über center → nur noch rechte Hälfte zum Suchen
                left = center + 1
            # sonst
            else:
                # wenn prefix gleich Präfix mit gleicher Länge des Wortes ist
                if self.term_list[center].subword_equals_or_is_smaller_then(prefix, len(prefix)) == "equal":
                    n += 1
                    # laufe nach rechts bis Präfixe nicht mehr gleich
                    while right >= center + n and self.term_list[center + n].subword_equals_or_is_smaller_then(prefix, len(prefix)) == "equal":
                        n += 1

                    degr = -1
                    # laufe nach links bis Präfixe nicht mehr gleich
                    while self.term_list[center + degr].subword_equals_or_is_smaller_then(prefix, len(prefix)) == "equal":
                        degr -= 1
                        n += 1

                    return n

                # sonst, rechte Schranke eins unter center → nur noch linke Hälfte zum Suchen
                right = center - 1

        # wenn kein Wort gefunden, gebe 0 zurück
        return 0

    # -----------------------------------------------------------------------------------------
    # len(...) gibt die Anzahl der in ... gespeicherten Begriffe zurück.
    def __len__(self):
        return len(self.term_list)

    # -----------------------------------------------------------------------------------------
    # str(...) gibt AutoComplete ... als String zurück.
    def __str__(self):
        return ''.join(str(term) for term in self.term_list)


# === Ende der Definition von AutoComplete ====================================================


# ---------------------------------------------------------------------------------------------
# Testfunktion
# Erstellt das AutoComplete-Objekt data mit txt-File dessen Name über die Kommandozeile eingelesen wurde,
# testet die match(prefix) Funktion mit "ya" als prefix aus
# und gibt dessen Ergebnis aus.
def test():
    filename = sys.argv[1]
    data = AutoComplete(filename)
    match_list = data.match("ya")
    for line in match_list:
        print(line, end="")


# ---------------------------------------------------------------------------------------------

if __name__ == '__main__':
    test()

# ---------------------------------------------------------------------------------------------
# python .\auto_complete.py ..\data\wiktionary.txt
#        4441190 yards
#        2925370 yard
#        1056080 yahweh
#         777685 yacht
#         709173 yankee
#         411943 yarn
#         404507 yale
#         399443 yawning
