import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
from fileHandler import saveRecords

import os
import csv


# Function to handle signup
def signUp():
    firstName = firstNameEntry.get().strip()
    middleName = middleNameEntry.get().strip()
    lastName = lastNameEntry.get().strip()
    birthday = birthdayEntry.get().strip()
    gender = genderEntry.get().strip()

    if not firstName or not middleName or not lastName or not birthday or not gender:
        messagebox.showerror("Error", "This field is required. Please fill in required inputs.")
        return

    try:
        datetime.strptime(birthday, "%m/%d/%Y")
    except ValueError:
        messagebox.showerror("Error", "Birthday must be in the format of MM/DD/YYYY.")
        return

    if gender not in ["Male", "Female", "Other"]:
        messagebox.showerror("Error", "Please input a valid gender.")
        return

    messagebox.showinfo("Success", f"Registration Successful!\n\nFirst Name: {firstName}\nMiddle Name: {middleName}\nLast Name: {lastName}\nBirthday: {birthday}\nGender: {gender}")

#call the function to save the records
    saveRecords("records.csv", [firstName, middleName, lastName, birthday, gender])
    
#ALL GUI STUFF BELOW
#Initialize root window
root = tk.Tk()
root.title("Registration Form")
root.geometry("400x400")
root.configure(bg='#8d2991')
windowWidth = 500 #width for the window for responsiveness
windowHeight = 400 #height for the window for responsiveness 
root.geometry(f"{windowWidth}x{windowHeight}") #set the window size

#Centering the frame
containerFrame = tk.Frame(root, bg='#8d2991', padx=30, pady=30, relief="ridge", bd=2)
containerFrame.place(relx=0.5, rely=0.5, anchor="center", width=500, height=400)

# Configure grid columns
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)

#Frame to hold the form
formFrame = tk.Frame(root, bg='#8d2991', padx=20, pady=20)
formFrame.grid(row=0, column=0, columnspan=2, sticky="news") #news stands for NORTH, EAST, WEST, SOUTH

#Title Label
formFrame = tk.Frame(containerFrame, bg='#8d2991')
formFrame.pack(fill="x", pady=10)
tk.Label(formFrame, text="Registration Form", font="Helvetica 16 bold", bg='#8d2991', fg="white").grid(row=0, column=0, columnspan=2, pady=10)

#Form Labels and Entries
entryFrame = tk.Frame(containerFrame, bg='#8d2991')
entryFrame.pack(fill="both", expand=True)

labels = ["First Name:", "Middle Name:", "Last Name:", "Birthday (MM/DD/YYYY):", "Gender:"]
entries = []
for i, label in enumerate(labels):
    tk.Label(formFrame, text=label, bg='#8d2991', fg="white", anchor="w").grid(row=i+1, column=0, sticky="w", pady=5) 

#Entry fields
firstNameEntry = tk.Entry(formFrame)
middleNameEntry = tk.Entry(formFrame)
lastNameEntry = tk.Entry(formFrame)
birthdayEntry = tk.Entry(formFrame)
genderEntry = ttk.Combobox(formFrame, values=["Male", "Female", "Other"], state="readonly")

entries = [firstNameEntry, middleNameEntry, lastNameEntry, birthdayEntry, genderEntry]
for i, entry in enumerate(entries):
    entry.grid(row=i+1, column=1, sticky="ew", padx=10, pady=5)

#Submit Button
tk.Button(formFrame, text="Sign Up", command=signUp, bg="white", fg="#8d2991", font="Helvetica 12 bold").grid(row=6, column=0, columnspan=2, pady=15, sticky="ew")

#Adjust column weights for responsiveness
formFrame.columnconfigure(0, weight=1)
formFrame.columnconfigure(1, weight=2)

#Run the main loop
root.mainloop() 