from tkinter import *

root = Tk()

w = Spinbox(root, from_=0, to=5)
w.pack()

w2 = Spinbox(root, values=('王昭君', '西施', '杨禹皇'))
w2.pack()


mainloop()
