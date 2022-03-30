import tkinter as tk
from tkinter import filedialog

from file_generator import generate_files_from_csv


class Gui:
    _filename = None

    @staticmethod
    def generate_root():
        root = tk.Tk()
        root.title("Chan File Generator")
        return root 

    @staticmethod
    def create_messages(parent):
        message = tk.Text(parent)
        message.insert(tk.END, "Chan File Generator")
        message.insert(tk.END, "\nPlease press the button")
        message.tag_config("center", justify="center")
        message.tag_add('center', "1.0", "3.0")
        message.pack()

    @staticmethod
    def create_button(parent, command):
        button = tk.Button(parent, text="Generate Files", justify=tk.CENTER, command=command)
        button.pack()

    @staticmethod
    def show_file_dialog():
        Gui._filename = filedialog.askopenfilename(initialdir="./", filetypes=[("csv files", "*.csv")])

    @staticmethod
    def generate_files():
        generate_files_from_csv(Gui._filename)

    @staticmethod
    def run_main_loop():
        root = Gui.generate_root()
        Gui.create_messages(root)
        Gui.create_button(root, Gui.generate_files)
        Gui.create_button(root, Gui.show_file_dialog)
        root.mainloop()
