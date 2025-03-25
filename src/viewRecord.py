import tkinter as tk
from tkinter import ttk, messagebox
import csv

RECORDS_FILE = "records.csv"

def loadRecords():
    # Load records from a CSV file and skip the first row (header)
    try:
        with open(RECORDS_FILE, mode='r', newline='') as file:
            reader = csv.reader(file)
            records = list(reader)
            return records[1:] if len(records) > 1 else []
    except FileNotFoundError:
        messagebox.showerror("Error", "The records file does not exist.")
    except Exception as e:
        messagebox.showerror("Unexpected Error", str(e))
    return []

def viewRecordWindow(mainWindow):
    # Open a new window to display all records sorted by Last Name
    root = tk.Toplevel(mainWindow)
    root.title("View Records")
    root.geometry("700x500")
    root.configure(bg='#e6e6fa')

    tk.Label(root, text="Records Viewer", font=("Roboto", 18, 'bold'), bg='#e6e6fa', fg='#4B0082').pack(pady=3)

    treeFrame = tk.Frame(root, bg='#e6e6fa')
    treeFrame.pack(pady=3, fill=tk.BOTH, expand=True)

    # Adjust column order: Last Name first
    columns = ("Last Name", "First Name", "Middle Name", "Birthday", "Gender")
    tree = ttk.Treeview(treeFrame, columns=columns, show='headings', height=10)

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor=tk.CENTER, width=120)
    tree.pack(fill=tk.BOTH, expand=True)

    # Load and correctly reorder records
    records = loadRecords()
    
    # Sort records by Last Name 
    sorted_records = sorted(records, key=lambda record: record[2].lower())  

    for record in sorted_records:
        if len(record) == 5:  
            first_name, middle_name, last_name, birthday, gender = record  
            tree.insert("", "end", values=(last_name, first_name, middle_name, birthday, gender))  

    # Close Button
    tk.Button(root, text="Close", font=("Roboto", 12), bg="#8B0000", fg="white", command=root.destroy).pack(side="bottom", pady=5, anchor="center")  
