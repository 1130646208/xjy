from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import colorchooser

if messagebox.askokcancel('INFO', '打开文件?'):
    print('选择了:', filedialog.askopenfilename(defaultextension='.py', filetypes=[('PNG', '.png'),('GIF', '.gif')]))
    #自动加上默认后缀
    print('选择颜色:',colorchooser.askcolor())



mainloop()
