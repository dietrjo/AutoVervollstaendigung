# ---------------------------------------------------------------------------------------------
# test.py
# ---------------------------------------------------------------------------------------------
# Testprogramm zum Testen der Auto-Completer-Funktionen
#   .run(data, k)   bekommt Daten aus txt File und k übergeben und gibt Ergebnisse
#                   der Auto-Vervollständigung zum entsprechenden User Input aus.
# ---------------------------------------------------------------------------------------------

import sys
from auto_complete import AutoComplete


# ---------------------------------------------------------------------------------------------
# run(data, k) bekommt Daten aus txt File (data) und Anzahl der auszugebenden Wörter (k) übergeben.
# Wartet dann auf Eingabe des Users und führt dieser als Prefix die match Funktion von der Klasse AutoComplete aus.
# Gibt dann schließlich die am höchsten gewichteten k-Einträge des Ergebnisses aus.
# Dies wird in einer Schleife ausgeführt bis das Programm manuell abgebrochen wird.
def run(data, k):
    while True:
        prefix = input()
        match_list = data.match(prefix)
        repeats = len(match_list) if len(match_list) < k else k
        for i in range(repeats):
            print(match_list[i], end="")


# ---------------------------------------------------------------------------------------------
# Hauptprogramm
# Liest file von txt Datei mit Daten und k von der Kommandozeile ein,
# erzeugt Objekt data von AutoComplete und ruft run mit data und k auf.
def main():
    file = sys.argv[1]
    k = int(sys.argv[2])
    data = AutoComplete(file)

    run(data, k)


# ---------------------------------------------------------------------------------------------

if __name__ == '__main__':
    main()

# ---------------------------------------------------------------------------------------------
# python .\test.py ..\data\wiktionary.txt 5
# auto
#         619695 automobile
#         424997 automatic
# comp
#       13315900 company
#        7803980 complete
#        6038490 companion
#        5205030 completely
#        4481770 comply
# the
#     5627187200 the
#      334039800 they
#      282026500 their
#      250991700 them
#      196120000 there
#
# python .\test.py ..\data\cities.txt 7
# M
#       12691836 Mumbai, India
#       12294193 Mexico City, Distrito Federal, Mexico
#       10444527 Manila, Philippines
#       10381222 Moscow, Russia
#        3730206 Melbourne, Victoria, Australia
#        3268513 Montréal, Quebec, Canada
#        3255944 Madrid, Spain
# Al M
#         431052 Al Maḩallah al Kubrá, Egypt
#         420195 Al Manşūrah, Egypt
#         290802 Al Mubarraz, Saudi Arabia
#         258132 Al Mukallā, Yemen
#         227150 Al Minyā, Egypt
#         128297 Al Manāqil, Sudan
#          99357 Al Maţarīyah, Egypt
