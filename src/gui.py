import tkinter
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
import os
import csv

root = tkinter.Tk()
root.title("Registration Form")
root.geometry("400x400")
root.configure(bg='#ef8169')

def signUp():
    firstName = firstNameEntry.get().strip()
    middleName = middleNameEntry.get().strip()
    lastName = lastNameEntry.get().strip()
    birthday = birthdayEntry.get().strip()
    gender = genderEntry.get().strip()

    #Validate required fields
    if not firstName or not middleName or not lastName or not birthday or not gender:
        messagebox.showerror("This field is required. Please fill in required inputs.")
        return

    #Validate birthday
    try:
        datetime.strptime(birthday, "%m/%d/%Y") #Check if the date is in the correct format
    except ValueError:
        messagebox.showerror("Birthday must be in the format of MM/DD/YYYY.")
        return

    #Validate gender
    if gender not in ["Male", "Female", "Other"]:
        messagebox.showerror("Please input a valid gender.")
        return

    #If all fields are valid, print the information
    
    messagebox.showinfo(f"Registration Successful!\n\nFirst Name: {firstName}\nMiddle Name: {middleName}\nLast Name: {lastName}\nBirthday: {birthday}\nGender: {gender}")

#call the function to save the records

#Create form labels
tkinter.Label(root, text="Registration Form", font="Helvetica 16 bold").pack(pady=10)

#StringVars for the form fields
firstName = tkinter.StringVar()
middleName = tkinter.StringVar()
lastName = tkinter.StringVar()
birthday = tkinter.StringVar()
gender = tkinter.StringVar() 

# First Name
tkinter.Label(root, text="First Name:").pack()
firstNameEntry = tkinter.Entry(root, textvariable=firstName)
firstNameEntry.pack()

# Middle Name
tkinter.Label(root, text="Middle Name:").pack()
middleNameEntry = tkinter.Entry(root, textvariable=middleName)
middleNameEntry.pack()

# Last Name
tkinter.Label(root, text="Last Name:").pack()
lastNameEntry = tkinter.Entry(root, textvariable=lastName)
lastNameEntry.pack()

# Birthday
tkinter.Label(root, text="Birthday (MM/DD/YYYY):").pack()
birthdayEntry = tkinter.Entry(root, textvariable=birthday)
birthdayEntry.pack()

# Gender
tkinter.Label(root, text="Gender:").pack()
genderEntry = ttk.Combobox(root, textvariable=gender, values=["Male", "Female", "Other"], state="readonly")
genderEntry.pack()

# Submit Button
tkinter.Button(root, text="Sign Up", command=signUp, bg="green", fg="white").pack(pady=20)

root.mainloop()




