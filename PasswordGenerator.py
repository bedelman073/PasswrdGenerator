# Importing modules
import customtkinter as ctk
from PIL import Image
import hashlib
import string
import secrets
import os
import pyzipper

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
    # creating a screen that allows the user to create a new account by entering a username and password
    global account_creation_frame,homepage_frame
    if homepage_frame:
        homepage_frame.destroy()
    account_creation_frame = ctk.CTkFrame(window, width=275, height=450, bg_color="transparent")
    account_creation_frame.pack(side="right", fill="both", expand=True)
    account_creation_frame.pack_propagate(False)
    prompt = ctk.CTkLabel(account_creation_frame, text="Create Your Account", font=font1)
    prompt.pack(pady=12, anchor="n")
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

# function that lets the user chose what they want to do with the program 
def user_account_homepage():
    # clearing all old widgets
    for widget in window.winfo_children():
        widget.destroy()
    pack_image()
    user_greeting=ctk.CTkLabel(window,text=f"Welcome, {username}!",font=font1)
    user_greeting.pack(pady=10)
    option_frame = ctk.CTkFrame(window, width=275, height=450, bg_color="transparent")
    option_frame.pack(side="right", fill="both", expand=True)
    option_frame.pack_propagate(False)
    generate_password_btn = ctk.CTkButton(option_frame, command=password_generation_screen, width=225, height=35, corner_radius=5, text="Generate Password", fg_color="#a649ff")
    generate_password_btn.pack(pady=20)
    exp_passwords_btn = ctk.CTkButton(option_frame, command=zip_and_secure(f"{username}PSWRDS.txt",f"Secured{username}PSWRDS.zip"), width=225, height=35, corner_radius=5, text="Export to Secure ZIP", fg_color="#a649ff")
    exp_passwords_btn.pack(pady=20)
    logout_btn = ctk.CTkButton(option_frame, command=lambda: logout(), width=225, height=35, corner_radius=5, text="Logout", fg_color="#a649ff")
    logout_btn.pack(pady=20)

# creating a screen that allows the user to chose what kind of password they want to generate
def password_generation_screen():
    for widget in window.winfo_children():
        widget.destroy()
    pack_image()
    password_option_frame = ctk.CTkFrame(window, width=275, height=450, bg_color="transparent")
    password_option_frame.pack(side="right", fill="both", expand=True)
    password_option_frame.pack_propagate(False)
    password_header=ctk.CTkLabel(password_option_frame,text=f"Password Generator",font=font1)
    password_header.pack(pady=10)
    password_subheader=ctk.CTkLabel(password_option_frame,text="Please Select an Option",font=font3)
    password_subheader.pack(pady=1)             # these two need commands 
    randpass_btn=ctk.CTkButton(password_option_frame, command=lambda: rand_password_screen(),width=225, height=35, corner_radius=5, text="Random Password", fg_color="#a649ff")
    randpass_btn.pack(pady=15)
    informedpass_btn=ctk.CTkButton(password_option_frame, command=lambda: informed_password_screen(), width=225, height=35, corner_radius=5, text="Informed Password", fg_color="#a649ff")
    informedpass_btn.pack(pady=15)
    return_to_selection_btn=ctk.CTkButton(password_option_frame, command=lambda: user_account_homepage(), width=225, height=35, corner_radius=5, text="Return to Selection", fg_color="#a649ff")
    return_to_selection_btn.pack(pady=15)

def on_slider_change(value):
    # function that changes the label on the screen to tell the user how many characters their password will be 
    global password_length
    password_length=round(value)
    num_disp.configure(text=str(password_length)+" Character(s)")

def rand_password_screen():
    # creating a screen that allows the user to chose how long they want their password to be using a slider widget, and giving them a submit button
    global slider_frame,slider,num_disp,pass_query
    for widget in window.winfo_children():
        widget.destroy()
    pack_image()
    slider_frame = ctk.CTkFrame(window, width=275, height=450, bg_color="transparent")
    slider_frame.pack(side="right", fill="both", expand=True)
    slider_frame.pack_propagate(False)
    slider_heading = ctk.CTkLabel(slider_frame,text="Chose Password\nLength",font=font1)
    slider_heading.pack(pady=10)
    slider = ctk.CTkSlider(slider_frame,command=on_slider_change,width=225,height=20,number_of_steps=10, from_=5,to=15,progress_color="#a649ff",button_color="grey")
    slider.pack(pady=10)
    slider.set(5)
    num_disp = ctk.CTkLabel(slider_frame,text="5 Character(s)",font=font1)
    num_disp.pack(pady=10)
    pass_query=ctk.CTkEntry(slider_frame,placeholder_text="What is this password for?",text_color="white", placeholder_text_color="white",width=225, height=35, corner_radius=5,border_color="#a649ff")
    pass_query.pack(pady=10)
    gen_pwd_button=ctk.CTkButton(slider_frame,command=lambda: randomPass(password_length),width=225, height=35, corner_radius=5, text="Generate!", fg_color="#a649ff")
    gen_pwd_button.pack(pady=10)

