from tkinter import *


def undo():
    text.edit_undo()
    
def callback(event):#绑定事件
    text.edit_separator()
    

root = Tk()

text = Text(root, height=10, width=20, undo=True, autoseparators=False)#最后一个参数,手动设置完整操作的标志,默认输入一句话或者一个段落是一次完整操作
text.pack()

text.insert(INSERT, '吃葡萄不吐葡萄皮,不吃葡萄倒吐葡萄皮.')

Button(text='撤销', command=undo).pack()

text.bind('<Key>', callback)

mainloop()
