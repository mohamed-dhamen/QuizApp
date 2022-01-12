import tkinter
from tkinter import *
from tkinter import ttk
class AdminUI(tkinter.Tk):
    global count
    count=0
    def __init__(self,name):
        self.data = []
        super(AdminUI, self).__init__()
        self.Aname=name
        self.geometry("300x300+500+80")
        self.title("Hello : "+self.Aname)
        self.config(bg="#F5B041")
        self.resizable(width=False, height=False)
        self.creat_buttons()
        self.mainloop()
    def creat_buttons(self):
        self.btnaddp=Button(text="person" ,width=40,bg='white')
        self.btnaddp.pack()
        self.btnaddquestion=Button(text="questions" ,width=40,bg='white')
        self.btnaddquestion.pack()

admin=AdminUI('mohamed')
