# ---------------------------------------------------------------------------------------------
# gui.py
# ---------------------------------------------------------------------------------------------
# Implementierung des GUI als Klasse mit den Operationen
#   Gui(app, data, filename, k)         erstellt grundlegende Struktur der grafischen Oberfläche
#   .on_search()                        Wort wird "gesucht" → Änderung der Gewichte bzw. Hinzufügen von Einträgen
#   .on_input_change(new_input_text)    händeln der Eingabeänderung → neue match-Suche, neue Anzeigeliste
#   .on_list_item_select(event)         händeln der Auswahl eines Wortes → Eingabeänderung
# ---------------------------------------------------------------------------------------------

import tkinter as tk
import ttkbootstrap as ttk
import shutil
import sys
import os
# Hinweis: ohne folgende Zeilen hat import nicht funktioniert
current_dir = os.path.dirname(os.path.realpath(__file__))
module_dir = os.path.join(current_dir, 'auto_completer')
sys.path.append(module_dir)
from auto_completer.auto_complete import AutoComplete


# === Definition der Klasse Gui ===============================================================

class Gui:

    # -----------------------------------------------------------------------------------------
    # Konstruktor
    # Anlegen aller GUI-Elemente und Konfiguration dieser.
    def __init__(self, app, data, filename, k):
        # speichere die über Konstruktor übergebenen Werte als Klassenattribute ab
        self.app = app
        self.data = data
        self.filename = filename
        self.k = k

        # konfiguriere Titel und Fenstergröße
        app.title("Auto Completer")
        app.geometry("500x300")

        # erstelle alles umfassenden Mainframe (umfasst komplettes Fenster und das auch bei manueller Größenänderung)
        main_frame = ttk.Frame(app)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # erstelle Suchleisten-Frame mit Input-Feld und Button als Kindern (parent=main_frame, umfasst komplette Zeile)
        search_bar = ttk.Frame(main_frame)
        search_bar.pack(fill="x", pady=(0, 12))

        # Klassenvariable für in Input-Feld eingegebenen Text
        self.input_text = tk.StringVar()
        # bei Änderung der Eingabe wird on_input_change mit neuer Eingabe als Attribut ausgeführt
        self.input_text.trace("w", lambda name, index, mode, new_input_text=self.input_text: self.on_input_change(
            new_input_text))
        # erstelle Input-Feld mit verbundener Textvariable (parent=search_bar, linksbündig)
        search_input = ttk.Entry(search_bar, textvariable=self.input_text, width=40)
        search_input.pack(side="left")

        # erstelle Button mit Text "Search" und bei Click auszuführender Funktion on_search
        # (parent=search_bar, linksbündig)
        search_button = ttk.Button(search_bar, text="Search", command=self.on_search)
        search_button.pack(side="left", padx=(10, 0))

        # erstelle Ergebnis-Frame mit Wörterliste und Scrollbar
        # (parent=main_frame, umfasst komplettes, restliches Fenster und das auch bei manueller Größenänderung)
        result_frame = ttk.Frame(main_frame)
        result_frame.pack(fill="both", expand=True)

        # erstelle Wörterliste (parent=result_frame, linksbündig,
        # umfasst kompletten restlichen Frame und das auch bei manueller Größenänderung)
        self.result_list = tk.Listbox(result_frame, width=50)
        self.result_list.pack(side="left", fill="both", expand=True)

        # erstelle vertikale, mit Wörterliste verknüpfte Scrollbar
        # (parent=result_frame, rechtsbündig, füllt gesamte Spalte im Frame)
        scrollbar = ttk.Scrollbar(result_frame, orient=tk.VERTICAL, command=self.result_list.yview)
        scrollbar.pack(side="right", fill="y")
        self.result_list.config(yscrollcommand=scrollbar.set)

        # wenn Wort in Wörterliste angeklickt wird, wird on_list_item_select ausgeführt
        self.result_list.bind('<<ListboxSelect>>', self.on_list_item_select)

    # -----------------------------------------------------------------------------------------
    # on_search() wird durch das Anklicken der Suche ausgeführt.
    # Zunächst werden der File zum Lesen und ein temporärer File zum Schreiben geöffnet/ erstellt.
    # Bei der Zeile mit dem Eingabewort wird nun eine 1 dazuaddiert und der Rest wird kopiert.
    # Wenn das Wort noch nicht vorhanden ist, wird ein neuer Eintrag mit dem Wort und dem Gewicht 1 angelegt.
    # Zum Schluss wird der ursprüngliche File durch den temporären File überschrieben, die Eingabe wird geleert
    # und die Daten werden neu angefordert.
    def on_search(self):
        if self.input_text.get().strip() != "":
            filedata = open(self.filename, 'r', encoding='utf-8')
            temp_filename = self.filename + ".temp"
            new_filedata = open(temp_filename, 'w', encoding='utf-8')

            found = False
            for line in filedata:
                if not found and line[15:].strip() == self.input_text.get():
                    new_number = int(line[:14]) + 1
                    line = f'{new_number:>14}	{line[15:]}'
                    found = True
                new_filedata.write(line)

            if not found:
                new_filedata.write(f'{1:>14}	{self.input_text.get()}\n')

            filedata.close()
            new_filedata.close()

            shutil.move(temp_filename, self.filename)
            self.input_text.set("")
            self.data = AutoComplete(self.filename)

    # -----------------------------------------------------------------------------------------
    # on_input_change(new_input_text) entfernt alle Wörter aus der Ergebnisliste,
    # führt die match-Suche mit der neuen Eingabe aus
    # und fügt die ersten k Wörter des Ergebnisses der Ergebnisliste hinzu
    def on_input_change(self, new_input_text):
        self.result_list.delete(0, tk.END)

        if new_input_text.get() != "":
            match_list = self.data.match(new_input_text.get())
            list_length = min(len(match_list), self.k)

            for i in range(list_length):
                self.result_list.insert(tk.END, match_list[i].word.strip())

    # -----------------------------------------------------------------------------------------
    # on_list_item_select(event) ersetzt Wort von Suchleiste mit in Wörterliste angeklicktem Wort
    def on_list_item_select(self, event):
        if self.result_list.curselection():
            selected_index = self.result_list.curselection()[0]
            self.input_text.set(self.result_list.get(selected_index))


# === Ende der Definition von Gui =============================================================
