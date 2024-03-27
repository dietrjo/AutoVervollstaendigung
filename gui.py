import os
import sys
import tkinter as tk
from tkinter import ttk

current_dir = os.path.dirname(os.path.realpath(__file__))
module_dir = os.path.join(current_dir, 'auto_completer')
sys.path.append(module_dir)
from auto_completer.auto_complete import AutoComplete


class Gui:
    def __init__(self, app, data, k):
        self.app = app
        self.data = data
        self.k = k

        self.app.title("Auto Completer")
        self.app.geometry("800x500")

        search_bar = ttk.Frame(self.app)
        search_bar.grid(column=0, row=0, sticky="N, W, E")

        self.input_text = tk.StringVar()
        self.input_text.trace("w", lambda name, index, mode, new_input_text=self.input_text: self.on_input_change(
            new_input_text))
        search_input = ttk.Entry(master=search_bar, textvariable=self.input_text)
        search_input.grid(column=0, row=0)

        search_button = ttk.Button(master=search_bar, text="search", command=self.on_search)
        search_button.grid(column=1, row=0)

        self.result_list = tk.Listbox(master=self.app)
        self.result_list.grid(column=0, row=1, sticky="N, W, E, S")
        self.result_list.bind('<<ListboxSelect>>', self.on_list_item_select)

    def on_search(self):
        print(self.input_text.get())

    def on_input_change(self, new_input_text):
        self.result_list.delete(0, self.result_list.size())

        if new_input_text.get() != "":
            match_list = self.data.match(new_input_text.get())
            list_length = len(match_list) if len(match_list) < self.k else self.k

            for i in range(list_length):
                self.result_list.insert(i, match_list[i].word.strip())

    def on_list_item_select(self, event):
        if self.result_list.curselection():
            selected_index = self.result_list.curselection()[0]
            self.input_text.set(self.result_list.get(selected_index))


def test():
    filename = sys.argv[1]
    k = int(sys.argv[2])
    data = AutoComplete(filename)
    app = tk.Tk()
    Gui(app, data, k)
    app.mainloop()


if __name__ == '__main__':
    test()
