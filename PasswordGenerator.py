# program functions/constants
user_data={}
global userdata
def get_data():
    global username
    global password
    username=username_ent.get()
    password=password_ent.get()
def create_account(frame):
    frame.destroy()
    right_frame = ctk.CTkFrame(window, 
                           width=275, 
                           height=450,
                           bg_color="transparent")
    right_frame.pack(side="right", 
                    fill="both", 
                    expand=True)
    right_frame.pack_propagate(False)
    prompt = ctk.CTkLabel(right_frame,text="Sign Up")
    prompt.pack(anchor="n")

# Importing modules
import customtkinter as ctk
from PIL import Image

# Setting fonts
font1 = ("Helvetica Neue", 25, "bold")

# Creating a window
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")
window = ctk.CTk()
window.geometry("550x300")
window.title("Password Generator")
window.resizable(False, False)

# Creating frames
right_frame = ctk.CTkFrame(window, 
                           width=275, 
                           height=450,
                           bg_color="transparent")
right_frame.pack(side="right", 
                 fill="both", 
                 expand=True)
right_frame.pack_propagate(False)
left_frame = ctk.CTkFrame(window, 
                          width=275, 
                          height=450,
                          bg_color="transparent")
left_frame.pack(side="left", 
                fill="both", 
                expand=True)
left_frame.pack_propagate(False)

# Creating and packing header
header = ctk.CTkLabel(right_frame, 
                      text="Password Generator", 
                      font=font1,text_color="white")
header.pack(pady=12,
            anchor="n")

# Creating and packing uandp frame
uandp_frame = ctk.CTkFrame(right_frame, 
                           width=200, 
                           height=200,
                           fg_color="transparent")
uandp_frame.pack()

# Creating and packing entry widgets
username_ent = ctk.CTkEntry(uandp_frame, 
                            width=250,
                            height=45, 
                            placeholder_text="Username",
                            text_color="white",
                            placeholder_text_color="white",
                            border_color="#c74afe")
username_ent.pack(padx=20,pady=15)
password_ent = ctk.CTkEntry(uandp_frame, 
                            width=250,
                            height=45, 
                            placeholder_text="Password",
                            text_color="white",
                            placeholder_text_color="white",
                            border_color="#c74afe",
                            show="*")
password_ent.pack(padx=20,
                  pady=15)
submit = ctk.CTkButton(uandp_frame, 
                       command=get_data,
                       width=225, 
                       height=35, 
                       corner_radius=5,
                       text="Login",
                       fg_color="#a649ff")
submit.pack(pady=5)
submit2 = ctk.CTkButton(uandp_frame, 
                        command=lambda:create_account(right_frame),
                        width=225, 
                        height=35, 
                        corner_radius=5,
                        text="I Don't Have A Profile", 
                        fg_color="#a649ff")
submit2.pack(pady=5)

# Creating and packing image
img1 = ctk.CTkImage(light_image=Image.open(r"menuicon.PNG"), 
                    dark_image=Image.open(r"menuicon.PNG"), 
                    size=(275, 450))
img_lab = ctk.CTkLabel(left_frame, 
                       text="", 
                       image=img1)
img_lab.pack()

window.mainloop()