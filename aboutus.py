from tkinter import *
class About(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("550x550+550+200")
        self.title("About App")
        self.resizable(False,False)
        self.top=Frame(self, height=500,width=550, bg='#ffa500')
        self.top.pack(fill=BOTH)
        self.text=Label(self.top, text="Hey this is about us page"'\n This application is made by Miss Reshmi Chaurasiya')
        self.text.place(x=50,y=50)