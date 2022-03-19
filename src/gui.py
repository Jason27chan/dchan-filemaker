import tkinter as tk

from src.file_generator import generate_files_from_csv


class Gui:
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
    def run_main_loop():
        root = tk.Tk()
        root.title("Chan File Generator")
        Gui.create_messages(root)
        Gui.create_button(root, generate_files_from_csv)
        root.mainloop()
