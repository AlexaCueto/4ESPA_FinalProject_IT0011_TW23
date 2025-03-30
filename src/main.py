import tkinter as tk
from signUp import signUpWindow
from searchRecord import searchRecordWindow
from viewRecord import viewRecordWindow

def main_menu():
    root = tk.Tk()
    root.title("Main Menu")
    root.geometry("700x500")
    root.configure(bg="#e6e6fa")

    tk.Label(root, text="Welcome to User Registration System", font=("Roboto", 18, 'bold'), bg="#e6e6fa", fg="#9370DB").pack(pady=30)
    tk.Label(root, text="What do you want to do for today?", font = ("Roboto", 15, 'italic'), bg="#e6e6fa", fg="#9370DB").pack(pady= 15)

    button_config = {"font": ("Roboto", 14), "bg": "#9370DB", "fg": "white", "width": 15, "height": 1}

    tk.Button(root, text="Sign Up", command=lambda: signUpWindow(root), **button_config).pack(pady=10)
    tk.Button(root, text="Search Records", command=lambda: searchRecordWindow(root), **button_config).pack(pady=10)
    tk.Button(root, text="View Records", command=lambda: viewRecordWindow(root), **button_config).pack(pady=10)
    tk.Button(root, text="Exit", command=root.quit, **button_config).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main_menu()
