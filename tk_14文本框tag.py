from tkinter import *

root = Tk()

text = Text(root, width=30, height=5)
text.pack()

text.insert(INSERT, '路漫漫其修远兮,')

text.tag_add('tag1', '1.1', '1.3', '1.5')
text.tag_config('tag1', background='yellow', foreground='red')
#新的样式会覆盖旧的样式.tag_raise('tag1') tag_lower('tag2')改变tag优先级

mainloop()
