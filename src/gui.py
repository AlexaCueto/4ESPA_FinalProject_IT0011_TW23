import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import csv
from fileHandler import saveRecords

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

    messagebox.showinfo("Success", f"Registration Successful!\n\nFirst Name: {firstName}\nMiddle Name: {middleName}\nLast Name: {lastName}\nBirthday: {birthday}\nGender: {gender}")

    saveRecords("records.csv", [firstName, middleName, lastName, birthday, gender])

#Function to update gender display with an upside-down arrow
def update_gender_display(event=None):
    selected_gender = genderEntry.get()
    if selected_gender and selected_gender not in ["▼ Male", "▼ Female", "▼ Other"]:
        genderEntry.set(selected_gender)

#Function to remove arrow when clicked
def remove_arrow(event=None):
    selected_gender = genderEntry.get().replace("▼ ", "")
    genderEntry.set(selected_gender)

# Initialize root window
root = tk.Tk()
root.title("Sign Up")
root.geometry("700x550")  # Default size
root.configure(bg='#e6e6fa')

# Style for rounded corners
style = ttk.Style()
style.theme_use('clam')
style.configure("RoundedFrame.TFrame", background='white', borderwidth=0, relief='flat')
style.configure("RoundedLabel.TLabel", background='white', foreground='#4B0082', font=("Arial", 12))
style.configure("RoundedEntry.TEntry", fieldbackground='#f0e6fa', foreground='#4B0082', font=("Arial", 12), borderwidth=0, highlightthickness=0)
style.configure("RoundedButton.TButton", background='#9370DB', foreground='white', font=("Arial", 12, 'bold'), borderwidth=0, relief='flat')

# Function to create rounded frame
def rounded_frame(parent, **kwargs):
    frame = ttk.Frame(parent, style="RoundedFrame.TFrame", **kwargs)
    return frame

# Centering the frame (adjusted width)
floatingFrame = rounded_frame(root, padding=30)
floatingFrame.place(relx=0.5, rely=0.5, anchor="center", width=550, height=450) #adjusted width

# Frame to hold the form
formFrame = rounded_frame(floatingFrame, padding=20)
formFrame.pack(fill="both", expand=True)

