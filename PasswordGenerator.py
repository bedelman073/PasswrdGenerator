import customtkinter as ctk
from PIL import Image
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")
window = ctk.CTk()
window.geometry("600x440")
window.title("Login")
header=ctk.CTkLabel(master=window,text="Login to Your Account")
header.pack()
window.mainloop()