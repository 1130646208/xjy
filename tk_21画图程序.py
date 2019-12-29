#bug:cannot change color
from tkinter import *
import random as r

root = Tk()

w = Canvas(root, width=400, height=200)
w.pack()

currentColor='red'
def setColor():
    color = ['red', 'pink', 'black', 'blue', 'red']
    currentColor = r.choice(color)
    print(currentColor)
    return currentColor


def paint(event):
    x1, y1 = (event.x), (event.y)
    x2, y2 = (event.x+1), (event.y+1)
    w.create_line(x1, y1, x2, y2, fill=currentColor)

w.bind('<B1-Motion>', paint)

Button(root, text='更改颜色', command=setColor).pack()
Label(root, text='当前颜色:'+currentColor).pack()



mainloop()
