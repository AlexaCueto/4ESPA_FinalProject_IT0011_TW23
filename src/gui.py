import tkinter
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
from fileHandler import saveRecords

import os
import csv

root = tkinter.Tk()
root.title("Registration Form")
root.geometry("800x600")

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
    saveRecords("records.csv", [firstName, middleName, lastName, birthday, gender])




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


root.mainloop()




