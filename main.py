# ---------------------------------------------------------------------------------------------
# main.py
# ---------------------------------------------------------------------------------------------
# Hauptprogramm der Auto-Vervollständigung Anwendung
#   .main()     Hauptfunktion
# ---------------------------------------------------------------------------------------------

import os
import sys
import ttkbootstrap as ttk
from gui import Gui
# Hinweis: ohne folgende Zeilen hat import nicht funktioniert
current_dir = os.path.dirname(os.path.realpath(__file__))
module_dir = os.path.join(current_dir, 'auto_completer')
sys.path.append(module_dir)
from auto_completer.auto_complete import AutoComplete


# ---------------------------------------------------------------------------------------------
# Hauptfunktion
# Liest filename von txt Datei mit Daten und k von der Kommandozeile ein,
# erzeugt Objekt data von AutoComplete und Objekt app von ttk.Window,
# ruft Gui damit auf und startet die app.
def main():
    filename = sys.argv[1]
    k = int(sys.argv[2])
    data = AutoComplete(filename)

    # themename "darkly" von ttkbootstrap als vordefiniertes Style-Paket
    app = ttk.Window(themename="darkly")
    Gui(app, data, filename, k)
    app.mainloop()


# ---------------------------------------------------------------------------------------------

if __name__ == '__main__':
    main()

# ---------------------------------------------------------------------------------------------
# python .\main.py .\mutable_data\wiktionary.txt 10
#
# python .\main.py .\mutable_data\cities.txt 15
