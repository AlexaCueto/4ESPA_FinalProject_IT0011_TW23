import tkinter as tk
from tkinter import ttk, messagebox
from fileHandler import loadRecords
from viewRecord import viewRecordWindow

RECORDS_FILE = "records.csv"

def searchRecordWindow(mainWindow):
    """Creates the search record window."""
    root = tk.Toplevel(mainWindow)
    root.title("Search A Record")
    root.geometry("700x500")
    root.configure(bg='#e6e6fa')

    def searchByName():
        """Search for a record by any name field (First, Middle, or Last) and display results."""
        searchValue = searchEntry.get().strip().lower()
        
        if not searchValue:
            messagebox.showerror("Error", "Search value cannot be empty.")
            return

        records = loadRecords(RECORDS_FILE)
        if not records:
            messagebox.showinfo("No Records", "No records found in the system.")
            return
        
        results = [
            record for record in records if 
            searchValue in record.get("First Name", "").strip().lower() or
            searchValue in record.get("Middle Name", "").strip().lower() or
            searchValue in record.get("Last Name", "").strip().lower()
        ]
        
        tree.delete(*tree.get_children())
        if results:
            for record in results:
                tree.insert("", "end", values=(record["First Name"], record["Middle Name"], record["Last Name"], record["Birthday"], record["Gender"]))
        else:
            messagebox.showinfo("No Record Found", "No matching record found.")

    def openViewRecords():
        """Open the view all records window."""
        viewRecordWindow(mainWindow)  # Opens the view records page

    # Title Label
    tk.Label(root, text="Records Viewer", font=("Arial", 18, 'bold'), bg='#e6e6fa', fg='#4B0082').pack(pady=10)

    # Search Frame
    searchFrame = tk.Frame(root, bg='#e6e6fa')
    searchFrame.pack(pady=5)

    tk.Label(searchFrame, text="Search A Record:", font=("Arial", 12), bg='#e6e6fa').pack(side=tk.LEFT, padx=5)
    
    searchEntry = tk.Entry(searchFrame, font=("Arial", 12), width=40)  # Wider input field
    searchEntry.pack(side=tk.LEFT, padx=5)

    tk.Button(searchFrame, text="Search", font=("Arial", 12, 'bold'), bg='#9370DB', fg='white', command=searchByName).pack(side=tk.LEFT, padx=5)

    # Treeview Frame
    treeFrame = tk.Frame(root)
    treeFrame.pack(pady=10, fill=tk.BOTH, expand=True)

    columns = ("First Name", "Middle Name", "Last Name", "Birthday", "Gender")
    tree = ttk.Treeview(treeFrame, columns=columns, show='headings')

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor=tk.CENTER, width=120)

    tree.pack(fill=tk.BOTH, expand=True)

    # View All Records Button (Now Links to View Records Page)
    tk.Button(root, text="View All Records", font=("Arial", 12, 'bold'), bg='#9370DB', fg='white', command=openViewRecords).pack(pady=10)

# Ensure this module can be imported without running code
if __name__ == "__main__":
    mainWindow = tk.Tk()
    mainWindow.title("Main Window")
    mainWindow.geometry("500x300")

    tk.Button(mainWindow, text="Open Search", command=lambda: searchRecordWindow(mainWindow)).pack(pady=20)

    mainWindow.mainloop()