# Title Label
ttk.Label(formFrame, text="Sign Up", style="RoundedLabel.TLabel", font=("Roboto", 18, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)

# Form Labels and Entries
labels = ["First Name:", "Middle Name:", "Last Name:", "Birthday (MM/DD/YYYY):", "Gender:"]

for i, label in enumerate(labels):
    ttk.Label(formFrame, text=label, style="RoundedLabel.TLabel").grid(row=i + 1, column=0, sticky="w", pady=7, padx=10) #Adjusted padx

# Entry fields (adjusted width)
entry_style = {"font": "Roboto 12", "bg": "#f0e6fa", "fg": "#4B0082", "relief": "flat", "highlightthickness": 0, "width": 25} #adjusted entry width
firstNameEntry = tk.Entry(formFrame, **entry_style)
middleNameEntry = tk.Entry(formFrame, **entry_style)
lastNameEntry = tk.Entry(formFrame, **entry_style)
birthdayEntry = tk.Entry(formFrame, **entry_style)
genderEntry = ttk.Combobox(formFrame, values=["Male", "Female", "Other"], state="readonly", style="RoundedEntry.TEntry", width=25) #adjusted combobox width

entries = [firstNameEntry, middleNameEntry, lastNameEntry, birthdayEntry, genderEntry]

for i, entry in enumerate(entries):
    entry.grid(row=i + 1, column=1, sticky="ew", padx=10, pady=10) #adjusted padx

# Set default arrow display
genderEntry.set("Select Gender")

# Bind events to modify arrow behavior
genderEntry.bind("<<ComboboxSelected>>", update_gender_display)  # Add arrow back after selection
genderEntry.bind("<Button-1>", remove_arrow)  # Remove arrow when clicked

entries = [firstNameEntry, middleNameEntry, lastNameEntry, birthdayEntry, genderEntry]
for i, entry in enumerate(entries):
    entry.grid(row=i + 1, column=1, sticky="ew", padx=10, pady=5) #adjusted padx

# Submit Button

ttk.Button(formFrame, text="            Sign  Up            ", command=signUp, style="RoundedButton.TButton").grid(row=6, column=0, columnspan=2, pady=15, sticky="")

# Adjust column weights for responsiveness
formFrame.columnconfigure(0, weight=2) #increased first column weight
formFrame.columnconfigure(1, weight=3)

# Run the main loop
root.mainloop()


#SAM'S CODE STARTS HERE---
import tkinter as tk
from tkinter import ttk, messagebox
import csv

RECORDS_FILE = "...\\records.csv"

def save_records(data):
    """Save records to a CSV file located outside the src folder."""
    try:
        with open(RECORDS_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)
    except Exception as e:
        messagebox.showerror("Error", f"Could not save record: {str(e)}")

def load_records():
    """Load records from a CSV file and skip the first row (header)."""
    try:
        with open(RECORDS_FILE, mode='r', newline='') as file:
            reader = csv.reader(file)
            records = list(reader)
            
            # Ensure there are records and skip the first row (header)
            return records[1:] if len(records) > 1 else []
        
    except FileNotFoundError:
        messagebox.showerror("Error", "The records file does not exist.")
    except Exception as e:
        messagebox.showerror("Unexpected Error", str(e))

    return []

def display_all_records():
    """Display all records in the treeview."""
    records = load_records()

    if not records:
        return
    
    tree.delete(*tree.get_children())
    for record in records:
        tree.insert("", "end", values=record)

def search_by_last_name():
    """Search for a record by last name and display results."""
    last_name = search_entry.get().strip()
    
    if not last_name:
        messagebox.showerror("Error", "Search value cannot be empty.")
        return
    
    records = load_records()
    if not records:
        return
    
    results = [record for record in records if len(record) >= 3 and record[2].strip().lower() == last_name.lower()]
    
    tree.delete(*tree.get_children())
    if results:
        for record in results:
            tree.insert("", "end", values=record)
    else:
        messagebox.showinfo("No Record Found", "No matching record found.")

# Initialize main window
root = tk.Tk()
root.title("Records Viewer")
root.geometry("700x500")
root.configure(bg='#e6e6fa')

# Title Label
title_label = tk.Label(root, text="Records Viewer", font=("Arial", 18, 'bold'), bg='#e6e6fa', fg='#4B0082')
title_label.pack(pady=10)

# Search Frame
search_frame = tk.Frame(root, bg='#e6e6fa')
search_frame.pack(pady=5)

search_label = tk.Label(search_frame, text="Search by Last Name:", font=("Arial", 12), bg='#e6e6fa')
search_label.pack(side=tk.LEFT, padx=5)

search_entry = tk.Entry(search_frame, font=("Arial", 12))
search_entry.pack(side=tk.LEFT, padx=5)

search_button = tk.Button(search_frame, text="Search", font=("Arial", 12, 'bold'), bg='#9370DB', fg='white', command=search_by_last_name)
search_button.pack(side=tk.LEFT, padx=5)

# Treeview Frame
tree_frame = tk.Frame(root)
tree_frame.pack(pady=10, fill=tk.BOTH, expand=True)

columns = ("First Name", "Middle Name", "Last Name", "Birthday", "Gender")
tree = ttk.Treeview(tree_frame, columns=columns, show='headings')

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor=tk.CENTER, width=120)

tree.pack(fill=tk.BOTH, expand=True)

# View All Records Button
view_all_button = tk.Button(root, text="View All Records", font=("Arial", 12, 'bold'), bg='#9370DB', fg='white', command=display_all_records)
view_all_button.pack(pady=10)

root.mainloop()