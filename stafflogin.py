import tkinter as tk
import mysql.connector
import os

def open_code_1():
    root.destroy()
    os.system("python loginpage.py")

def check_credentials():
    staffno = id_box.get()
    lname = lname_box.get()
    
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Aayush@2301',
        database='Dreamhouse'
    )
    
    cursor = db.cursor()

    cursor.execute("SELECT * FROM staffs WHERE staffno = %s AND lname = %s", (staffno, lname))
    
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

id_label = tk.Label(frame, text="Enter Staff No :")
id_label.grid(row=0, column=0, padx=10, pady=10)
id_box = tk.Entry(frame)
id_box.grid(row=0, column=1, padx=10, pady=10)
lname_label = tk.Label(frame, text="Enter Last Name :")
lname_label.grid(row=1, column=0, padx=10, pady=10)
lname_box = tk.Entry(frame)
lname_box.grid(row=1, column=1, padx=10, pady=10)

button = tk.Button(frame, text="Login", command=check_credentials)
button.grid(row=3, column=0, columnspan=3)

message = tk.Label(frame, text="")


root.mainloop()
