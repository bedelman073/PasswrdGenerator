
# Importing modules
import customtkinter as ctk
from PIL import Image
import hashlib
import string
import secrets
import random
import time

# Program functions/constants

def homepage():
    global window,homepage_frame,left_frame,username_ent,password_ent
    # Creating frames
    homepage_frame = ctk.CTkFrame(window, width=275, height=450, bg_color="transparent")
    homepage_frame.pack(side="right", fill="both", expand=True)
    homepage_frame.pack_propagate(False)
    # Creating and packing header
    header = ctk.CTkLabel(homepage_frame, text="Password Generator", font=font1, text_color="white")
    header.pack(pady=12, anchor="n")
    # Creating and packing uandp frame
    uandp_frame = ctk.CTkFrame(homepage_frame, width=200, height=200, fg_color="transparent")
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
    submit2 = ctk.CTkButton(uandp_frame, command=create_account, width=225, height=35,
                            corner_radius=5, text="I Don't Have A Profile", fg_color="#a649ff")
    submit2.pack(pady=5)

def create_account():
    # Destroying the old frame and adding a new one
    global account_creation_frame,homepage_frame
    if homepage_frame:
        homepage_frame.destroy()
    account_creation_frame = ctk.CTkFrame(window, width=275, height=450, bg_color="transparent")
    account_creation_frame.pack(side="right", fill="both", expand=True)
    # Prompting for data entry
    account_creation_frame.pack_propagate(False)
    prompt = ctk.CTkLabel(account_creation_frame, text="Create Your Account", font=font1)
    prompt.pack(pady=12, anchor="n")
    # Creating a new uandp frame and new data entries 
    uandp_frame = ctk.CTkFrame(account_creation_frame, width=200, height=300, fg_color="transparent")
    uandp_frame.pack()
    global newusername_ent, newpassword_ent
    newusername_ent = ctk.CTkEntry(uandp_frame, width=250, height=45, placeholder_text="Username",
                                text_color="white", placeholder_text_color="white", border_color="#c74afe")
    newusername_ent.pack(padx=20, pady=8)
    newpassword_ent = ctk.CTkEntry(uandp_frame, width=250, height=45, placeholder_text="Password",
                                text_color="white", placeholder_text_color="white", border_color="#c74afe", show="*")
    newpassword_ent.pack(padx=20, pady=8)
    submit = ctk.CTkButton(uandp_frame, command=lambda:check_data(account_creation_frame), width=225, height=35, corner_radius=5, text="Submit",
                       fg_color="#a649ff")
    submit.pack(pady=5),
    returnhomebutton = ctk.CTkButton(account_creation_frame,width=225, command=lambda:returnhome(), height=35, corner_radius=5, text="Return Home",
                       fg_color="#a649ff")
    returnhomebutton.pack()

def user_account_homepage():
    for widget in window.winfo_children():
        widget.destroy()

# creating a function that packs a frame to hold an image to the left side of the program
def pack_image():
    global window,left_frame
    left_frame = ctk.CTkFrame(window, width=275, height=450, bg_color="transparent")
    left_frame.pack(side="left", fill="both", expand=True)
    left_frame.pack_propagate(False)

# funciton to get the homescreen username and password, and checks the credentials 
def get_data():
    global username, password
    username = username_ent.get()
    password = password_ent.get()
    with open("hashed_pws.txt","r") as file:
        for line in file:
            if encrypt(password) in line:
                loginlabel = ctk.CTkLabel(homepage_frame,text="Logging in...",text_color="#66ff00")
                loginlabel.pack()
                homepage_frame.update()  
                homepage_frame.after(3000, lambda: user_account_homepage())  
                return
        else:
            errorlabel = ctk.CTkLabel(homepage_frame,text="Username or Password does not match",text_color="red",font=font3)
            errorlabel.pack()
            return

# function that checks if the user is already in the system, and records them as a new user and encrypts their password if they are not 
def check_data(frame):
    newusername = newusername_ent.get()
    newpassword = newpassword_ent.get()
    with open("hashed_pws.txt", "r") as file:
        for line in file:
            stored_username, _ = line.strip().split(":")  # Splitting the line using ":" as delimiter
            if newusername == stored_username:
                errorlabel = ctk.CTkLabel(frame, text="User is already in the database", text_color="red",font=font3)
                errorlabel.pack()
                return
    encrypted_password = encrypt(newpassword)
    with open("hashed_pws.txt", "a") as file:
        file.write(f"{newusername}:{encrypted_password}\n")  # Using ":" as delimiter
    successlabel = ctk.CTkLabel(account_creation_frame, text="Registration successful!\nReturning to Homepage...", text_color="#66ff00",font=font3)
    successlabel.pack(pady=8)
    frame.after(3000, lambda: frame.destroy())
    homepage()

# password hashing function that stores encrypted data in a .txt file
def encrypt(password):
    hashed_password = hashlib.sha256()
    hashed_password.update(password.encode('utf-8'))
    encrypted_password = hashed_password.hexdigest()
    return encrypted_password

def returnhome():
    global homepage_frame, account_creation_frame
    if account_creation_frame:
        account_creation_frame.destroy()
        homepage()

# # # # # # # PASSWORD FUNCTIONS # # # # # # # # 
        
def randomPass():
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(12))
    return(password)

def informedPass():
    word = str(input("Please input a word:"))
    password = ''
    translationdict = {'e':'3','E':'3','Z':'2','l':'1','L':'1','o':'0','O':'0','S':'5','s':'5','a':'@'}
    pwordalphabet = (string.punctuation)
    pwordalphabet = pwordalphabet.replace('&','0')
    for i in range(len(word)):
        if (word[i] in translationdict):
            word = word.replace(word[i],translationdict[word[i]],i-1)
   
    frontComponent = ''.join(secrets.choice(pwordalphabet) for i in range(2))
    backComponent = ''.join(secrets.choice(pwordalphabet) for i in range(2))
    password = ''.join((frontComponent,word,backComponent))

    return(password)


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
# jumpstarting the program 
homepage()
pack_image()
# Creating and packing image
img1 = ctk.CTkImage(light_image=Image.open(r"menuicon.PNG"), dark_image=Image.open(r"menuicon.PNG"), size=(275, 450))
img_lab = ctk.CTkLabel(left_frame, text="", image=img1)
img_lab.pack()

window.mainloop()