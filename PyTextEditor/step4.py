# adapted from https://knowpapa.com/text-editor/
# and https://gist.github.com/Enrix835/115589

import Tkinter
from Tkinter import Menu
import tkFileDialog
import tkMessageBox
import ScrolledText

root = Tkinter.Tk(className=" ELEC 3225 Text Editor in Python")
textPad = ScrolledText.ScrolledText(root, width=50, height=25) # creates text area

# create a menu
def newFile():
    if tkMessageBox.askokcancel("New", "Do you really want delete your work?"):
        file.close()
        file.open()

def openFile():
    file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Select a file')
    if file != None:
        contents = file.read()
        textPad.insert('1.0',contents)
        file.close()

def saveFile():
    file = tkFileDialog.asksaveasfile(mode='w')
    if file != None:
    # slice off the last character from get, as an extra return is added
        data = self.textPad.get('1.0', END+'-1c')
        file.write(data)
        file.close()
        
def exit():
    if tkMessageBox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()

def about():
    label = tkMessageBox.showinfo("About", "Text editor made for ELEC 3225 GUI Exercise")

# edit menu
def cut():
    try:
        textPad.clipboard_clear()
        textPad.clipboard_append(textPad.selection_get()) 
        textPad.delete("sel.first", "sel.last")
    except:
        tkMessageBox.showerror("Error","Nothing to cut")

def copy():
    try:
        textPad.clipboard_clear()
        textPad.clipboard_append(textPad.selection_get()) 
    except:
        tkMessageBox.showerror("Error","Nothing to copy")

def paste():
    try:
        text = textPad.clipboard_get()
        textPad.insert('insert', text)
    except:
        tkMessageBox.showerror("Error","Nothing to paste")

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
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit)

# setup for edit menu
editmenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editmenu)

# drop down items for the commands within the edit menu
editmenu.add_command(label="Undo", command=placeholder)
editmenu.add_command(label="Redo", command=placeholder)
editmenu.add_separator()
editmenu.add_command(label="Copy", command=copy)
editmenu.add_command(label="Cut", command=cut)
editmenu.add_command(label="Paste", command=paste)

# setup for help menu
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)

# drop down items for the commands within the help menu
helpmenu.add_command(label="User help", command=placeholder)
helpmenu.add_command(label="About", command=placeholder)
# end of menu creation

textPad.pack()  # makes the text area
root.mainloop()
