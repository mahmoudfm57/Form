from tkinter import *
from tkinter import ttk
import tkcalendar
root = Tk()
root.geometry('470x340')
root.title('Data Entey Form')

#title
title= Label(root,text='Data Entry Form',font="Calibri 20 bold")
title.grid(row=0,column=0,pady=10,columnspan=4)


#first and last name

fname_label = Label(root,text='First Name')
fname_label.grid(row=1,column=0,padx=10)

fname_entry = Entry(root,width=20)
fname_entry.grid(row=1,column=1)


lname_label = Label(root,text='Last Name')
lname_label.grid(row=1,column=2,padx=10)

lname_entry = Entry(root,width=20)
lname_entry.grid(row=1,column=3,pady=5)

#birth data

birth_label = Label(root,text='Birth Data')
birth_label.grid(row=2,column=0,padx=10,sticky="w")

birth_entry = tkcalendar.DateEntry(root,width=20)
birth_entry.grid(row=2,column=1,pady=5,columnspan=3,sticky="we")

#Gender
Gender = Label(root,text='Gender')
Gender.grid(row=3,column=0,padx=10,sticky="w")

gender=StringVar()
gender.set('Male')
male =Radiobutton(root,text="Male",variable=gender,value='Male')
male.grid(row=3,column=1,pady=5,sticky="w")

female =Radiobutton(root,text="Female",variable=gender,value='Female')
female.grid(row=3,column=2,pady=5,sticky="w")

#country

country_label = Label(root,text='Country')
country_label.grid(row=4,column=0,padx=10,sticky="w")

country_choices = ttk.Combobox(root,width=20,values=["Saudi Arabia","Syria","Egypt","Turkey","UAE"])
country_choices.grid(row=4,column=1,pady=5,columnspan=3,sticky="we")

#Address
text_label = Label(root,text="Address")
text_label.grid(row=5,column=0,padx=10,sticky="nw")

text_entry = Text(root,width=20,height=5)
text_entry.grid(row=5,column=1,pady=5,columnspan=3,sticky="we")

#buttons
def record():
    fname = fname_entry.get()
    lname = lname_entry.get()
    birth = birth_entry.get()
    gender_ = gender.get()
    country = country_choices.get()
    address = text_entry.get("1.0","end-1c")
    text= fname+","+lname+","+birth+","+gender_+","+country+","+address+"\n"
    with open(r"D:\My Project\pyton\ادخل بيانات Form\file.csv","a") as file:
        file.write(text)
    clear_all()
def clear_all():
    fname_entry.delete(0,"end")
    lname_entry.delete(0,"end")
    birth_entry.delete(0,"end")
    gender.set('Male')
    country_choices.delete(0,"end")
    text_entry.delete("1.0","end")
    fname_entry


seve =Button(root,text="Save",command=record)
seve.grid(row=6,column=0,padx=10,sticky="e",ipadx=10)

clear =Button(root,text="Clear",command=clear_all)
clear.grid(row=6,column=2,padx=10)



root.mainloop()