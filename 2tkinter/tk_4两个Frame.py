from tkinter import *

def callback():
    var.set('哈哈哈,信了你的鬼!')


root = Tk()

frame1 = Frame(root)
frame2 = Frame(root)

var = StringVar()
var.set('点击下方按钮,开启新纪元!\n不点后悔一辈子!!!')

textLabel = Label(frame1,
                  textvariable=var,
                  justify=LEFT,
                  padx=10,
                  pady=10)
textLabel.pack(side=LEFT)

photo = PhotoImage(file='bd.gif')
imgLabel = Label(frame1, image=photo)
imgLabel.pack(side=RIGHT)

theButton = Button(frame2, text='点我,点我!!!', command=callback)
theButton.pack()

frame1.pack(padx=10, pady=10)
frame2.pack(padx=10, pady=10)

mainloop()
