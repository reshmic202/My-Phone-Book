from tkinter  import *
import datetime
from mypeople import MyPeople
from addpeople import AddPeople
from aboutus import About
date =datetime.datetime.now().date()
print(str(date))
 
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
#print("Current Time =", current_time)


class Application(object):
    def __init__(self,master):
        self.master = master

        #frames
        self.top =Frame(master,height=150,bg='white')
        self.top.pack(fill=X)

        self.bottom=Frame(master,height=500,bg='#6203fc')
        self.bottom.pack(fill=X)

        #top frame design
        self.top_image=PhotoImage(file='icons/book.png')
        self.top_image_label =Label(self.top,image=self.top_image,height=75,width=75)
        self.top_image_label.place(x=50,y=20)

        self.heading =Label(self.top,text='My PhoneBook App',font='arial 30 bold',bg='white',fg='#ebb434')
        self.heading.place(x=160,y=40)
        self.date_lbl =Label(self.top,text="Today's date:"+str(date),font='arial 12 bold',fg='#ebb434',bg='white')
        self.date_lbl.place(x=450,y=90)
    
        self.now_lbl=Label(self.top,text="Time:"+current_time,font='arial 12 bold',fg='#ebb434',bg='white')
        self.now_lbl.place(x=450,y=120)

        #button1-View people
        self.viewButton = Button(self.bottom, text="My people", fg="#6932a8",bg="white",font='arial 12 bold',command=self.my_people)
        self.viewButton.place(x=250,y=70)

        #button2-add people
        self.addButton = Button(self.bottom,text="Add people",fg="#6932a8",bg="white",font='arial 12 bold',command=self.addpeoplefunction)
        self.addButton.place(x=250,y=130)

        #button3-About us
        self.aboutButton = Button(self.bottom,text="About Us",fg="#6932a8",bg="white",font='arial 12 bold',command =self.about_us)
        self.aboutButton.place(x=250,y=190)
    def my_people(self):
        people =MyPeople()
    def about_us(self):
        about =About()


    def addpeoplefunction(self):
        addpeoplewindows=AddPeople()
def main():
    root =Tk()
    app =Application(root)
    root.title("PhoneBook App")
    root.geometry("650x550+200+100")
    root.resizable(True,True)
    root.mainloop()
if __name__ == '__main__':
    main()

    