from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_input = website_entry.get()
    email_input = email_entry.get()
    password_input = password_entry.get()
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
generate_button = Button(text="Generate Password")
generate_button.grid(row=3,column=2,pady=5)
add_button = Button(text="Add",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)



window.mainloop()