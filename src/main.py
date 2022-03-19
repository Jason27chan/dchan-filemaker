import tkinter
from csv import reader
import tkinter as tk
import os

print("running main")
def generate_files_from_csv():
    # open file
    with open("testdata.csv", "r") as my_file:
        # pass the file object to reader()
        file_reader = reader(my_file)

        # do this for all the rows
        for row in file_reader:
            # print the row
            print(row)

            if len(row) > 0:
                if not os.path.exists('./data'):
                    os.mkdir('data')
                prospective_file_name = row[0]
                new_file = open(f'./data/{prospective_file_name}.csv', 'w')
                new_file.close()


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

button = tk.Button(container, text="Generate Files", justify=tkinter.CENTER, command=generate_files_from_csv)
button.pack()

root.mainloop()
