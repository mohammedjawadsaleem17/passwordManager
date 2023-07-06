 #bismillah
from tkinter import *
from tkinter import messagebox
from random import *
# import pyperclip
import json


#Implementing the search feature and migrating from saving data in txt to json format



# -------------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6' , '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_symbols = [choice(symbols) for _ in range(randint(2,4))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]


    #Combine 3 Lists into One List

    password_list = password_letters+password_numbers+password_symbols
    shuffle(password_list)

    password="".join(password_list)
    print(password)
    password_entry.insert(0,password)
    # pyperclip.copy(password)

    #putting string to clipboard

# ---------------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_entry.get()#Here the fields are retrived
    email=email_entry.get()
    password=password_entry.get()




    new_data = {
        website:{
            "email":email,
            "password":password,
        }
    }







    #To display a message to check are they actually happy with what they have written
    if len(website) == 0 or len(password)==0 or len(email)==0:
        messagebox.showinfo(title="Oh!",message="Please make sure you haven't left any feilds empty")
    else:
        # is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\nis it okay to save?")
    #The message box is going to return a boolean True / False
        # if there is no file , the append keyword will create a new file
        try:
            with open("data.json","r") as data_file:
                data=json.load(data_file)

        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
            data.update(new_data)

            with open("data.json","w") as data_file:
                json.dump(data,data_file,indent=4)



                # data_file.write(f"{website} | {email} | {password}\n")
                # After succees we need to delete the present entries
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)

# -------------------------------------------------------- Implementing Search SETUP ----------------------------------------------------- #
def find_password():
    website=website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No data found")
    else:
        if website in data:
            print("Success")
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error",message=f"No Details found for {website}")

# -------------------------------------------------------- UI SETUP ----------------------------------------------------- #
windows=Tk()
windows.title("SecurePass")
windows.config(padx=50,pady=77)

canvas = Canvas(width=200,height=200)
passwordImage = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=passwordImage)
canvas.grid(row=0,column=1)

#Creating Website
website_label = Label(text="Website:", font=("Arial", 11))
website_label.grid(row=1, column=0)
email = Label(text="Email/Username:",font=("Arial",11))
email.grid(row=2,column=0)
password_label = Label(text="Password:", font=("Arial", 11))
password_label.grid(row=3, column=0)



#Creating Entry Space

website_entry = Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2,pady=7)

searchButton = Button(text="Search",width=15,height=1,command=find_password)
searchButton.grid(row=1,column=3,columnspan=1)


website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2,pady=7)
email_entry.insert(0,"mohammedjawad@gmail.com")
password_entry= Entry(width=35)
password_entry.grid(row=3,column=1,columnspan=2,pady=7)
#Adding the password entry adding a commit here



passwordButton = Button(text="Generate Password",width=15,height=1,command=generate_password)
passwordButton.grid(row=3,column=3,columnspan=1)

addButton = Button(text="Add",width=30,command=save)
addButton.grid(row=4,column=1,columnspan=2)

windows.mainloop()





