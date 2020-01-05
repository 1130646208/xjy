from tkinter import *

root = Tk()

group = LabelFrame(root, text='请选择:',padx=5, pady=5)
group.pack(padx=10, pady=10)

GIRLS = ['西施', '貂蝉', '王昭君', '杨玉环']

v = []

for girl in GIRLS:
    v.append(IntVar())
    b = Checkbutton(root, text=girl, variable=v[-1])
    b.pack(anchor=W)#N E S W NE...

z = IntVar()

Radiobutton(group, text='One', variable=z, value=1, indicatoron=False).pack(anchor=W)
Radiobutton(group, text='Two', variable=z, value=2).pack(anchor=W)
Radiobutton(group, text='Three', variable=z, value=3).pack(anchor=W)
Radiobutton(group, text='Four', variable=z, value=4).pack(anchor=W)

mainloop()
