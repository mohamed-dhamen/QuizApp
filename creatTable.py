from tkinter import *
from tkinter import ttk

ws = Tk()
ws.title('PythonGuides')
ws.geometry('500x500')

set = ttk.Treeview(ws)
set.pack()

set['columns'] = ('id', 'full_Name', 'award')
set.column("#0", width=0, stretch=NO)
set.column("id", anchor=CENTER, width=80)
set.column("full_Name", anchor=CENTER, width=80)
set.column("award", anchor=CENTER, width=80)

set.heading("#0", text="", anchor=CENTER)
set.heading("id", text="ID", anchor=CENTER)
set.heading("full_Name", text="Full_Name", anchor=CENTER)
set.heading("award", text="Award", anchor=CENTER)

# data
data = [
    [1, "Jack", "gold"],
    [2, "Tom", "Bronze"]

]

global count
count = 0

for record in data:
    set.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2]))

    count += 1

Input_frame = Frame(ws)
Input_frame.pack()

id = Label(Input_frame, text="ID")
id.grid(row=0, column=0)

full_Name = Label(Input_frame, text="Full_Name")
full_Name.grid(row=0, column=1)

award = Label(Input_frame, text="Award")
award.grid(row=0, column=2)

id_entry = Entry(Input_frame)
id_entry.grid(row=1, column=0)

fullname_entry = Entry(Input_frame)
fullname_entry.grid(row=1, column=1)

award_entry = Entry(Input_frame)
award_entry.grid(row=1, column=2)


def input_record():
    global count

    set.insert(parent='', index='end', iid=count, text='',
               values=(id_entry.get(), fullname_entry.get(), award_entry.get()))
    count += 1

    id_entry.delete(0, END)
    fullname_entry.delete(0, END)
    award_entry.delete(0, END)


# button
Input_button = Button(ws, text="Input Record", command=input_record)

Input_button.pack()

ws.mainloop()