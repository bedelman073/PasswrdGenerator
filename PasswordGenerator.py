# Program functions/constants

# password hashing function that stores encrypted data in a .txt file
def encrypt(password):
    hashed_password = hashlib.sha256()
    hashed_password.update(password.encode('utf-8'))
    encrypted_password = hashed_password.hexdigest()
    return encrypted_password

def homepage(root):
    
    global right_frame,left_frame,username_ent,password_ent
    
    # Creating frames
    right_frame = ctk.CTkFrame(root, width=275, height=450, bg_color="transparent")
    right_frame.pack(side="right", fill="both", expand=True)
    right_frame.pack_propagate(False)
    left_frame = ctk.CTkFrame(root, width=275, height=450, bg_color="transparent")
    left_frame.pack(side="left", fill="both", expand=True)
    left_frame.pack_propagate(False)

    # Creating and packing header
    header = ctk.CTkLabel(right_frame, text="Password Generator", font=font1, text_color="white")
    header.pack(pady=12, anchor="n")

    # Creating and packing uandp frame
    uandp_frame = ctk.CTkFrame(right_frame, width=200, height=200, fg_color="transparent")
    uandp_frame.pack()

    # Creating and packing entry widgets
    username_ent = ctk.CTkEntry(uandp_frame, width=250, height=45, placeholder_text="Username",
                                text_color="white", placeholder_text_color="white", border_color="#c74afe")
    username_ent.pack(padx=20, pady=8)
    password_ent = ctk.CTkEntry(uandp_frame, width=250, height=45, placeholder_text="Password",
                                text_color="white", placeholder_text_color="white", border_color="#c74afe", show="*")
    password_ent.pack(padx=20, pady=8)

    # Creating buttons
    submit = ctk.CTkButton(uandp_frame, command=get_data, width=225, height=35, corner_radius=5, text="Login",
                        fg_color="#a649ff")
    submit.pack(pady=5)
    submit2 = ctk.CTkButton(uandp_frame, command=lambda: create_account(right_frame), width=225, height=35,
                            corner_radius=5, text="I Don't Have A Profile", fg_color="#a649ff")
    submit2.pack(pady=5)

def create_account(frame):
    # Destroying the old frame and adding a new one
    frame.destroy()
    global right_frame2
    right_frame2 = ctk.CTkFrame(window, width=275, height=450, bg_color="transparent")
    right_frame2.pack(side="right", fill="both", expand=True)
    # Prompting for data entry
    right_frame2.pack_propagate(False)
    prompt = ctk.CTkLabel(right_frame2, text="Create Your Account", font=font1)
    prompt.pack(pady=12, anchor="n")
    # Creating a new uandp frame and new data entries 
    uandp_frame = ctk.CTkFrame(right_frame2, width=200, height=300, fg_color="transparent")
    uandp_frame.pack()
    global newusername_ent, newpassword_ent
    newusername_ent = ctk.CTkEntry(uandp_frame, width=250, height=45, placeholder_text="Username",
                                text_color="white", placeholder_text_color="white", border_color="#c74afe")
    newusername_ent.pack(padx=20, pady=8)
    newpassword_ent = ctk.CTkEntry(uandp_frame, width=250, height=45, placeholder_text="Password",
                                text_color="white", placeholder_text_color="white", border_color="#c74afe", show="*")
    newpassword_ent.pack(padx=20, pady=8)
    submit = ctk.CTkButton(uandp_frame, command=lambda:check_data(right_frame2), width=225, height=35, corner_radius=5, text="Submit",
                       fg_color="#a649ff")
    submit.pack(pady=5),
    returnhomebutton = ctk.CTkButton(right_frame2,width=225, command=lambda:returnhome(right_frame2,window), height=35, corner_radius=5, text="Return Home",
                       fg_color="#a649ff")
    returnhomebutton.pack()

def returnhome(frame,root):
    frame.destroy()
    homepage(root)

# funciton to get the homescreen username and password, and checks the credentials 
def get_data():
    global username, password
    username = username_ent.get()
    password = password_ent.get()
    with open("hashed_pws.txt","r") as file:
        for line in file:
            if encrypt(password) in line:
                loginlabel = ctk.CTkLabel(right_frame,text="Logging in...",text_color="#66ff00")
                loginlabel.pack()
                return
        else:
            errorlabel = ctk.CTkLabel(right_frame,text="Username or Password does not match",text_color="red",font=font3)
            errorlabel.pack()
            return

# function that checks if the user is already in the system, and records them as a new user and encrypts their password if they are not 
def check_data(frame):
    global newusername, newpassword
    newusername = newusername_ent.get()
    newpassword = newpassword_ent.get()
    with open("hashed_pws.txt", "r") as file:
        for line in file:
            if newusername in line:
                errorlabel = ctk.CTkLabel(frame, text="User is already in the database", text_color="red",font=font3)
                errorlabel.pack()
                return
    encrypted_password = encrypt(newpassword)
    with open("hashed_pws.txt", "a") as file:
        file.write(f"[{newusername},{encrypted_password}]\n")
    successlabel = ctk.CTkLabel(right_frame2, text="Registration successful!\nReturning to Homepage...", text_color="#66ff00",font=font3)
    successlabel.pack(pady=8)
    frame.after(3000, lambda: frame.destroy())
    homepage(window)


# Importing modules
import customtkinter as ctk
from PIL import Image
import hashlib

# Setting fonts
font1 = ("Helvetica Neue", 25, "bold")
font2 = ("Helvetica Neue", 15, "bold")
font3 = ("Helvetica Neue", 12, "bold")
# Creating a window
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")
window = ctk.CTk()
window.geometry("550x300")
window.title("Password Generator")
window.resizable(False, False)
homepage(window)
# Creating and packing image
img1 = ctk.CTkImage(light_image=Image.open(r"menuicon.PNG"), dark_image=Image.open(r"menuicon.PNG"), size=(275, 450))
img_lab = ctk.CTkLabel(left_frame, text="", image=img1)
img_lab.pack()

window.mainloop()