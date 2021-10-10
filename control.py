from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Dbconnect import DBConnect
from ListRequest import ListStudent

dbConnect = DBConnect()

def BuSaveData():
    #print("Full Name:{}".format(EntryFullName.get()))
    #print("Graduate info:{}".format(SpanGender.get()))
    msg = dbConnect.Add(EntryFullName.get(), SpanGender.get())
    messagebox.showinfo(title="Add info",message=msg)
    EntryFullName.delete(0, 'end')

def BuListData():
    #print('not implemented yet')
    listrequest=ListStudent()

root = Tk()
root.title("Student name")
root.configure(background="#e1d8b2")
# Style
style = ttk.Style()
style.theme_use('classic')
style.configure('TLable', background="#e1d8b2")
style.configure('TButton', background="#e1d8b2")
style.configure('TRadiobutton', background="#e1d8b2")

# Student info
ttk.Label(root, text="Full Name:").grid(row=0, column=0, padx=10, pady=10)
EntryFullName = ttk.Entry(root, width=30, font=('Arial', 16))
EntryFullName.grid(row=0, column=1, columnspan=2, pady=10)

# Graduate info
ttk.Label(root, text="Gender:").grid(row=1, column=0)
SpanGender = StringVar()
ttk.Radiobutton(root, text="Graduate", variable=SpanGender, value="Graduate").grid(row=1, column=1)
ttk.Radiobutton(root, text="undergraduate", variable=SpanGender, value="undergraduate").grid(row=1, column=2)

# buttons
buSubmit = ttk.Button(root, text="Submit")
buSubmit.grid(row=3, column=3)
buList = ttk.Button(root, text="List Students Name")
buList.grid(row=3, column=2)
buSubmit.config(command=BuSaveData)
buList.config(command=BuListData)
root.mainloop()
