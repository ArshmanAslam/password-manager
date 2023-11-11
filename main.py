from tkinter import *
from tkinter import messagebox
from random import shuffle, randint, choice
import pyperclip


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter = [choice(letters) for _ in range(randint(6, 8))]
    symbol = [choice(symbols) for _ in range(randint(2, 4))]
    number = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = letter + symbol + number
    shuffle(password_list)

    final_password = "".join(password_list)
    password.insert(0, final_password)
    pyperclip.copy(final_password)


def save_file():
    email_txt = email.get()
    website_txt = website.get()
    password_txt = password.get()
    if website_txt == '' and password_txt == '' and email_txt == '':
        messagebox.showinfo(title='Empty Fields', message='PLEASE FILL THE FIELDS')

    else:
        if messagebox.askyesnocancel(title='User Confirmation', message=f'Your Password For Website: {website_txt} \n'
                                                                        f'Password: {password_txt}\n'
                                                                        f'Email / UserName: {email_txt}'):
            file = open('Data.txt', 'a')
            file.write(f'\n{website_txt} | {email_txt} | {password_txt}')
            email.delete(0, END)
            website.delete(0, END)
            password.delete(0, END)


screen = Tk()
screen.config(padx=50, pady=50, bg="#98F5FF")
screen.title("Password Manager Gui")
# canvas+image Part
canvas = Canvas(width=200, height=200, bg="#98F5FF", highlightthickness=0)
image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)
# canvas end

# texts
text1 = Label(text='Website:', width=10, height=2, bg="#98F5FF")
text1.grid(row=1, column=1)

text2 = Label(text='Email/Username:', width=15, height=2, bg="#98F5FF")
text2.grid(row=2, column=1)

text3 = Label(text='Password:', width=10, height=2, bg="#98F5FF")
text3.grid(row=3, column=1)
# text label ending

# text field

website = Entry(width=35)
website.grid(row=1, column=1, columnspan=3)
website.focus()

email = Entry(width=35)
email.grid(row=2, column=1, columnspan=3)

password = Entry(width=35)
password.grid(row=3, column=1, columnspan=3)

# button
b = Button(text='Add', width=36, command=save_file)
b.grid(row=4, column=2)

generate = Button(text='Generate Password', width=15, command=password_generator)
generate.grid(row=3, column=3)

screen.mainloop()
