from tkinter import *
from tkinter import ttk
from Dbconnect import DBConnect

dbconnect = DBConnect()

class ListStudent:

    def __init__(self):
        self._root=Tk()
        self._dbconnect = DBConnect()
        tv=ttk.Treeview(self._root)
        tv.pack()
        tv.heading('#0',text='ID')
        tv.configure(column=('#Name','#Graduate'))
        tv.heading('#Name',text='Name')
        tv.heading('#Graduate',text='Graduate')
        cursor=self._dbconnect.ListRequest()
        for row in cursor:
            tv.insert('','end','#{}'.format(row['ID']),text=row['ID'])
            tv.set('#{}'.format(row['ID']),'#Name',row['Name'])
            tv.set('#{}'.format(row['ID']), '#Graduate', row['Graduate'])
        self._root.mainloop()
