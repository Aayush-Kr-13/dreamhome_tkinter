import tkinter as tk
import mysql.connector
import os

def open_code_1():
    root.destroy()
    os.system("python dreamhome_tkinter\main.py")

def check_credentials():
    admin_id = admin_id_box.get()
    password = password_box.get()
    
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Aayush@2301',
        database='Dreamhouse'
    )
    
    cursor = db.cursor()

    cursor.execute("SELECT * FROM admin WHERE admin_id = %s AND password = %s", (admin_id, password))
    
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

admin_id_label = tk.Label(frame, text="Enter Admin Id :")
admin_id_label.grid(row=0, column=0, padx=10, pady=10)
admin_id_box = tk.Entry(frame)
admin_id_box.grid(row=0, column=1, padx=10, pady=10)
password_label = tk.Label(frame, text="Enter Password :")
password_label.grid(row=1, column=0, padx=10, pady=10)
password_box = tk.Entry(frame)
password_box.grid(row=1, column=1, padx=10, pady=10)

button = tk.Button(frame, text="Login", command=check_credentials)
button.grid(row=3, column=0, columnspan=3)

message = tk.Label(frame, text="")


root.mainloop()
