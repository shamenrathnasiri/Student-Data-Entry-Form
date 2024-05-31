
import tkinter as tk

root =tk.Tk()
root.title("Student data entry form - University of SYYZ")
root.geometry('800x600')
root.resizable(False,False)
 
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
genderEntry1=tk.Radiobutton(root,text="Male",font='arial 14',value='male',variable=genderValue)
genderEntry2=tk.Radiobutton(root,text="Female",font='arial 14',value='Female',variable=genderValue)
mobileEntry=tk.Entry(root,textvariable=mobileValue,width=30,bd=2,font=20)
emailEntry=tk.Entry(root,textvariable=emailValue,width=30,bd=2,font=20)

nameEntry.place(x=200,y=150)
adressEntry.place(x=200,y=200)
ageEntry.place(x=200,y=250)
genderEntry1.place(x=200,y=300)
genderEntry2.place(x=300,y=300)
mobileEntry.place(x=200,y=350)
emailEntry.place(x=200,y=400)

root.mainloop()