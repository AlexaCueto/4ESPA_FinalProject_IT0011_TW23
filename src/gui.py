from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime

def signUp():
    firstName = firstNameEntry.get().strip()
    middleName = middleNameEntry.get().strip()
    lastName = lastNameEntry.get().strip()
    birthday = birthdayEntry.get().strip()
    gender = genderEntry.get().strip()
    
firstName = StringVar()
middleName = StringVar()
lastName = StringVar()
birthday = StringVar()
gender = StringVar()

#Validate required fields
if not firstName or not middleName or not lastName or not birthday or not gender:
    messagebox.showerror("This field is required. Please fill in required inputs.")
    return

#Valide first name
if not firstName.isalpha():
    messagebox.showerror("First name must be alphabetic characters.")
    return

#Validate middle name
if not middleName.isalpha():
    messagebox.showerror("Middle name must be alphabetic characters.")
    return

#Validate last name
if not lastName.isalpha():
    messagebox.showerror("Last name must be alphabetic characters.")
    return

#Validate birthday
try:
    datetime.strptime(birthday, "%m/%d/%Y") #Check if the date is in the correct format
except ValueError:
    messagebox.showerror("Birthday must be in the format of MM/DD/YYYY.")
    return

#Validate gender
if gender not in ["Male", "Female", "Other"]
    messagebox.showerror("Please input a valid gender.")
    return

#If all fields are valid, print the information
messagebox.showinfo(f"Registration Successful!\n\nFirst Name: {firstName}\nMiddle Name: {middleName}\nLast Name: {lastName}\nBirthday: {birthday}\nGender: {gender}")