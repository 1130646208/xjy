from tkinter import *

def test():
    print('作者:杜甫','作品:登高',sep='\n',end='\n')
    text.image_create(END, image=photo)

root = Tk()

text = Text(root, width=100, height=5)
text.pack()
text.insert(INSERT, '万里悲秋常作客,\n')
text.insert(END, '百年多病独登台.\n')

b = Button(text, text='点击百度一下', command=test)
text.window_create(INSERT, window=b)

photo = PhotoImage(file='bd.gif')



mainloop()
