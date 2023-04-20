from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


def find():
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data found.")
    else:
        if web_input.get() in data:
            messagebox.showinfo(title=web_input.get(), message=f"Email: {data[web_input.get()]['email']}"
                                                               f"\nPassword: {data[web_input.get()]['password']}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {web_input.get()} exist.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
               'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
               'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for word in range(nr_letters)]
    password_symbol = [random.choice(symbols) for w in range(nr_symbols)]
    password_number = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letter + password_symbol + password_number
    random.shuffle(password_list)

    password_gen = "".join(password_list)
    password_input.insert(0, password_gen)
    pyperclip.copy(password_gen)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = web_input.get()
    email = username_input.get()
    password = password_input.get()
    new_data = {website: {"email": email, "password": password}}
    if website == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", "w")as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            web_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)
website = Label(text="Website:")
website.grid(column=0, row=1)
web_input = Entry(width=34)
web_input.focus()
web_input.grid(column=1, row=1)
search_button = Button(text="Search", width=14, command=find)
search_button.grid(column=2, row=1)
username = Label(text="Email/Username:")
username.grid(column=0, row=2)
username_input = Entry(width=53)
username_input.insert(0, "mohdwaqipervez@gmail.com")
username_input.grid(column=1, row=2, columnspan=2)
password = Label(text="Password:")
password.grid(column=0, row=3)
password_input = Entry(width=34)
password_input.grid(column=1, row=3)
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=45, command=save)
add_button.grid(column=1, row=4, columnspan=2)
window.mainloop()
