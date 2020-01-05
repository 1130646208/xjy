from tkinter import *

root = Tk()
w1 = Message(root, text='这是一则消息', width=100)
w1.pack()

w2 = Message(root, text='这是一则消息\n,长长长长长长长长长长长长', width=100)
w2.pack()

mainloop()
