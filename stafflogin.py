import tkinter as tk
from tempCodeRunnerFile import db
import os

def open_code_1():
    root.destroy()
    os.system("python dreamhome_tkinter\\staffinterface.py")
    
def open_code_2():
    root.destroy()
    os.system("python dreamhome_tkinter\\loginpage.py")

def check_credentials():
    staffno = id_box.get()
    lname = lname_box.get()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM staffs WHERE staffno = %s AND lname = %s", (staffno, lname))
    
    row = cursor.fetchone()
    
    if row:
        success_label = tk.Label(root, text="Login successful!")
        success_label.place(x=150, y=150)
        open_code_1()
        root.destroy()
    else:
        error_label = tk.Label(root, text="Invalid username or password.",bg="red")
        error_label.place(x=150, y=150)


root = tk.Tk()
root.title("Staff Login")
root.geometry("400x250")
frame = tk.Frame(root, width=350, height=500, bg="#2C3E50")
frame.pack(fill=tk.BOTH, expand=True)

large_font = ('Verdana', 15)
large_font1 = ('Verdana', 10)

button1 = tk.Button(frame, text="Back",fg="red", command=open_code_2)
button1.place(x=10,y=10)

staff_label = tk.Label(frame, text="Staff Login",bg="#2C3E50",fg="Orange",font=large_font)
staff_label.place(x=125,y=15)

id_label = tk.Label(frame, text="Enter Staff No :",bg="#2C3E50",fg="white",font=large_font1)
id_label.place(x=50, y=80)
id_box = tk.Entry(frame)
id_box.place(x=200, y=80)
lname_label = tk.Label(frame, text="Enter Last Name :",bg="#2C3E50",fg="white",font=large_font1)
lname_label.place(x=50, y=120)
lname_box = tk.Entry(frame)
lname_box.place(x=200, y=120)

button = tk.Button(frame, text="Login", command=check_credentials,bg="#1ABC9C")
button.place(x=180, y=180)

message = tk.Label(frame, text="")


root.mainloop()
