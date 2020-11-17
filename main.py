from tkinter import *
import tkinter.ttk as ttk
import string
import random


# password Generator

def Generator():
    upper = list(string.ascii_uppercase)
    lower = list(string.ascii_lowercase)
    digits = list(string.digits)
    special_car = ['@','#','$','*','&','_','!']
    lst = [upper,lower,digits,special_car]
    passwordlist = []
    for i in lst:
        passwordlist.extend(i)
    
    password_Entry.delete(0,END)
    random.shuffle(passwordlist)
    length = passlength.get()
    password_Entry.insert(0,passwordlist[:int(length)])
    

# global variables
bg = 'yellow'

# basic gui code
root = Tk()
root.geometry('300x200')
root.title('Password Generator')
root.config(bg = bg)

# variables
length = StringVar()




# heading label
Label(text = 'Password Generator' ,font ='times 14 bold',bg = bg).pack(pady = 10)

# password entrybox
password_Entry = ttk.Entry(root,width=25,font='times 14')
password_Entry.pack(pady = 10)

# password lenght combobox
passlength = ttk.Combobox(value = [4,8,10,12,14,16],textvariable = length,state = 'readonly',width = 5)
passlength.current(1)
passlength.pack()

# button to Generate
btn = ttk.Button(text = 'Generate',command=Generator)
btn.pack(pady = 17)

root.mainloop()