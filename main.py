from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    letters_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list.extend(letters_list)
    numbers_list = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list.extend(numbers_list)
    symbols_list = [random.choice(symbols) for _ in range(nr_symbols)]
    password_list.extend(symbols_list)

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_input = website_entry.get()
    email_input = email_entry.get()
    password_input = password_entry.get()
    if len(website_input) == 0 or len(password_input) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_input,message=f"These are the details entered:\nEmail: {email_input} \nPassword: {password_input} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as f:
                f.write(f" {website_input}  | {email_input}  | {password_input}\n")
    website_entry.delete(0,END)
    password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
# Setting Up Window
window = Tk()
window.title("Password Manager")
window.config(pady=50,padx=50)
# Setting Up Canvas
canvas = Canvas(width=200,height=200,highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image= logo_img)
canvas.grid(row=0,column = 1)
#Labels
website_label = Label(text="Website:",font=("Arial",15,"normal"))
website_label.grid(row=1,column=0)
email_label = Label(text="Email/Username:",font=("Arial",15,"normal"))
email_label.grid(row=2,column=0)
password_label = Label(text="Password:",font=("Arial",15,"normal"))
password_label.grid(row=3,column=0)
#Entries
website_entry = Entry(width=35,font=("Arial",15,"normal"),bd=0,fg="black",bg="white")
website_entry.grid(row=1,column=1,columnspan=2)
email_entry = Entry(width=35,font=("Arial",15,"normal"),bd=0,fg="black",bg="white")
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"stephenmasih39@gmail.com")
password_entry = Entry(width=21,font=("Arial",15,"normal"),bd=0,fg="black",bg="white")
password_entry.grid(row=3,column=1)
#Buttons
generate_button = Button(text="Generate Password",command=generate_password)
generate_button.grid(row=3,column=2,pady=5)
add_button = Button(text="Add",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)



window.mainloop()