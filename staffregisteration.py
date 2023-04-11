import tkinter as tk
import mysql.connector
import random
import string

def generate_random_string(length):
    all_chars = list(string.digits + string.ascii_letters.upper())
    random.shuffle(all_chars)
    random_chars = random.sample(all_chars, length)
    return ''.join(random_chars)

def submit_data():
    fname = fname_entry.get()
    lname = lname_entry.get()
    gender = gender_entry.get()
    dob = dob_entry.get()
    position = position_entry.get()
    supervisor = supervisor_entry.get()
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Aayush@2301',
        database='Dreamhouse'
    )
    staffno = generate_random_string(10)
    cursor = db.cursor()
    sql = "INSERT INTO staffs (staffno ,fname, lname, gender, dob, position, supervisor ) VALUES (%s, %s, %s, %s,%s,%s,%s)"
    values = (staffno ,fname, lname, gender, dob, position, supervisor )
    cursor.execute(sql, values)
    db.commit()
    db.close()
    fname_entry.delete(0, tk.END)
    lname_entry.delete(0, tk.END)
    gender_entry.delete(0, tk.END)
    dob_entry.delete(0, tk.END)
    position_entry.delete(0, tk.END)
    supervisor_entry.delete(0, tk.END)
    tk.messagebox.showinfo("Success", "Data submitted successfully")
    staffno=""
    
root = tk.Tk()
root.title("Staff Registration")

fname_label = tk.Label(root, text="First Name:")
fname_label.grid(row=0, column=0)
fname_entry = tk.Entry(root)
fname_entry.grid(row=0, column=1)

lname_label = tk.Label(root, text="Last Name:")
lname_label.grid(row=1, column=0)
lname_entry = tk.Entry(root)
lname_entry.grid(row=1, column=1)

gender_label = tk.Label(root, text="Gender:")
gender_label.grid(row=2, column=0)
gender_entry = tk.Entry(root)
gender_entry.grid(row=2, column=1)

dob_label = tk.Label(root, text="DOB:")
dob_label.grid(row=3, column=0)
dob_entry = tk.Entry(root)
dob_entry.grid(row=3, column=1)

position_label = tk.Label(root, text="Position:")
position_label.grid(row=4, column=0)
position_entry=tk.Entry(root)
position_entry.grid(row=4, column = 1)

supervisor_label = tk.Label(root, text="Supervisor:")
supervisor_label.grid(row=5 , column =0)
supervisor_entry = tk.Entry(root)
supervisor_entry.grid(row=5 , column=1)

submit_button = tk.Button(root, text="Submit", command=submit_data)
submit_button.grid(row=6, column=0, columnspan=2)

root.mainloop()


