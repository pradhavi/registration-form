from tkinter import*
from tkinter import*
import sqlite3
root = Tk()
root.geometry('500x500')

root.title("Registration Form For 5G Hackathon")


Fullname=StringVar()
Email=StringVar()
var = IntVar()
c=StringVar()
var1= IntVar()
participents= IntVar()
def database():
   name1=Fullname.get()
   email=Email.get()
   gender=var.get()
   country=c.get()
   prog=var1.get()
   par=participents.get()
   conn = sqlite3.connect('Form.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS PARTICIPANTS (Fullname TEXT,Email TEXT,Gender TEXT,country TEXT,Programming TEXT,Participants INT)')
   cursor.execute('INSERT INTO PARTICIPANTS (FullName,Email,Gender,country,Programming,Participants) VALUES(?,?,?,?,?,?)',(name1,email,gender,country,prog,par,))
   conn.commit()


label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="FullName",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root,textvar=Fullname)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Email",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root,textvar=Email)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
label_3.place(x=70,y=230)

Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)

label_4 = Label(root, text="country",width=20,font=("bold", 10))
label_4.place(x=70,y=280)

list1 = ['US','India','UK','Australia','Chaina','Europe','Greek'];

droplist=OptionMenu(root,c, *list1)
droplist.config(width=15)
c.set('select your country') 
droplist.place(x=240,y=280)

label_4 = Label(root, text="Programming",width=20,font=("bold", 10))
label_4.place(x=85,y=330)
var2= IntVar()
Checkbutton(root, text="java", variable=var1).place(x=235,y=330)

Checkbutton(root, text="python", variable=var2).place(x=290,y=330)

label_5=Label(root, text="Participants",width=20,font=("bold",10))
label_5.place(x=80,y=375)

entry_5 = Entry(root,textvar=participents)
entry_5.place(x=240,y=375)

Button(root, text='Submit',width=20,bg='brown',fg='white',command=database).place(x=180,y=420)

root.mainloop()
