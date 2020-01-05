from tkinter import *

root = Tk()

photo = PhotoImage(file='cat_500_600.gif')
theLabel = Label(root,
                 text='路漫漫其修远兮,吾将上下而求索',
                 justify=LEFT,
                 image=photo,
                 compound=CENTER,
                 font=('华文彩云',20,BOLD),
                 fg='white')
theLabel.pack()

mainloop()

