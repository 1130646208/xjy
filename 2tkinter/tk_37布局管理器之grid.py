from tkinter import *

root = Tk()

photo = PhotoImage(file='bd.gif')
Label(root, image=photo).grid(row=2, column=0, columnspan=2, padx=8, pady=8)

Label(root, text='NAME').grid(row=0, sticky=W)
Label(root, text='PASS').grid(row=1, sticky=W)

Entry(root).grid(row=0, column=1)
Entry(root, show='.').grid(row=1, column=1)

Button(root, text='SUBMIT').grid(row=0, column=3,rowspan=2)

mainloop()
