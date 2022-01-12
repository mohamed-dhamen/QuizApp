import time
import tkinter
from tkinter import *
from QuizeManage import QuizM
class QuizUser(tkinter.Tk):
    diccounter=1
    listcounter=0
    def __init__(self, name):
        super().__init__()
        self.score = 0
        self.btnbox_y_pos = 100
        self.list_Quiz = QuizM.view_data(self)
        self.messagequestion=StringVar(self,'')
        self.option1=''
        self.option2 = ''
        self.option3 = ''
        self.option4 =''
        self.answer=StringVar(self,'')
        self.stName = tkinter.StringVar(self,'')
        self.stLname =tkinter.StringVar(self,'')
        self.stName=name
        #self.stLname=lastname
        self.geometry("850x530+200+80")
        self.title(self.stName)
        self.resizable(width=False, height=False)
        self.creat_Lframe_userInfo()
        self.add_Names_Scor()
        self.creat_zone_question()
        self.creat_zone_buttonbox()
        self.add_btnbox()
        self.creat_btnStart()
        self.creat_btnnext()
        self.creat_btnquit()
        self.mainloop()
    def creat_Lframe_userInfo(self):
        self.userinfolabel = LabelFrame(self, width=200, height=410,font=("Arial", 10), bd=5, fg="black",bg="#52BE80",text="user Info")
        self.userinfolabel.place(x=630,y=70)

    def add_Names_Scor(self):
        self.textlebel1 = Label(self.userinfolabel, text='Name   :', fg='white', font=("Arial", 12),bg="#52BE80")
        self.textlebel1.place(x=5, y=4)
        self.lablName = Label(self.userinfolabel, text=self.stName, fg='white', font=("Arial", 12),bg="#52BE80")
        self.lablName.place(x=80, y=4)
        # self.textlebel2 = Label(self.userinfolabel, text='Last Name:', fg='white', font=("Arial", 12),bg="#52BE80")
        # self.textlebel2.place(x=5, y=40)
        # self.lablLName = Label(self.userinfolabel, text=self.stLname, fg='white', font=("Arial", 12),bg="#52BE80")
        # self.lablLName.place(x=90, y=40)
    def creat_zone_question(self):
        self.labequestion = LabelFrame(self, fg='black', font=("Arial", 10), width=600, height=55, bd=5,bg="#138D75",text="Question?")
        self.labequestion.place(x=20, y=20)
        self.labelText=Label(self.labequestion,font=("Arial", 15),text="no question yeat ",fg='white',bg="#138D75")
        self.labelText.place(x=150,y=0)
    def creat_zone_buttonbox(self):
        self.boxframe = LabelFrame(self, text="zone of repense ", bd=5, width=600, height=410,font=("Arial",10),bg='#F39C12')
        self.boxframe.place(x=20, y=75)
    def add_btnbox(self):
        self.varint=IntVar(self)
        self.varint.set(1)
        self.btnR1=Radiobutton(self.boxframe,text='',variable=self.varint,value=1,font=("Arial",15),bg='#F39C12',fg='white',command=self.selected)
        self.btnR1.place(x=60,y=self.btnbox_y_pos)
        self.btnR2 = Radiobutton(self.boxframe, text='', variable=self.varint, value=2, font=("Arial", 15),bg='#F39C12',fg='white',command=self.selected)
        self.btnR2.place(x=60, y=self.btnbox_y_pos+40)
        self.btnR3 = Radiobutton(self.boxframe, text='', variable=self.varint, value=3, font=("Arial", 15),bg='#F39C12',fg='white',command=self.selected)
        self.btnR3.place(x=60, y=self.btnbox_y_pos+80)
        self.btnR4 = Radiobutton(self.boxframe, text='', variable=self.varint, value=4, font=("Arial", 15),bg='#F39C12',fg='white',command=self.selected)
        self.btnR4.place(x=60, y=self.btnbox_y_pos+120)

    def selected(self):
        match self.varint.get():
            case 1:
                self.btnR1.config(fg="green")
                self.btnR2.config(fg="white")
                self.btnR3.config(fg="white")
                self.btnR4.config(fg="white")
            case 2:
                self.btnR1.config(fg="white")
                self.btnR2.config(fg="green")
                self.btnR3.config(fg="white")
                self.btnR4.config(fg="white")
            case 3:
                self.btnR1.config(fg="white")
                self.btnR2.config(fg="white")
                self.btnR3.config(fg="green")
                self.btnR4.config(fg="white")
            case 4:
                self.btnR1.config(fg="white")
                self.btnR2.config(fg="white")
                self.btnR3.config(fg="white")
                self.btnR4.config(fg="green")

        return self.varint.get()

    def creat_btnStart(self):
        self.btnstart=Button(self,text='Start',width=20,height=2,bg="#3498DB",fg="white",font=("Arial",10),relief=RAISED,command=self.startquiz)
        self.btnstart.place(x=640,y=14)



    def creat_btnnext(self):
        self.btnNext=Button(self.boxframe,text='Next',width=15,height=2,bg="#138D75",fg="white",
                            font=("Arial",10),relief=RAISED,command=self.next)
        self.btnNext.place(x=400,y=310)
    def creat_btnquit(self):
        self.btnQuit = Button(self.boxframe, text='exit', width=15, height=2, bg="#138D75", fg="white",
                              font=("Arial", 10), relief=RAISED,command=self.quit)
        self.btnQuit.place(x=200, y=310)
    def startquiz(self):
            dic=self.list_Quiz[QuizUser.listcounter]
            self.messagequestion = str(QuizUser.diccounter)+" : "+dic[str(QuizUser.diccounter)]
            self.labelText.config(text=self.messagequestion)
            self.options = dic['option']
            self.answer = dic['repense']
            self.option1 = self.options[0] + ' !'
            self.option2 = self.options[1] + ' !'
            self.option3 = self.options[2] + ' !'
            self.option4 = self.options[3] + ' !'
            self.labelText.config(text=self.messagequestion)
            self.btnR1.config(text=self.option1)
            self.btnR2.config(text=self.option2)
            self.btnR3.config(text=self.option3)
            self.btnR4.config(text=self.option4)
            self.btnstart.config(stat=DISABLED,text="starting ...")
            print(self.list_Quiz)

    def quit(self):
        time.sleep(1)
        self.destroy()
    def next(self):
        QuizUser.diccounter=QuizUser.diccounter+1
        QuizUser.listcounter=QuizUser.listcounter+1
        number=self.selected()
        if QuizUser.listcounter <len(self.list_Quiz):
            if self.options[number - 1] == self.answer:
                self.score = self.score + 10
                from tkinter import messagebox
                messagebox.showinfo("alert", "ok you going good  score :" + str(self.score))
            else :
                from tkinter import messagebox
                messagebox.showinfo("alert", ":( sorry you teket a mastak but no problem :")
            dic = self.list_Quiz[QuizUser.listcounter]
            self.messagequestion = str(QuizUser.diccounter) + " : " + dic[str(QuizUser.diccounter)]
            self.labelText.config(text=self.messagequestion)
            self.options = dic['option']
            self.answer = dic['repense']
            self.option1 = self.options[0] + ' !'
            self.option2 = self.options[1] + ' !'
            self.option3 = self.options[2] + ' !'
            self.option4 = self.options[3] + ' !'
            self.labelText.config(text=self.messagequestion)
            self.btnR1.config(text=self.option1)
            self.btnR2.config(text=self.option2)
            self.btnR3.config(text=self.option3)
            self.btnR4.config(text=self.option4)
        else:
            from tkinter import messagebox
            if self.options[number - 1] == self.answer:
                self.score = self.score + 10
            messagebox.showinfo("final score", "this is your score:"+str(self.score))
