from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generatePassword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char    
    password_entry.delete(0,END)
    password_entry.insert(0,password)
    pyperclip.copy(password)
#-----------------------------RETRIEVE PASSWORD AND OTHER DETAILS------------#
def retrieve_details():
    curr_entry = website_entry.get()
    if(len(curr_entry)==0):
        messagebox.showinfo(title="Error",message = "Please fill out the website field")
    else:
        try:
            with(open("file.json",mode = "r") as file):
               data = json.load(file)
               email = data[curr_entry]["email"]
               password = data[curr_entry]["password"]   
        except (FileNotFoundError,KeyError):
            messagebox.showinfo(title="Error",message="The existing website details does not exist")
        else:
            messagebox.showinfo(title=curr_entry,message = f"Email: {email}\nPassword: {password}")

                   


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_details():
    website = website_entry.get().lower()
    email = email_entry.get().lower()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please fill out all the fields")
        return

    try:
        with open("file.json", "r") as read_file:
            data = json.load(read_file)
    except FileNotFoundError:
        data = {}
    except json.JSONDecodeError:
        # Handles the case where file.json exists but is empty or invalid
        data = {}

    data.update(new_data)

    with open("file.json", "w") as write_file:
        json.dump(data, write_file, indent=4)

    website_entry.delete(0, END)
    password_entry.delete(0, END)
    website_entry.focus()
    messagebox.showinfo(title="Success", message="Details saved successfully!")         

            

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)
img= PhotoImage(file = "logo.png")
canvas = Canvas(window,width = 200,height = 200)
canvas.create_image(100,100,image= img)
canvas.grid(row = 0,column = 1)



website_label = Label(text = "Website: ")
website_label.grid(row = 1,column = 0)
email_label = Label(text = "Email/Username: ")
email_label.grid(row= 3,column = 0)
password_label = Label(text = "Password: ")
password_label.grid(row = 4, column = 0)



website_entry = Entry(width = 35)
website_entry.focus()
website_entry.grid(row = 1,column = 1,columnspan = 2)
email_entry = Entry(width = 35)
email_entry.grid(row = 3,column = 1,columnspan = 2)
email_entry.insert(0,"rudraksh.padhi@gmail.com")
password_entry = Entry(width = 35)
password_entry.grid(row = 4,column = 1,columnspan = 2)


gen_pass_button = Button(text = "Generate Password",command = generatePassword)
gen_pass_button.grid(row = 5,column = 2,sticky="w")
add_button = Button(text = "Add",width = 30,command = add_details)
add_button.grid(row = 6,column = 1,columnspan = 2)
search_button = Button(text = "Search",width = 14,command = retrieve_details)
search_button.grid(row = 2,column = 2)
window.mainloop() 