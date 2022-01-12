import time
import tkinter
from tkinter import *
class UserLogin(tkinter.Tk):
    def __init__(self):
         super().__init__()
         self.message = tkinter.StringVar(self,'')
         self.username = tkinter.StringVar(self,'')
         self.password = tkinter.StringVar(self,'')
         self.ButtAdmin = tkinter.StringVar(self,'')
         self.ButtLogin = tkinter.StringVar(self,'')
         self.title("Login Form")
         # setting height and width of screen
         self.geometry("300x250+500+200")
         self.resizable(width=False, height=False)
         self.labelframe1 = LabelFrame(self, text="user", highlightbackground="black", highlightcolor="orange",bd=5, )
         self.labelframe1.pack(fill=BOTH, expand="yes", padx=20, pady=20)
         #Creating layout of login form
         self.outtitle1 =Label(self.labelframe1, text="Please enter details below", bg="orange", fg="white")
         self.outtitle1.pack()
         #Username Label
         self.text1=Label(self.labelframe1, text="Username * ")
         self.text1.place(x=20,y=40)
         # Username textbox
         self.entry1=Entry(self.labelframe1, textvariable=self.username)
         self.entry1.place(x=90, y=42)
         # Password Label
         self.text2=Label(self.labelframe1, text="Password * ")
         self.text2.place(x=20, y=80)
         # Password textbox
         self.entry2=Entry(self.labelframe1, textvariable=self.password, show="*")
         self.entry2.place(x=90, y=82)
         # Label for displaying login status[success/failed]
         self.outtext2=Label(self.labelframe1, text="", textvariable=self.message, fg='red')
         self.outtext2.place(x=95, y=100)
         # Login button
         self.ButtLogin = Button(self.labelframe1, text="Login", width=30, height=1, bg="orange", command=self.login)
         self.ButtLogin.place(x=15, y=130)
         self.ButtAdmin = Button(self.labelframe1, width=30, height=1, text="Admin", bg='orange', fg='black', command=self.getAdminLogin)
         self.ButtAdmin.place(x=15, y=160)
         self.mainloop()

    def login(self):
         # getting form data
         uname = self.username.get()
         pwd = self.password.get()
         # applying empty validation
         if uname == '' or pwd == '':
              self.message.set("fill the empty field!!!")
         else:
              if uname == "user" and pwd == "user":
                  self.message.set("Login success")
                  self.destroy()
                  time.sleep(1)
                  from quizui import QuizUser
                  QuizUser(uname)
              else:
                   self.message.set("Wrong username or password!!!")
    def getAdminLogin(self):
         self.destroy()
         return AdminLogin()



class AdminLogin(tkinter.Tk):
     def __init__(self):
          super().__init__()
          self.messageA = tkinter.StringVar(self, '')
          self.usernameA = tkinter.StringVar(self, '')
          self.passwordA = tkinter.StringVar(self, '')
          self.ButtLoginA = tkinter.StringVar(self, '')
          self.title("Login Admin  Form")
          # setting height and width of screen
          self.geometry("300x250+500+200")
          self.resizable(width=False, height=False)
          self.labelframe1 = LabelFrame(self, text="user", highlightbackground="black", highlightcolor="orange", bd=5)
          self.labelframe1.pack(fill=BOTH, expand="yes", padx=20, pady=20)
          # Creating layout of login form
          self.outtitle1 = Label(self.labelframe1, text="Please enter details below", bg="orange", fg="white")
          self.outtitle1.pack()
          # Username Label
          self.text1 = Label(self.labelframe1, text="Username * ")
          self.text1.place(x=20, y=40)
          # Username textbox
          self.entry1 = Entry(self.labelframe1, textvariable=self.usernameA)
          self.entry1.place(x=90, y=42)
          # Password Label
          self.text2 = Label(self.labelframe1, text="Password * ")
          self.text2.place(x=20, y=80)
          # Password textbox
          self.entry2 = Entry(self.labelframe1, textvariable=self.passwordA, show="*")
          self.entry2.place(x=90, y=82)
          # Label for displaying login status[success/failed]
          self.outtext2 = Label(self.labelframe1, text="", textvariable=self.messageA, fg='red')
          self.outtext2.place(x=95, y=100)
          # Login button
          self.ButtLoginA = Button(self.labelframe1, text="Login", width=30, height=1, bg="orange", command=self.login)
          self.ButtLoginA.place(x=15, y=130)
          self.mainloop()

     def login(self):
          # getting form data
          uname = self.usernameA.get()
          pwd = self.passwordA.get()
          # applying empty validation
          if uname == '' or pwd == '':
               self.messageA.set("fill the empty field!!!")
          else:
               if uname == "admin" and pwd == "admin":
                    self.messageA.set("Login success")
               else:
                    self.messageA.set("Wrong username or password!!!")
