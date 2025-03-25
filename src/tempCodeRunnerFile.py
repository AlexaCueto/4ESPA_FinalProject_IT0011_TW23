import tkinter as tk
from signUp import signUpWindow
# from searchRecord import searchRecordWindow
from viewRecord import viewRecordWindow

def main_menu():
    root = tk.Tk()
    root.title("Main Menu")
    root.geometry("400x350")
    root.configure(bg="#e6e6fa")

    tk.Label(root, text="Welcome to the System", font=("Roboto", 18, 'bold'), bg="#e6e6fa", fg="#9370DB").pack(pady=20)

    tk.Button(root, text="Sign Up", font=("Roboto", 14), background='#9370DB', fg="white", command=lambda: signUpWindow(root)).pack(pady=10)
    # tk.Button(root, text="Search Records", font=("Roboto", 14), background='#9370DB', fg="white", command=lambda: searchRecordWindow(root)).pack(pady=10)
    tk.Button(root, text="View Records", font=("Roboto", 14), background='#9370DB', fg="white", command=lambda: viewRecordWindow(root)).pack(pady=10)
    tk.Button(root, text="Search a Record", font=("Roboto", 14), background='#9370DB', fg="white", command=lambda: searchRecordWindow(root)).pack(pady=10)
    tk.Button(root, text="Exit", font=("Roboto", 14), background='#9370DB', fg="white", command=root.quit).pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main_menu()
