from tkinter import *

def test():
    if e1.get() == '小甲鱼':
        print('正确')
        return True
    else:
        print('错误')
        e1.delete(0, END)
        return False

def fail():
    print('invalidcommand=fail')


root = Tk()


Label(root, text='作品').grid(row=0,column=0)
Label(root, text='作者').grid(row=1,column=0)

v1 = StringVar()
v2 = StringVar()
#validate:
#invalidacommand:验证失败时调用
#validatecommand:验证时调用
e1 = Entry(root, textvariable=v1, validate='focusout', validatecommand=test, invalidcommand=fail)
e2 = Entry(root, textvariable=v2, show='*')
e1.grid(row=0, column=1, padx=10, pady=5)
e2.grid(row=1, column=1, padx=10, pady=5)

def show():
    print('作品<<%s>>'%e1.get())
    print('作者<<%s>>'%e2.get())

Button(root, text='获取信息', width=10, command=show)\
             .grid(row=2, column=0,sticky=W, padx=10, pady=5)

Button(root, text='退出', width=10, command=root.quit)\
             .grid(row=2, column=1,sticky=E, padx=10, pady=5)

mainloop()
