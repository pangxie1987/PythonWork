#encoding=utf-8
from tkinter import *
from tkinter.ttk import Treeview
import xlrd

class GUI(object):

    #
    # def gui(self):
    #     self.root=Tk()
    #     self.root.title = 'GUI'
    #     self.root.geometry('1000x800')
    #     self.root.resizable(width=True, height=True)
    #     self.root.mainloop()
    #
    # def frame(self):
    #     self.frame01=Frame(self.root,width=1000,heigth=300)
    #     self.frame01.grid(row=0, column=0,rowspan=10,columnspan=0)
    #     self.frame02 = Frame(self.root, width=1000, heigth=300)
    #     self.frame02.grid(row=11, column=0, rowspan=11,columnspan=0)
    #
    # def button(self):
    #     self.button01=Button(self.frame01,text='获取',width=20,heigth=10,command='')
    #     self.button01.grid(row=0,rowspan=5,column=0,columnspan=5)
    #
    # def lable(self):
    #     self.lable01=Label(self.frame01,width=40,heigth=30)
    #     self.lable01.grid(row=6,column=6,rowspan=10)
    #
    # def tree(self):
    #     self.tree=Treeview(width=1000,heigth=200,columns=('a','b','c','d'))
    #     self.tree.column('编号')
    #     self.tree.column('A')
    #     self.tree.column('B')
    #     self.tree.column('C')

    def __init__(self):
        self.root = Tk()
        self.root.title('GUI')
        self.root.geometry('1000x800')
        self.root.resizable(width=True, height=True)

        self.frame01 = Frame(self.root, width=1000, height=600)
        self.frame01.grid(row=0, column=0, rowspan=2, columnspan=1)
        self.frame02 = Frame(self.root, width=1000, height=300)
        self.frame02.grid(row=2, column=0, rowspan=10, columnspan=1)
        self.frame02.grid_propagate(0)

        self.button01 = Button(self.frame01, text='获取',bg='green', fg='red', width=10, height=3, command='')
        self.button01.grid(row=0, column=0)

        self.button02 = Button(self.frame01,text='退出',bg='red', width=10, height=3, command=self.root.quit  )
        self.button02.grid(row=1, column=0)

        self.update_rows=StringVar()    #声明Excel行数
        self.lable01 = Label(self.frame01, width=40, height=6,textvariable=self.update_rows,bg='yellow')
        self.lable01.grid(row=2, column=0)
        #调用获取行数的方法
        self.get_rows()


        #创建列表树
        self.tree = Treeview(self.frame02,show='headings', columns=('a', 'b', 'c', 'd'))
        self.tree.column('a', width=100, anchor='center')
        self.tree.column('b', width=200, anchor='center')
        self.tree.column('c', width=200, anchor='center')
        self.tree.column('d', width=200, anchor='center')
        self.tree.heading('a', text='编号')
        self.tree.heading('b', text='A')
        self.tree.heading('c', text='B')
        self.tree.heading('d', text='C')
        self.tree.grid(row=6, column=6,sticky=NSEW)

        self._ExcelData()

        #创建滚动条

        self.vbar = Scrollbar(self.frame02, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.vbar.set)
        self.vbar.grid(row=6, column=7, sticky=NS)

    #获取Excel中的数据，并插入到tree表格中
    def _ExcelData(self):
        self.table=xlrd.open_workbook('TestData.xlsx')
        self.sheet=self.table.sheet_by_index(0)
        self.rows=self.sheet.nrows
        self.lable01.after(self.rows)
        self.cols=self.sheet.ncols
        for i in range(self.rows):
            self.tree.insert('',i,values=(self.sheet.row_values(i)))
        return self.rows

    #获取Excel行数的方法，用于更新lable中的数据
    def get_rows(self):
        self.table = xlrd.open_workbook('TestData.xlsx')
        self.sheet = self.table.sheet_by_index(0)
        self.update_rows.set(self.sheet.nrows)
        self.lable01.after(500,self.get_rows)

def main():
    mygui=GUI()
    mygui.root.mainloop()

if __name__=='__main__':

    main()