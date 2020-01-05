from tkinter import *

root = Tk()

def callback():
    print('OKOKOK!!!')


photo = PhotoImage(file='bd.gif')
Label(root, image=photo).pack()


Button(root, text='CLICK ME', command=callback).place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.5, anchor=CENTER)#rel:相对于父组件的位置,anchor:组件锚点

#注意,pack和place可以混用,pack和grid不可混用

mainloop()
