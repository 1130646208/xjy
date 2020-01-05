from tkinter import *
import math

root = Tk()

w = Canvas(root, width=200, height=200, background='red')
w.pack()

R = 50
x0 = 100
y0 = 100
#画法1
#x = [x0 + R * math.cos(2*math.pi*i/5) for i in range(5)]
#y = [y0 + R * math.sin(2*math.pi*i/5) for i in range(5)]
#画法2

x = [x0 + R * math.cos(2*math.pi*i*2/5) for i in range(5)]
y = [y0 + R * math.sin(2*math.pi*i*2/5) for i in range(5)]

points = [ (x[i], y[i]) for i in range(5)]


#画法1
#line1 = w.create_line(x[0], y[0], x[2], y[2], fill='green', width=3)
#line2 = w.create_line(x[0], y[0], x[3], y[3], fill='green', width=3)
#line3 = w.create_line(x[1], y[1], x[4], y[4], fill='green', width=3)
#line4 = w.create_line(x[1], y[1], x[3], y[3], fill='green', width=3)
#line5 = w.create_line(x[2], y[2], x[4], y[4], fill='green', width=3)

#画法2
w.create_polygon(points, outline='green', fill='yellow')


mainloop()
