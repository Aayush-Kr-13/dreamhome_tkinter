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
    tk.messagebox.showinfo("Success", "Data submitted successfully")
    staffno=""

def open_code_1():
    root.destroy()
    os.system("python admininterface.py")
   
root = tk.Tk()
root.title("Staff Registration")

root.geometry("330x500")
frame = tk.Frame(root, width=330, height=500, bg="lightgreen")
frame.pack(fill=tk.BOTH, expand=True)

button1 = tk.Button(frame, text="Home",fg="red", command=open_code_1)
button1.grid(row=0,column=1,columnspan=2,pady=10)

fname_label = tk.Label(frame, text="First Name:")
fname_label.grid(row=1, column=1, padx=20, pady=15)
fname_entry = tk.Entry(frame)
fname_entry.grid(row=1, column=2)

lname_label = tk.Label(frame, text="Last Name:")
lname_label.grid(row=2, column=1, padx=20, pady=15)
lname_entry = tk.Entry(frame)
lname_entry.grid(row=2, column=2)

gender_label = tk.Label(frame, text="Gender:")
gender_label.grid(row=3, column=1, padx=20, pady=15)
gender_entry = tk.Entry(frame)
gender_entry.grid(row=3, column=2)

dob_label = tk.Label(frame, text="DOB:")
dob_label.grid(row=4, column=1, padx=20, pady=15)
dob_entry = tk.Entry(frame)
dob_entry.grid(row=4, column=2)

position_label = tk.Label(frame, text="Position:")
position_label.grid(row=5, column=1, padx=20, pady=15)
position_entry=tk.Entry(frame)
position_entry.grid(row=5, column = 2)

supervisor_label = tk.Label(frame, text="Supervisor:")
supervisor_label.grid(row=6, column=1, padx=20, pady=15)
supervisor_entry = tk.Entry(frame)
supervisor_entry.grid(row=6 , column=2)

branch_label = tk.Label(frame, text="Branch_id:")
branch_label.grid(row=7, column=1, padx=20, pady=15)
branch_entry = tk.Entry(frame)
branch_entry.grid(row=7 , column=2)

salary_label = tk.Label(frame, text="Salary:")
salary_label.grid(row=8, column=1, padx=20, pady=15)
salary_entry = tk.Entry(frame)
salary_entry.grid(row=8 , column=2)

submit_button = tk.Button(frame, text="Submit",fg="brown", command=submit_data)
submit_button.grid(row=9, column=1, columnspan=2,padx=20, pady=10)

root.mainloop()


