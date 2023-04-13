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
    gender = gender_entry.get()
    branch=branch_entry.get()
    salary=salary_entry.get()
    dob = dob_entry.get()
    position = position_entry.get()
    supervisor = supervisor_entry.get()
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='12345',
        database='proj'
    )
    staffno = generate_random_string(10)
    cursor = db.cursor()
    sql = "INSERT INTO staffs (staffno ,fname, lname, gender, dob, position, supervisor,branch_id,salary ) VALUES (%s, %s, %s, %s,%s,%s,%s,%s,%s)"
    values = (staffno ,fname, lname, gender, dob, position, supervisor,branch,salary )
    cursor.execute(sql, values)
    db.commit()
    db.close()
    fname_entry.delete(0, tk.END)
    lname_entry.delete(0, tk.END)
    gender_entry.delete(0, tk.END)
    dob_entry.delete(0, tk.END)
    position_entry.delete(0, tk.END)
    supervisor_entry.delete(0, tk.END)
    branch_entry.delete(0, tk.END)
    salary_entry.delete(0, tk.END)
    success_label = tk.Label(root, text="Registrartion Successful!",bg="lightgreen")
    success_label.place(x=150, y=500)
    clientid_label = tk.Label(root, text="Your Staff Id is :" +staffno)
    clientid_label.place(x=150, y=530)
    staffno=""

def open_code_1():
    root.destroy()
    os.system("python dreamhome_tkinter\\admininterface.py")
   
root = tk.Tk()
root.title("Staff Registration")

root.geometry("400x600")
frame = tk.Frame(root, width=400, height=600, bg="#2C3E50")
frame.pack(fill=tk.BOTH, expand=True)

large_font = ('Verdana', 19)
large_font1 = ('Verdana', 10)

user_label = tk.Label(frame, text="Staff Registration",bg="#2C3E50",fg="Orange",font=large_font)
user_label.place(x=70,y=35)

button1 = tk.Button(frame, text="Back",fg="red", command=open_code_1)
button1.place(x=10,y=10)

fname_label = tk.Label(frame, text="First Name:")
fname_label.place(x=40,y=100)
fname_entry = tk.Entry(frame)
fname_entry.place(x=180,y=100)

lname_label = tk.Label(frame, text="Last Name:")
lname_label.place(x=40,y=150)
lname_entry = tk.Entry(frame)
lname_entry.place(x=180,y=150)

gender_label = tk.Label(frame, text="Gender:")
gender_label.place(x=40,y=200)
gender_entry = tk.Entry(frame)
gender_entry.place(x=180,y=200)

dob_label = tk.Label(frame, text="DOB:")
dob_label.place(x=40,y=250)
dob_entry = tk.Entry(frame)
dob_entry.place(x=180,y=250)

position_label = tk.Label(frame, text="Position:")
position_label.place(x=40,y=300)
position_entry=tk.Entry(frame)
position_entry.place(x=180,y=300)

supervisor_label = tk.Label(frame, text="Supervisor:")
supervisor_label.place(x=40,y=350)
supervisor_entry = tk.Entry(frame)
supervisor_entry.place(x=180,y=350)

branch_label = tk.Label(frame, text="Branch_id:")
branch_label.place(x=40,y=400)
branch_entry = tk.Entry(frame)
branch_entry.place(x=180,y=400)

salary_label = tk.Label(frame, text="Salary:")
salary_label.place(x=40,y=450)
salary_entry = tk.Entry(frame)
salary_entry.place(x=180,y=450)

submit_button = tk.Button(frame, text="Submit",bg="#1ABC9C", command=submit_data)
submit_button.place(x=150,y=560)

root.mainloop()


