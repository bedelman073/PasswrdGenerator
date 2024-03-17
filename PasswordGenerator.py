# Importing modules
import customtkinter as ctk
import sqlite3
import bcrypt
from PIL import Image
# initalizing a secure database to store passwords and usernames
conn=sqlite3.connect("data.db")
cursor=conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT NOT NULL,
        password TEXT NOT NULL)''')
# setting fonts
font1=("Helvetica",25,"bold")
# creating a window 
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")
window = ctk.CTk()
window.geometry("450x360")
window.title("Login")
header=ctk.CTkLabel(master=window,text="Login to Your Account")
header.pack()
window.mainloop()