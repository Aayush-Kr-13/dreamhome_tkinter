import tkinter as tk
import mysql.connector
import os

def open_code_1():
    root.destroy()
    os.system("python main.py")

def check_credentials():
    clientno = id_box.get()
    email = email_box.get()
    
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='12345',
        database='proj'
    )
    
    cursor = db.cursor()

    cursor.execute("SELECT * FROM clients WHERE clientno = %s AND email = %s", (clientno, email))
    
    row = cursor.fetchone()
    
    if row:
        message.config(text="Login Successful", fg="green")
        open_code_1()
        root.destroy()
    else:
        message.config(text="Invalid User ID or Email", fg="red")


root = tk.Tk()
root.geometry("350x500")
frame = tk.Frame(root, width=350, height=500, bg="lightgreen")
frame.pack(fill=tk.BOTH, expand=True)

id_label = tk.Label(frame, text="Enter Client Id :")
id_label.grid(row=0, column=0, padx=10, pady=10)
id_box = tk.Entry(frame)
id_box.grid(row=0, column=1, padx=10, pady=10)
email_label = tk.Label(frame, text="Enter Email :")
email_label.grid(row=1, column=0, padx=10, pady=10)
email_box = tk.Entry(frame)
email_box.grid(row=1, column=1, padx=10, pady=10)

button = tk.Button(frame, text="Login", command=check_credentials)
button.grid(row=3, column=0, columnspan=3)

message = tk.Label(frame, text="")


root.mainloop()
