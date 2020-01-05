from tkinter import *

root = Tk()

sb = Scrollbar(root)
sb.pack(side=RIGHT, fill=Y)


lb = Listbox(root, yscrollcommand=sb.set)
for i in range(100):
    lb.insert(END, i)

lb.pack(side=LEFT, fill=BOTH)


mainloop()
