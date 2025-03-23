from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
import os
import csv

def signUp():
    firstName = firstNameEntry.get().strip()
    middleName = middleNameEntry.get().strip()
    lastName = lastNameEntry.get().strip()
    birthday = birthdayEntry.get().strip()
    gender = genderEntry.get().strip()
    
firstName = StringVar()
middleName = StringVar()
lastName = StringVar()
birthday = StringVar()
gender = StringVar()

#Validate required fields
if not firstName or not middleName or not lastName or not birthday or not gender:
    messagebox.showerror("This field is required. Please fill in required inputs.")
    return

#Valide first name
if not firstName.isalpha():
    messagebox.showerror("First name must be alphabetic characters.")
    return

#Validate middle name
if not middleName.isalpha():
    messagebox.showerror("Middle name must be alphabetic characters.")
    return

#Validate last name
if not lastName.isalpha():
    messagebox.showerror("Last name must be alphabetic characters.")
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

def load_records(filename):
    """Load records from a CSV file."""
    try:
        if not os.path.exists(filename):
            raise FileNotFoundError("Error: The records file does not exist.")
        
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            records = list(reader)

            if not records:
                raise ValueError("Error: The records file is empty.")

            return records

    except FileNotFoundError as e:
        print(e)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"Unexpected error: {e}")

    return []

def display_all_records(records):
    """Display all records."""
    if not records:
        print("No records available.")
        return

    print("\nExisting Records:")
    for record in records:
        print(f"First Name: {record['First name']}, Middle Name: {record['Middle name']}, "
              f"Last Name: {record['Last name']}, Birthday: {record['Birthday']}, Gender: {record['Gender']}")
    print()

def search_by_last_name(records, last_name):
    """Search for a record by last name."""
    try:
        if not last_name.strip():
            raise ValueError("Search value cannot be empty.")

        results = [record for record in records if record.get("Last name", "").strip().lower() == last_name.strip().lower()]

        if results:
            print("\nRecord(s) found:")
            for record in results:
                print(f"First Name: {record['First name']}, Middle Name: {record['Middle name']}, "
                      f"Last Name: {record['Last name']}, Birthday: {record['Birthday']}, Gender: {record['Gender']}")
        else:
            print("No matching record found.")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def search_records():
    """Handles searching and displaying records."""
    filename = "records.csv"
    records = load_records(filename)

    if not records:
        return

    while True:
        print("\nOptions:")
        print("1. View all records")
        print("2. Search a record by last name")
        print("3. Exit")

        try:
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                display_all_records(records)
            elif choice == "2":
                last_name = input("Enter last name to search: ").strip()
                search_by_last_name(records, last_name)
            elif choice == "3":
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    search_records()
