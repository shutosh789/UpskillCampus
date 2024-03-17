import tkinter as tk
from tkinter import messagebox

def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    
    if not website or not username or not password:
        messagebox.showerror("Error", "Please fill in all fields.")
        return


    with open("passwords.txt", "a") as file:
        file.write(f"Website: {website}\n")
        file.write(f"Username: {username}\n")
        file.write(f"Password: {password}\n\n")

    website_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)


def retrieve_passwords():
    passwords = ""
    try:
        with open("passwords.txt", "r") as file:
            passwords = file.read()
    except FileNotFoundError:
        passwords = "Password file not found."

    messagebox.showinfo("Stored Passwords", passwords)

root = tk.Tk()
root.title("Password Manager")
root.geometry("400x300")  


website_label = tk.Label(root, text="Website:")
website_label.pack()
website_entry = tk.Entry(root)
website_entry.pack()

username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()


save_button = tk.Button(root, text="Save Password", command=save_password)
save_button.pack()

retrieve_button = tk.Button(root, text="Retrieve Passwords", command=retrieve_passwords)
retrieve_button.pack()

root.mainloop()
