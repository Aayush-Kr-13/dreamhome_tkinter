import tkinter as tk
import mysql.connector
import random
import string
import os

def generate_random_string(length):
    all_chars = list(string.digits + string.ascii_letters.upper())
    random.shuffle(all_chars)
    random_chars = random.sample(all_chars, length)
    return ''.join(random_chars)

def submit_data():
    fname = fname_entry.get()
    lname = lname_entry.get()
    telno = telno_entry.get()
    email = email_entry.get()
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='12345',
        database='proj'
    )
    clientno = generate_random_string(10)
    cursor = db.cursor()
    sql = "INSERT INTO clients (clientno ,fname, lname, telno, email) VALUES (%s, %s, %s, %s,%s)"
    values = (clientno, fname, lname, telno, email)
    cursor.execute(sql, values)
    db.commit()
    db.close()
    fname_entry.delete(0, tk.END)
    lname_entry.delete(0, tk.END)
    telno_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    tk.messagebox.showinfo("Success", "Data submitted successfully")
    clientno=""
 
def open_code_1():
    root.destroy()
    os.system("python loginpage.py")

root = tk.Tk()
root.title("User Registeration")
root.geometry("400x380")
frame = tk.Frame(root, width=500, height=500, bg="#2C3E50")
frame.pack(fill=tk.BOTH, expand=True)

large_font = ('Verdana', 18)
large_font1 = ('Verdana', 10)

user_label = tk.Label(frame, text="User Registration",bg="#2C3E50",fg="Orange",font=large_font)
user_label.place(x=100,y=22)

button1 = tk.Button(frame, text="Back",fg="red", command=open_code_1)
button1.place(x=10,y=10)

fname_label = tk.Label(frame, text="First Name:",bg="silver",font=large_font1)
fname_label.place(x=60, y=80)
fname_entry = tk.Entry(frame)
fname_entry.place(x=200, y=80)

lname_label = tk.Label(frame, text="Last Name:",bg="silver",font=large_font1)
lname_label.place(x=60, y=150)
lname_entry = tk.Entry(frame)
lname_entry.place(x=200, y=150)

telno_label = tk.Label(frame, text="Telephone Number:",bg="silver",font=large_font1)
telno_label.place(x=30, y=220)
telno_entry = tk.Entry(frame)
telno_entry.place(x=200, y=220)

email_label = tk.Label(frame, text="Email Address:",bg="silver",font=large_font1)
email_label.place(x=60, y=290)
email_entry = tk.Entry(frame)
email_entry.place(x=200, y=290)


submit_button = tk.Button(frame, text="Submit",bg="#1ABC9C", command=submit_data)
submit_button.place(x=150,y=335)


root.mainloop()


