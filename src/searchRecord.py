import tkinter as tk
from tkinter import ttk, messagebox
import csv

RECORDS_FILE = "records.csv" #GUMAGANA TO 

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
