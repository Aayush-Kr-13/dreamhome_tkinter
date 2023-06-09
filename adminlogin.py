import tkinter as tk
import mysql.connector
import os
from tempCodeRunnerFile import db

def open_code_1():
    root.destroy()
    os.system("python dreamhome_tkinter\\admininterface.py")
    
def open_code_2():
    root.destroy()
    os.system("python dreamhome_tkinter\\loginpage.py")


def check_credentials():
    admin_id = admin_id_box.get()
    password = password_box.get()
    
    cursor = db.cursor()

    cursor.execute("SELECT * FROM admin WHERE admin_id = %s AND password = %s", (admin_id, password))
    
    row = cursor.fetchone()
    
    if row:
        success_label = tk.Label(root, text="Login successful!",bg="lightgreen")
        success_label.place(x=150, y=150)
        open_code_1()
        root.destroy()
    else:
        error_label = tk.Label(root, text="Invalid username or password.",bg="red")
        error_label.place(x=150, y=150)


root = tk.Tk()
root.title("Admin Login")
root.geometry("400x250")
frame = tk.Frame(root, width=350, height=500, bg="#2C3E50")
frame.pack(fill=tk.BOTH, expand=True)

large_font = ('Verdana', 15)
large_font1 = ('Verdana', 10)

button1 = tk.Button(frame, text="Back",fg="red", command=open_code_2)
button1.place(x=10,y=10)

admin_label = tk.Label(frame, text="Admin Login",bg="#2C3E50",fg="Orange",font=large_font)
admin_label.place(x=125,y=15)

admin_id_label = tk.Label(frame, text="Enter Admin Id :",bg="#2C3E50",fg="white",font=large_font1)
admin_id_label.place(x=50, y=80)
admin_id_box = tk.Entry(frame)
admin_id_box.place(x=180, y=80)
password_label = tk.Label(frame, text="Enter Password :",bg="#2C3E50",fg="white",font=large_font1)
password_label.place(x=50, y=120)
password_box = tk.Entry(frame)
password_box.place(x=180, y=120)

button = tk.Button(frame, text="Login", command=check_credentials,bg="#1ABC9C")
button.place(x=180, y=180)

message = tk.Label(frame, text="")


root.mainloop()
