from tkinter import *
import hashlib


import webbrowser

def show_arrow_cursor(event):
    text.config(cursor='arrow')

def show_xterm_cursor(event):
    text.config(cursor='xterm')

def click(event):
    webbrowser.open('http://www.baidu.com')

def getSig(contents):
    m = hashlib.md5(contents.encode())#先编码成二进制
    return m.digest()

def check():
    contents = text.get('1.0',END)
    if sig != getSig(contents):
        print('警告:内容被篡改!')

    else:
        print('内容正常!')

root = Tk()

text = Text(root, width=50, height=30)
text.pack()

text.insert(INSERT, '点我打开百度')
sig = getSig(text.get('1.0',END))

text.tag_add('link', '1.1')
text.tag_config('link', foreground='blue', underline=True)

text.tag_bind('link', '<Enter>', show_arrow_cursor)
text.tag_bind('link', '<Leave>', show_xterm_cursor)
text.tag_bind('link', '<Button-1>', click)

Button(root, text='检查内容.', command=check).pack()


mainloop()
