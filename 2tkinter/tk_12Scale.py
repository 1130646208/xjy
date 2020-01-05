from tkinter import *

def show():
    print(s1.get(), s2.get())

root = Tk()

s1 = Scale(root, from_=0, tickinterval=5, resolution=5, to=40, length=200)
s1.pack()

s2 = Scale(root, from_=0, tickinterval=20, resolution=10, to=200, length=600, orient=HORIZONTAL)
s2.pack()

Button(root, text='获取位置', command=show).pack()


mainloop()
