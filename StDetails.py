import tkinter as tk
from tkinter import ttk
import mysql.connector 
import tkinter.messagebox as msg


root =tk.Tk()
root.title("Student data entry form - University of SYYZ")
root.geometry('800x600')
root.resizable(False,False)

#add database
def regdata():
    mydb = mysql.connector.connect(
        host ="localhost",
        port = "3306",
        user ="root",
        password ="",
        database ="stdreg")
    
    mycursor = mydb.cursor()

    name = nameEntry.get()
    adress = adressEntry.get()
    age = ageEntry.get()
    gender = genderEntry.get()
    mobile = mobileEntry.get()
    email = emailEntry.get()

    mycursor.execute("insert into stdetails values(%s,%s,%s,%s,%s,%s)",(name,adress,age,gender,mobile,email))
    mydb.commit()
    msg.showinfo("registration","registeres successfully")

def clear(): #clear 
    nameEntry.delete(0,tk.END)
    adressEntry.delete(0,tk.END)
    ageEntry.delete(0,tk.END)
    genderEntry.delete(0,tk.END)
    mobileEntry.delete(0,tk.END)
    emailEntry.delete(0,tk.END)

tk.Label(root,text="Student Registration Form", font="arial 25").pack(pady=50)
tk.Label(text="Name", font =23).place(x=100,y=150)
tk.Label(text="Adress", font =23).place(x=100,y=200)
tk.Label(text="Age", font =23).place(x=100,y=250)
tk.Label(text="Gender", font =23).place(x=100,y=300)
tk.Label(text="Mobile No", font =23).place(x=100,y=350)
tk.Label(text="Email", font =23).place(x=100,y=400)

#data entry variable
nameValue= tk.StringVar()
adressValue= tk.StringVar()
ageValue= tk.StringVar()
genderValue=tk.StringVar()
mobileValue= tk.StringVar()
emailValue= tk.StringVar()

nameEntry=tk.Entry(root,textvariable=nameValue,width=30,bd=2,font=20)
adressEntry=tk.Entry(root,textvariable=adressValue,width=30,bd=2,font=20)
ageEntry=tk.Entry(root,textvariable=ageValue,width=30,bd=2,font=20)
genderEntry=tk.Entry(root,textvariable=genderValue,width=30,bd=2,font=20)
mobileEntry=tk.Entry(root,textvariable=mobileValue,width=30,bd=2,font=20)
emailEntry=tk.Entry(root,textvariable=emailValue,width=30,bd=2,font=20)

nameEntry.place(x=200,y=150)
adressEntry.place(x=200,y=200)
ageEntry.place(x=200,y=250)
genderEntry.place(x=200,y=300)
mobileEntry.place(x=200,y=350)
emailEntry.place(x=200,y=400)

#submit and clear button

button1 =ttk.Button(root,text='Submit', command= regdata ) #submit button
button1.pack()
button1.place(x=270,y=500)

button2=ttk.Button(root,text=' X Clear', command= clear) #clear button
button2.pack()
button2.place(x=470,y=500)



root.mainloop()