def informed_password_screen():
    # creating a screen that allows the user to input information about their informed password, and holds the button for submission
    global informed_frame,informed_entry,informed_pass_query
    for widget in window.winfo_children():
        widget.destroy()
    pack_image()
    informed_frame = ctk.CTkFrame(window, width=275, height=450, bg_color="transparent")
    informed_frame.pack(side="right", fill="both", expand=True)
    informed_frame.pack_propagate(False)
    informed_heading = ctk.CTkLabel(informed_frame,text="Chose Password\nInclusion",font=font1)
    informed_heading.pack(pady=10)
    informed_entry = ctk.CTkEntry(informed_frame,placeholder_text="Enter your inclusion here",text_color="white", placeholder_text_color="white",width=225, height=35, corner_radius=5,border_color="#a649ff")
    informed_entry.pack(pady=10)
    informed_pass_query=ctk.CTkEntry(informed_frame,placeholder_text="What is this password for?",text_color="white", placeholder_text_color="white",width=225, height=35, corner_radius=5,border_color="#a649ff")
    informed_pass_query.pack(pady=10)
    gen_inf_pwd_button=ctk.CTkButton(informed_frame,command=lambda: informedPass(entry=informed_entry.get()),width=225, height=35, corner_radius=5, text="Generate!", fg_color="#a649ff")
    gen_inf_pwd_button.pack(pady=10)
    
def logout():
    # removing all widgets and returning home
    global window
    for widget in window.winfo_children():
        widget.destroy()
    pack_image()
    homepage()

def zip_and_secure(file_to_zip,output_zip_file):
    # checks if the file exists, if it does, the data from the file is written to a zip file protected by their account password
    if not os.path.exists(file_to_zip):
        return
    with open(file_to_zip, 'rb') as file:
        data = file.read()
    with pyzipper.AESZipFile(output_zip_file,'w', compression=pyzipper.ZIP_LZMA, encryption=pyzipper.WZ_AES) as zipf:
        zipf.setpassword(password.encode()) 
        zipf.writestr(file_to_zip, data)


# creating a function that packs a frame to hold an image to the left side of the program
def pack_image():
    global window,left_frame
    left_frame = ctk.CTkFrame(window, width=275, height=450, bg_color="transparent")
    left_frame.pack(side="left", fill="both", expand=True)
    left_frame.pack_propagate(False)
    img1 = ctk.CTkImage(light_image=Image.open(r"menuicon.PNG"), dark_image=Image.open(r"menuicon.PNG"), size=(275, 450))
    img_lab = ctk.CTkLabel(left_frame, text="", image=img1)
    img_lab.pack()

# funciton to get the homescreen username and password, and checks the credentials 
def get_data():
    global username, password
    username = username_ent.get()
    password = password_ent.get()
    with open("hashed_pws.txt","r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(":")
            if username == stored_username and encrypt(password) == stored_password:
                loginlabel = ctk.CTkLabel(homepage_frame,text="Logging in...",text_color="#66ff00",font=font3)
                loginlabel.pack()
                homepage_frame.update()  
                homepage_frame.after(1500, lambda: user_account_homepage())  
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
# function for random password creation      
def randomPass(pwlength):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(1,pwlength+1))
    with open(f"{username}PSWRDS.txt","a") as file:
        file.write(f"{pass_query.get()}:{password}\n")
        file.close()
    show_password(password)

# function for informed password creation
def informedPass(entry):
    password = ''
    translationdict = {'e':'3','E':'3','Z':'2','l':'1','L':'1','o':'0','O':'0','S':'5','s':'5','a':'@'}
    pwordalphabet = (string.punctuation)
    pwordalphabet = pwordalphabet.replace('&','0')
    for i in range(len(entry)):
        if (entry[i] in translationdict):
            entry = entry.replace(entry[i],translationdict[entry[i]],i-1)
   
    frontComponent = ''.join(secrets.choice(pwordalphabet) for i in range(2))
    backComponent = ''.join(secrets.choice(pwordalphabet) for i in range(2))
    password = ''.join((frontComponent,entry,backComponent))
    with open(f"{username}PSWRDS.txt","a") as file:
        file.write(f"{informed_pass_query.get()}:{password}\n")
        file.close()
    show_password(password)

# creating a screen that allows the user to see the password generated for them
def show_password(pswrd):
    for widget in window.winfo_children():
        widget.destroy()
    pack_image()
    show_frame = ctk.CTkFrame(window, width=275, height=450, bg_color="transparent")
    show_frame.pack(side="right", fill="both", expand=True)
    show_frame.pack_propagate(False)
    pwd_header = ctk.CTkLabel(show_frame,text="Your Password:",font=font1)
    pwd_header.pack(pady=10)
    pwd = ctk.CTkLabel(show_frame,text=f"{pswrd}",font=font1,text_color="#a649ff")
    pwd.pack(pady=10)
    location_header = ctk.CTkLabel(show_frame,text=f"This password is stored in\n{username}PWDS.txt.\nVisit the homepage to protect this file.",font=font3)
    location_header.pack(pady=10)
    home_btn = ctk.CTkButton(show_frame,command=lambda: user_account_homepage(),width=225, height=35, corner_radius=5, text="Return Home", fg_color="#a649ff")
    home_btn.pack(pady=10)

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
window.resizable(width=False, height=False)
# jumpstarting the program 
homepage()
pack_image()
# running an instance of mainloop to accept new inputs 
window.mainloop()