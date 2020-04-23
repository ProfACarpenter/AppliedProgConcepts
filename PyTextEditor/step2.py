# adapted from https://knowpapa.com/text-editor/

import Tkinter
from Tkinter import Menu
import tkMessageBox
import ScrolledText

root = Tkinter.Tk(className=" ELEC 3225 Text Editor in Python")
textPad = ScrolledText.ScrolledText(root, width=50, height=25) # creates text area

# create a menu

def placeholder():
    tkMessageBox.showinfo("PyText", "This is a placeholder item and will be replaced later")

menu = Menu(root)
# configuration for a menu bar
root.config(menu=menu)

# setup for the filemenu
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)

# drop down items for the commands within the file menu
filemenu.add_command(label="New", command=placeholder)
filemenu.add_command(label="Open", command=placeholder)
filemenu.add_command(label="Save", command=placeholder)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=placeholder)

# setup for edit menu
editmenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editmenu)

# drop down items for the commands within the edit menu
editmenu.add_command(label="Undo", command=placeholder)
editmenu.add_command(label="Redo", command=placeholder)
editmenu.add_separator()
editmenu.add_command(label="Copy", command=placeholder)
editmenu.add_command(label="Cut", command=placeholder)
editmenu.add_command(label="Paste", command=placeholder)

# setup for help menu
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)

# drop down items for the commands within the help menu
helpmenu.add_command(label="User help", command=placeholder)
helpmenu.add_command(label="About", command=placeholder)
# end of menu creation

textPad.pack()
root.mainloop()