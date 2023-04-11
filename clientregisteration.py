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
        password='Aayush@2301',
        database='Dreamhouse'
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
 
root = tk.Tk()
root.geometry("300x300")
frame = tk.Frame(root, width=500, height=500, bg="lightgreen")
frame.pack(fill=tk.BOTH, expand=True)

root.title("Client Registration")

fname_label = tk.Label(frame, text="First Name:")
fname_label.grid(row=0, column=1, padx=10, pady=10)
fname_entry = tk.Entry(frame)
fname_entry.grid(row=0, column=2)

lname_label = tk.Label(frame, text="Last Name:")
lname_label.grid(row=1, column=1, padx=10, pady=10)
lname_entry = tk.Entry(frame)
lname_entry.grid(row=1, column=2)

telno_label = tk.Label(frame, text="Telephone Number:")
telno_label.grid(row=2, column=1, padx=10, pady=10)
telno_entry = tk.Entry(frame)
telno_entry.grid(row=2, column=2)

email_label = tk.Label(frame, text="Email Address:")
email_label.grid(row=3, column=1, padx=10, pady=10)
email_entry = tk.Entry(frame)
email_entry.grid(row=3, column=2)

null_label = tk.Label(frame, text="")
null_label.grid(row=5, column=0)

submit_button = tk.Button(frame, text="Submit", command=submit_data)
submit_button.grid(row=6, column=1, columnspan=2)

root.mainloop()


