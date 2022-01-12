import tkinter
from tkinter import *
class AddPerson(tkinter.Tk):
    def __init__(self):
        super(AddPerson, self).__init__()
        self.geometry("300x300+500+80")
        self.title("Hello : " + self.Aname)
        self.config(bg="#F5B041")
        self.resizable(width=False, height=False)
        self.creat_labeladdP()
        self.mainloop()
    def creat_labeladdP(self):
        self.inputFrame = Frame(self, width=200, bd=5, bg="#F5B041")
        self.inputFrame.pack()

        self.id = Label(self.inputFrame, text="ID  :", bg="#F5B041", fg='white', font=("Arial", 15))
        self.id.grid(row=0, column=0)

        self.full_Name = Label(self.inputFrame, text="Full_Name:", bg="#F5B041", fg="white", font=("Arial", 15))
        self.full_Name.grid(row=1, column=0)

        self.email = Label(self.inputFrame, text="Email:", bg="#F5B041", fg="white", font=("Arial", 15))
        self.email.grid(row=2, column=0)
        self.id_entry = Entry(self.inputFrame, width=30)
        self.id_entry.grid(row=0, column=1)

        self.fullname_entry = Entry(self.inputFrame, width=30)
        self.fullname_entry.grid(row=1, column=1)

        self.email_entry = Entry(self.inputFrame, width=30)
        self.email_entry.grid(row=2, column=1)

        self.Input_button = Button(self.inputFrame, text="Input data", width=25, bg='green')
        self.Input_button.grid(row=3, column=1)
AddPerson()