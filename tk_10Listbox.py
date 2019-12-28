from tkinter import *

root = Tk()

theLB = Listbox(root, selectmode=BROWSE, height=3)#SINGLE,BROWSE,MULTIPLE,EXTENED,height:设置显示行数
theLB.pack()

for item in ['王双星', '冯越', '冯双星', '王越']:
    theLB.insert(END, item)

theButton = Button(root, text='删除', command=lambda x=theLB:x.delete(ACTIVE))
theButton.pack()


mainloop()
