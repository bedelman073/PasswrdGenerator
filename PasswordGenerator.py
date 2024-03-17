# Importing modules
import customtkinter as ctk
from PIL import Image

# setting fonts
font1 = ("Helvetica", 20, "bold")

# creating a window
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")
window = ctk.CTk()
window.geometry("550x450")
window.title("Login")

# Creating frames
right_frame = ctk.CTkFrame(window,width=275, height=450)
right_frame.pack(side="right",fill="both",expand=True)
left_frame = ctk.CTkFrame(window, width=275, height=450)
left_frame.pack(side="left",fill="both",expand=True)

# Creating and packing header
header = ctk.CTkLabel(right_frame, text="Secure Password Generator", font=font1)
header.pack(anchor="n")

# Creating and packing entry widgets
username_ent = ctk.CTkEntry(right_frame, placeholder_text="Username")
username_ent.pack(pady=10)
password_ent = ctk.CTkEntry(right_frame, placeholder_text="Password")
password_ent.pack()
submit = ctk.CTkButton(right_frame,width=50,height=10,corner_radius=5)
submit.pack(pady=30)
# Creating and packing image
img1 = ctk.CTkImage(light_image=Image.open(r"C:\Users\Ben Edelman\PasswrdGenerator\menuicon.jpg"), dark_image=Image.open(r"C:\Users\Ben Edelman\PasswrdGenerator\menuicon.jpg"), size=(275, 450))
img_lab = ctk.CTkLabel(left_frame, text="", image=img1)
img_lab.pack()

window.mainloop()
