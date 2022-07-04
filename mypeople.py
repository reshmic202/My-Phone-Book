from tkinter import*
import sqlite3

from click import command
from addpeople import AddPeople
from updatepeople import Update
from display import Display
from tkinter import messagebox

con=sqlite3.connect('database.db')
cur =con.cursor()

class MyPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x650+600+200")
        self.title("My People")
        self.resizable(False,False)
        self.top =Frame(self,height=150,bg='white')
        self.top.pack(fill=X)
        self.bottom=Frame(self,height=500,bg='#ebe134')
        self.bottom.pack(fill=X)

        #top frame design
        self.top_image=PhotoImage(file='icons/people.png')
        self.top_image_label =Label(self.top,image=self.top_image,height=75,width=75)
        self.top_image_label.place(x=50,y=20)

        self.heading =Label(self.top,text='My PhoneBook App',font='arial 30 bold',bg='white',fg='#ebb434')
        self.heading.place(x=160,y=40)

        self.scroll=Scrollbar(self.bottom,orient=VERTICAL)
        

        self.listBox=Listbox(self.bottom,width=40,height=27)
        self.listBox.grid(row=0,padx=(40,0))
        self.scroll.config(command=self.listBox.yview)
        self.listBox.config(yscrollcommand=self.scroll.set)

        persons =cur.execute("select * from'addressbook'").fetchall()
        print(persons)
        count = 0
        for person in persons:
            self.listBox.insert(count, str(person[0])+". "+person[1]+" "+person[2])
            count+= 1
            
        self.scroll.grid(row=0,column=1,sticky=N+S)
        
        #buttons
        btnadd = Button(self.bottom,text="Add",width=12,font='Sans 12 bold',command=self.add_people)
        btnadd.grid(row=0,column=2,padx=20,pady=10,sticky=N)

        btnUpdate = Button(self.bottom,text="Update",width=12,font='Sans 12 bold', command=self.updatePerson)
        btnUpdate.grid(row=0,column=2,padx=20,pady=50,sticky=N)
       
        btnDisplay = Button(self.bottom,text="Display",width=12,font='Sans 12 bold',command=self.display_person)
        btnDisplay.grid(row=0,column=2,padx=20,pady=90,sticky=N)

        btnDelete = Button(self.bottom,text="Delete",width=12,font='Sans 12 bold',command=self.delete_person)
        btnDelete.grid(row=0,column=2,padx=20,pady=130,sticky=N)
    def delete_person(self):
        selected_item=self.listBox.curselection()
        person =self.listBox.get(selected_item)
        person_id = person.split(".")[0]

        query="delete from addressbook where person_id ={}".format(person_id)
        answer =messagebox.askquestion("Warning","Are you sure you wanna delete?")
        if answer=='yes':
            try:
                cur.execute(query)
                con.commit()
            except EXCEPTION as e:
                messagebox.showerror("Error",str(e))

    def add_people(self):
        add_page=AddPeople()
        self.destroy()

    def updatePerson(self):
        selected_item=self.listBox.curselection()
        person =self.listBox.get(selected_item)
        person_id = person.split(".")[0]
        updatepage=Update(person_id)

    def display_person(self):
        selected_item=self.listBox.curselection()
        person =self.listBox.get(selected_item)
        person_id = person.split(".")[0]
        displaypage=Display(person_id)

        


