from tkinter import *

root = Tk()

options = [
    '1',
    '2',
    '3',
    '4']

v1 = StringVar()
v1.set(options[0])

w = OptionMenu(root, v1, *options)#不加星号会当成一个选项
w.pack()



mainloop()

