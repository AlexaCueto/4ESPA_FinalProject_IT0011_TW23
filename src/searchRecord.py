import tkinter as tk #gui
from tkinter import ttk, messagebox
from fileHandler import loadRecords #csv file
from viewRecord import viewRecordWindow

RECORDS_FILE = "records.csv"

def searchRecordWindow(mainWindow):
    #Creates the search record window.
    root = tk.Toplevel(mainWindow)
    root.title("Search A Record")
    root.geometry("700x500")
    root.configure(bg='#e6e6fa')

    def searchByName():
        #Search for a record and display results.
        searchCategory = searchType.get()
        searchValue = searchEntry.get().strip().lower()
        
        if not searchValue:
            messagebox.showerror("Error", "Search value cannot be empty.")
            root.destroy()  #Close window on error
            return

        records = loadRecords(RECORDS_FILE)
        if not records:
            messagebox.showinfo("No Records", "No records found in the system.")
            root.destroy()  #Close window on error
            return
        
        if searchCategory == "First Name":
            results = [
                record for record in records
                if record.get("First Name", "").strip().lower().startswith(searchValue)
            ]
        elif searchCategory == "Middle Name":
            results = [
                record for record in records
                if record.get("Middle Name", "").strip().lower().startswith(searchValue)
            ]
        elif searchCategory == "Last Name":
            results = [
            record for record in records
            if record.get("Last Name", "").strip().lower().startswith(searchValue)
        ]
        
        tree.delete(*tree.get_children())
        if results:
            for record in results:
                tree.insert("", "end", values=(record["First Name"], record["Middle Name"], record["Last Name"], record["Birthday"], record["Gender"]))
        else:
            messagebox.showinfo("No Record Found", "No matching record found.")
            root.destroy()  #Close window on error

    def openViewRecords():
        """Open the view all records window."""
        viewRecordWindow(mainWindow)

    def goBack():
        """Return to the main menu."""
        root.destroy()  #Close search window

    #Title Label
    tk.Label(root, text="Records Viewer", font=("Roboto", 18, 'bold'), bg='#e6e6fa', fg='#4B0082').pack(pady=10)

    #Search Frame
    searchFrame = tk.Frame(root, bg='#e6e6fa')
    searchFrame.pack(pady=5)

    tk.Label(searchFrame, text="Search A Record:", font=("Roboto", 12), bg='#e6e6fa').pack(side=tk.LEFT, padx=5)
    
    #Dropdown to select search type (First Name or Last Name)
    searchType = ttk.Combobox(searchFrame, values=["First Name", "Middle Name", "Last Name"], font=("Roboto", 12), state="readonly")
    searchType.set("Last Name")  # Default to Last Name
    searchType.pack(side=tk.LEFT, padx=5)

    searchEntry = tk.Entry(searchFrame, font=("Roboto", 12), width=30)
    searchEntry.pack(side=tk.LEFT, padx=5)

    tk.Button(searchFrame, text="Search", font=("Roboto", 12, 'bold'), bg='#9370DB', fg='white', command=searchByName).pack(side=tk.LEFT, padx=5)

    #Treeview Frame
    treeFrame = tk.Frame(root)
    treeFrame.pack(pady=10, fill=tk.BOTH, expand=True)

    columns = ("First Name", "Middle Name", "Last Name", "Birthday", "Gender")
    tree = ttk.Treeview(treeFrame, columns=columns, show='headings')

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor=tk.CENTER, width=120)

    tree.pack(fill=tk.BOTH, expand=True)

    #Buttons Frame
    buttonFrame = tk.Frame(root, bg='#e6e6fa')
    buttonFrame.pack(pady=10)

    tk.Button(buttonFrame, text="View All Records", font=("Roboto", 12, 'bold'), bg='#9370DB', fg='white', command=openViewRecords).pack(side=tk.LEFT, padx=10)
    tk.Button(buttonFrame, text="Back", font=("Roboto", 12, 'bold'), bg='#8B0000', fg='white', command=goBack).pack(side=tk.LEFT, padx=10)