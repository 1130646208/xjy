from tkinter import *

root = Tk()

text = Text(root, height=10, width=20)
text.pack()

text.insert(INSERT, '吃葡萄不吐葡萄皮,不吃葡萄倒吐葡萄皮.')


def getIndex(text, index):
    return tuple(map(int, str.split(text.index(index), '.')))
#map(int,[]):将字符串列表转化成int列表

start = '1.0'
while True:
    pos = text.search('吃', start, stopindex=END)
    if not pos:
        break
    
    print('找到啦,位置是:', getIndex(text, pos))
    start = pos + '+1c'
    


mainloop()
