# adapted from https://knowpapa.com/text-editor/

import Tkinter
import ScrolledText # Because Tkinter textarea does not provide scrolling
#  abilities, we use this additional library
root = Tkinter.Tk(className=" ELEC 3225 Text Editor in Python")
textPad = ScrolledText.ScrolledText(root, width=50, height=25)
textPad.pack()
root.mainloop()