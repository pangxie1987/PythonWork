import time
from tkinter import *
from tkinter.ttk import Treeview

def tick():

    global time1

    time2=time.strftime('%H:%M:%S')

    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    clock.after(200,tick)


def treetime():
    n=1
    if time1!='0':

        tree.insert('',1,values=[1,time1])
        tree.after(1000,treetime)

gui=Tk()
time1=''

# gui.geometry('100x20')
# gui.resizable(width=True,height=True)

clock=Label(gui,font=('times',20,'bold'),bg='green')
clock.grid(row=0,column=0)

tree=Treeview(gui,show='headings',columns=('a','b'))
tree.heading('a',text='序号')
tree.heading('b',text='时间')
tree.grid(row=1,column=0,sticky=NSEW)
tick()
treetime()

gui.mainloop()