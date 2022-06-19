import tkinter as tk
from tkinter import filedialog

import main as ma

mainfile = ''
checkfile = ''


def upload_main_file():
    selectFile = tk.filedialog.askopenfilename()  # askopenfilename 1次上传1个；askopenfilenames1次上传多个
    entry1.insert(0, selectFile)


def upload_check_file():
    selectFile = tk.filedialog.askopenfilename()  # askopenfilename 1次上传1个；askopenfilenames1次上传多个
    entry2.insert(0, selectFile)


def select_output_file():
    selectFile = tk.filedialog.askdirectory()  # askopenfilename 1次上传1个；askopenfilenames1次上传多个
    entry3.insert(0, selectFile)


root = tk.Tk()

frm = tk.Frame(root)
frm.grid(padx='20', pady='30')
btn = tk.Button(frm, text='上传main文件', command=upload_main_file).grid(row=0, column=0, ipadx='3', ipady='3', padx='10', pady='20')
label1 = tk.Label(frm,text='需要核对的单号与供应商对应表，字段要求 number,supply').grid(row=1,column=0)
btn1 = tk.Button(frm, text='上传check文件', command=upload_check_file).grid(row=2, column=0, ipadx='3', ipady='3', padx='10', pady='20')
label2 = tk.Label(frm,text='需要核对的两列供应商组，字段要求 supply1,supply2').grid(row=3,column=0)
btn2 = tk.Button(frm, text='选择输出文件夹', command=select_output_file).grid(row=4, column=0, ipadx='3', ipady='3', padx='10', pady='20')
entry1 = tk.Entry(frm, width=40)
entry1.grid(row=0, column=1)
entry2 = tk.Entry(frm, width=40)
entry2.grid(row=2, column=1)
entry3 = tk.Entry(frm, width=40)
entry3.grid(row=4, column=1)

def outresult():
    ma.output(entry1.get(), entry2.get(), entry3.get())

btn3 = tk.Button(frm, text='生成结果', command=outresult)
btn3.grid(row=5, column=0, ipadx='30', ipady='3', padx='10', pady='20')

root.mainloop()
