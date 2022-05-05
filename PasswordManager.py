from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
    password = ""

    # Clear text
    password_entry.delete(0, END)

    # Fill letters
    for _ in range(12):
        password += (random.choice(alphabet))

    # Replace some letters with upper case
    for _ in range(random.randint(1, 5)):
        random_letter = password[random.randint(1, 9)]
        password = password.replace(random_letter, random_letter.upper())

    # Replace some lower case letters with numbers
    for _ in range(random.randint(1, 5)):
        num = str(random.randint(0, 9))
        random_letter = password[random.randint(1, 9)]
        if random_letter.islower():
            password = password.replace(random_letter, num)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():

    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    empty = False

    for _ in website, username, password:
        if _ == "":
            empty = True

    if empty:
        messagebox.showinfo("Alert", "Enter all details before adding password")
    else:
        saving = messagebox.askokcancel(title=website, message=f"Username: {username} \nPassword: {password} \n\nSave details?")
        if saving:
            with open("data.txt", mode="a") as password_list:
                password_list.write(f"\n{website}, {username}, {password}")

        website_entry.delete(0, END)
        password_entry.delete(0, END)
        website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=50, pady=20)
window.title("Password Manager")


logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)


# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

username_entry = Entry(width=35)
username_entry.insert(0, "my_email@email.com")
username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=17)
password_entry.grid(column=1, row=3)

# Buttons
generate_password = Button(text="Generate Password", command=generate)
generate_password.grid(column=2,  row=3)

add = Button(text="Add", width=33, command=save_password)
add.grid(column=1, row=4, columnspan=2)



window.mainloop()