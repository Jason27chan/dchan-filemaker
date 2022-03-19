import tkinter as tk


class Gui:
    @staticmethod
    def run_main_loop():
        root = tk.Tk()

        root.title("Chan File Generator")

        container = tk.Frame(root)
        container.pack()

        message = tk.Text(container)
        message.insert(tk.END, "Chan File Generator")
        message.insert(tk.END, "\nPlease press the button")
        message.tag_config("center", justify="center")
        message.tag_add('center', "1.0", "3.0")
        message.pack()

        button = tk.Button(container, text="Generate Files", justify=tk.CENTER, command=generate_files_from_csv)
        button.pack()

        root.mainloop()
