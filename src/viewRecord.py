import tkinter as tk
from tkinter import ttk, messagebox
import csv

RECORDS_FILE = "records.csv"

def loadRecords():
    """Load records from a CSV file and skip the first row (header)."""
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

def displayAllRecords():
    """Display all records in the treeview."""
    records = loadRecords()
    tree.delete(*tree.get_children())
    for record in records:
        tree.insert("", "end", values=record)

def viewRecordsWindow(mainWindow):
    """Open a new window to display all records."""
    root = tk.Toplevel(mainWindow)
    root.title("View Records")
    root.geometry("700x500")
    root.configure(bg='#e6e6fa')
    
    tk.Label(root, text="Records Viewer", font=("Arial", 18, 'bold'), bg='#e6e6fa', fg='#4B0082').pack(pady=10)
    
    treeFrame = tk.Frame(root, bg='#e6e6fa')
    treeFrame.pack(pady=10, fill=tk.BOTH, expand=True)
    
    global tree
    tree = ttk.Treeview(treeFrame, columns=("First Name", "Middle Name", "Last Name", "Birthday", "Gender"), show='headings')
    for col in ("First Name", "Middle Name", "Last Name", "Birthday", "Gender"):
        tree.heading(col, text=col)
        tree.column(col, anchor=tk.CENTER, width=120)
    tree.pack(fill=tk.BOTH, expand=True)
    
    displayAllRecords()
