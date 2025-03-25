import tkinter as tk
from tkinter import ttk, messagebox
import csv

def open_sign_up_window():
    sign_up_window = tk.Toplevel()  # Create a new top-level window
    sign_up_window.title("Sign Up")
    sign_up_window.geometry("600x500")
    sign_up_window.configure(bg='#e6e6fa')