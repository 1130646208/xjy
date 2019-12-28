from tkinter import *

def test(content):
    return content.isdigit()


def calc():
    a = int(v1.get())
    b = int(v2.get())
    v3.set(str(a + b))
    
root = Tk()

frame = Frame(root)
frame.pack(padx=10, pady=10)

v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
v3.set('0')
testCMD = frame.register(test)

#key判断test返回值,如果返回True则保留,如果返回假,则清除
e1 = Entry(frame, width=10, textvariable=v1, validate='key', \
           validatecommand=(testCMD, '%P')).grid(row=0, column=0)
Label(frame, text='+').grid(row=0, column=1)

e2 = Entry(frame, width=10, textvariable=v2, validate='key', \
           validatecommand=(testCMD, '%P')).grid(row=0, column=2)
Label(frame, text='=').grid(row=0, column=3)

e3 = Entry(frame, width=10, textvariable=v3, state='readonly').grid(row=0, column=4)

Button(frame, width=10, text='计算', command=calc).grid(row=1, column=2, pady=5)

mainloop()
