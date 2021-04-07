import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import re
from tkinter import messagebox
import re


root = tk.Tk()
root.title("Text Editor")

root.rowconfigure(0, minsize = 500, weight = 1)
root.columnconfigure(1, minsize = 800, weight = 1)


def open_file():
    filepath = askopenfilename(filetype = [("Text Files", ".txt"),("All Files", "*.*")])
    if not filepath:
        return
    text_field.delete("1.0", tk.END)
    with open(filepath) as newFile:
        text = newFile.read()
        text_field.insert(tk.END, text)
    root.title("Text Editor " + filepath)

def safe():
    filepath = asksaveasfilename(defaultextension = ".txt", filetype = [("text files", ".txt"), ("all files", "*.*")])
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = text_field.get("1.0", tk.END)
        output_file.write(text)


# option list fonts
option_list = ["Arial", "Calibri", "Times"]
def font(value):

    if value == "Arial":
        text_field["font"] = "Arial"
    elif value == "Calibri":
        text_field["font"] = "Calibri"
    elif value == "Times":
        text_field["font"] = value

# search
def search():



   text_field.tag_remove("found", "1.0", tk.END)

   text = testst.get()
   if text:
       idx = "1.0"

       while 1:
           idx = text_field.search(text, idx, nocase = 1, stopindex=END)

           if not idx:
               break

           lastidx = "%s+%dc" % (idx, len(text))

           text_field.tag_add("found", idx, lastidx)
           idx = lastidx
       text_field.tag_config("found", background = "yellow")









# set optionmenu var
variable = tk.StringVar()
variable.set("Times")
testst = tk.StringVar()

# widgets
b_frame = tk.Frame(root)
text_field = tk.Text(root, font=("Times New Roman", 12))

b_open = tk.Button(b_frame, text = "Open File", command = open_file, anchor = "w")
b_save = tk.Button(b_frame, text = "Save File", command = safe, anchor = "w")

b_fonts = tk.OptionMenu(b_frame, variable, *option_list, command = font)

b_search = tk.Button(b_frame, text = "Search", anchor = "w", command = search)
b_search_entry = tk.Entry(b_frame, textvariable = testst)


# config
b_fonts.configure(anchor = "w")

b_open.grid(row = 0, column = 0, sticky = "ew", padx = 5, pady = 5)
b_save.grid(row = 1, column = 0, sticky = "ew", padx = 5, pady = 5)

b_fonts.grid(row = 2, column = 0, sticky = "ew", padx = 5, pady = 5)

b_search.grid(row = 3, column = 0, sticky = "ew", padx = 5, pady = 5 )
b_search_entry.grid(row = 4, column = 0, sticky = "ew", padx = 5, pady = 5 )

b_frame.grid(row = 0, sticky = "ns")
text_field.grid(row = 0, column = 1, sticky = "nsew")






root.mainloop()