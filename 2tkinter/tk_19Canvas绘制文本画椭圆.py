from tkinter import *

root = Tk()

w = Canvas(root, width=200, height=100)
w.pack()

line1 = w.create_line(0, 0, 50, 25, fill='green', width=3)
line2 = w.create_line(200, 0, 150, 25, fill='green', width=3)
line3 = w.create_line(0, 100, 50, 75, fill='green')
line4 = w.create_line(200, 100, 150, 75, fill='green')
rect1 = w.create_rectangle(50, 25, 150, 75, fill='yellow')

w.create_text(100, 50, text='WSX')
w.create_oval(50, 25, 150, 75)

mainloop()
