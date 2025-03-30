import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import csv
from fileHandler import saveRecords

def isUserExists(firstName, middleName, lastName):
    try:
        with open("records.csv", "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 3 and row[0] == firstName and row[1] == middleName and row[2] == lastName:
                    return True  #User already exists
    except FileNotFoundError:
        return False  #If file doesn't exist, no duplicates
    return False  #No match found

def signUpWindow(mainWindow):
    root = tk.Toplevel(mainWindow) #toplevel
    root.title("Sign Up")
    root.geometry("700x500")
    root.configure(bg='#e6e6fa')
    
    #Function to handle signup
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

        if isUserExists(firstName, middleName, lastName):
            messagebox.showerror("Error", "This user has already been signed up!")
            return (signUpWindow)
        
        messagebox.showinfo("Success", f"Registration Successful!\n\nFirst Name: {firstName}\nMiddle Name: {middleName}\nLast Name: {lastName}\nBirthday: {birthday}\nGender: {gender}")

        saveRecords("records.csv", [firstName, middleName, lastName, birthday, gender])

        root.destroy()  #Close the signup window after clicking signup
        mainWindow.deiconify()  #Bring back main menu
    
    #Function to update gender display with an upside-down arrow
    def update_gender_display(event=None):
        selected_gender = genderEntry.get()
        if selected_gender and selected_gender not in ["▼ Male", "▼ Female", "▼ Other"]:
            genderEntry.set(selected_gender)

    #Function to remove arrow when clicked
    def remove_arrow(event=None):
        selected_gender = genderEntry.get().replace("▼ ", "")
        genderEntry.set(selected_gender)

    #Style for rounded corners
    style = ttk.Style(root)
    style.theme_use('clam')
    style.configure("RoundedFrame.TFrame", background='white', borderwidth=0, relief='flat')
    style.configure("RoundedLabel.TLabel", background='white', foreground='#4B0082', font=("Arial", 12))
    style.configure("RoundedEntry.TEntry", fieldbackground='#f0e6fa', foreground='#4B0082', font=("Arial", 12), borderwidth=0, highlightthickness=0)
    style.configure("RoundedButton.TButton", background='#9370DB', foreground='white', font=("Arial", 12, 'bold'), borderwidth=0, relief='flat')

    #Function to create rounded frame
    def rounded_frame(parent, **kwargs):
        frame = ttk.Frame(parent, style="RoundedFrame.TFrame", **kwargs)
        return frame

    #Centering the frame (adjusted width)
    floatingFrame = rounded_frame(root, padding=30)
    floatingFrame.place(relx=0.5, rely=0.5, anchor="center", width=550, height=450) #adjusted width

    #Frame to hold the form
    formFrame = rounded_frame(floatingFrame, padding=20)
    formFrame.pack(fill="both", expand=True)

    # itle Label
    ttk.Label(formFrame, text="Sign Up", style="RoundedLabel.TLabel", font=("Roboto", 18, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)

    #Form Labels and Entries
    labels = ["First Name:", "Middle Name:", "Last Name:", "Birthday (MM/DD/YYYY):", "Gender:"]

    for i, label in enumerate(labels):
        ttk.Label(formFrame, text=label, style="RoundedLabel.TLabel").grid(row=i + 1, column=0, sticky="w", pady=7, padx=10) #Adjusted padx

    #Entry fields (adjusted width)
    entry_style = {"font": "Roboto 12", "bg": "#f0e6fa", "fg": "#4B0082", "relief": "flat", "highlightthickness": 0, "width": 25} #adjusted entry width
    firstNameEntry = tk.Entry(formFrame, **entry_style)
    middleNameEntry = tk.Entry(formFrame, **entry_style)
    lastNameEntry = tk.Entry(formFrame, **entry_style)
    birthdayEntry = tk.Entry(formFrame, **entry_style)
    genderEntry = ttk.Combobox(formFrame, values=["Male", "Female", "Other"], state="readonly", style="RoundedEntry.TEntry", width=25) #adjusted combobox width

    entries = [firstNameEntry, middleNameEntry, lastNameEntry, birthdayEntry, genderEntry]

    for i, entry in enumerate(entries):
        entry.grid(row=i + 1, column=1, sticky="ew", padx=10, pady=10) #adjusted padx

    #Set default arrow display
    genderEntry.set("Select Gender")

    #Bind events to modify arrow behavior
    genderEntry.bind("<<ComboboxSelected>>", update_gender_display)  # Add arrow back after selection
    genderEntry.bind("<Button-1>", remove_arrow)  # Remove arrow when clicked

    entries = [firstNameEntry, middleNameEntry, lastNameEntry, birthdayEntry, genderEntry]
    for i, entry in enumerate(entries):
        entry.grid(row=i + 1, column=1, sticky="ew", padx=10, pady=5) #adjusted padx

    #Submit Button

    ttk.Button(formFrame, text="            Sign  Up            ", command=signUp, style="RoundedButton.TButton").grid(row=6, column=0, columnspan=2, pady=15, sticky="")

    #Adjust column weights for responsiveness
    formFrame.columnconfigure(0, weight=2) #increased first column weight
    formFrame.columnconfigure(1, weight=3)

    mainWindow.mainloop()