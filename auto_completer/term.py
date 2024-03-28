# ---------------------------------------------------------------------------------------------
# term.py
# ---------------------------------------------------------------------------------------------
# Implementierung des Datentyps Term als Klasse mit den Operationen
#   Term(weight, word)                          erstellt Term-Objekt mit word und zugehörigem weight
#   .word_is_smaller_then(other_word)           gibt zurück, ob word aus Objekt alphabetisch kleiner als other_word ist
#   .weight_is_smaller_then(other_weight)       gibt zurück, ob weight aus Objekt kleiner als other_weight ist
#   .subword_equals_or_is_smaller_then(other_word, num_first_letters)
#                                               gibt zurück, ob Präfix mit num_first_letters Buchstaben von word aus
#                                               Objekt kleiner als Präfix mit num_first_letters Buchstaben von
#                                               other_word ist
#   str(...)                                    gibt Term ... als String zurück
# ---------------------------------------------------------------------------------------------


# === Definition der Klasse Term ==============================================================

class Term:

    # -----------------------------------------------------------------------------------------
    # Konstruktor
    def __init__(self, weight, word):
        # wenn weight negativ → Error
        if weight < 0:
            raise ValueError(f'Error! Weight of {word} is not positive.')
        self.weight = weight
        self.word = word

    # -----------------------------------------------------------------------------------------
    # word_is_smaller_then(other_word) gibt True zurück, wenn word aus Objekt alphabetisch kleiner als other_word ist.
    # Sonst False.
    def word_is_smaller_then(self, other_word):
        return self.word < other_word

    # -----------------------------------------------------------------------------------------
    # weight_is_smaller_then(other_weight) gibt True zurück, wenn weight aus Objekt kleiner als other_weight ist.
    # Sonst False.
    def weight_is_smaller_then(self, other_weight):
        return self.weight < other_weight

    # -----------------------------------------------------------------------------------------
    # subword_equals_or_is_smaller_then(other_word, num_first_letters) gibt True zurück, wenn Präfix mit
    # num_first_letters Buchstaben von word aus Objekt kleiner als Präfix mit num_first_letters Buchstaben von
    # other_word ist.
    # Wenn beide Präfixe gleich sind, wird "equal" zurückgegeben.
    # Wenn beides nicht zutrifft, False.
    def subword_equals_or_is_smaller_then(self, other_word, num_first_letters):
        if self.word[0:num_first_letters] == other_word[0:num_first_letters]:
            return "equal"
        return self.word[0:num_first_letters] < other_word[0:num_first_letters]

    # -----------------------------------------------------------------------------------------
    # str(...) gibt Term ... als String zurück.
    def __str__(self):
        return f'{self.weight:>14} {self.word}'


# === Ende der Definition von Term ============================================================


# ---------------------------------------------------------------------------------------------
# Testfunktion
# Erstellt drei unterschiedliche Terme und vergleicht diese entsprechend, dass alle Funktionen getestet werden.
def test():
    term1 = Term(5627187200, "the")
    term2 = Term(879975500, "his")
    term3 = Term(109051000, "these")

    print(term1)
    print(term2)
    print(term3)

    print(f'\n{term1.word_is_smaller_then(term2.word)} (has to be: False)')
    print(f'{term1.weight_is_smaller_then(term2.weight)} (has to be: False)\n')

    print(f'{term1.subword_equals_or_is_smaller_then(term3.word, 4)} (has to be: True)')
    print(f'{term1.subword_equals_or_is_smaller_then(term3.word, 3)} (has to be: equal)')


# ---------------------------------------------------------------------------------------------

if __name__ == '__main__':
    test()

# ---------------------------------------------------------------------------------------------
# python .\term.py
#     5627187200 the
#      879975500 his
#      109051000 these
#
# False (has to be: False)
# False (has to be: False)
#
# True (has to be: True)
# equal (has to be: equal)
