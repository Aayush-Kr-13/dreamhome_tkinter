import tkinter as tk
import string
import os
import random
from tempCodeRunnerFile import db

def generate_random_string(length):
    all_chars = list(string.digits + string.ascii_letters.upper())
    random.shuffle(all_chars)
    random_chars = random.sample(all_chars, length)
    return ''.join(random_chars)

def submit_data():
    branch_id = generate_random_string(6)
    branch_name = branchname_entry.get()
    branch_hno = branch_hno_entry.get()
    branch_street = branch_street_entry.get()
    branch_city=branch_city_entry.get()
    branch_postal_code=branch_postal_code_entry.get()
    cursor = db.cursor()
    sql = "INSERT INTO branches (branch_id, branch_name, branch_hno, branch_street, branch_city, branch_postal_code) VALUES (%s, %s, %s, %s,%s,%s)"
    values = (branch_id, branch_name, branch_hno, branch_street, branch_city, branch_postal_code)
    cursor.execute(sql, values)
    db.commit()
    db.close()
    branchname_entry.delete(0, tk.END)
    branch_hno_entry.delete(0, tk.END)
    branch_street_entry .delete(0, tk.END)
    branch_city_entry.delete(0, tk.END)
    branch_postal_code_entry.delete(0, tk.END)
    root.destroy()
    open_code_2()

def open_code_1():
    root.destroy()
    os.system("python dreamhome_tkinter\\admininterface.py")
    
def open_code_2():
    root.destroy()
    os.system("python dreamhome_tkinter\\addBranch.py")

root = tk.Tk()
root.geometry("350x500")
frame = tk.Frame(root, width=350, height=500, bg="#2C3E50")
frame.pack(fill=tk.BOTH, expand=True)

large_font = ('Verdana', 20)
large_font1 = ('Verdana', 10)

root.title("Property Registration")

button1 = tk.Button(frame, text="Back",fg="red", command=open_code_1)
button1.place(x=10,y=10)

_label = tk.Label(frame, text="Add Branch",bg="#2C3E50",fg="Orange",font=large_font)
_label.place(x=100,y=35)

branchname_label = tk.Label(frame, text="Branch Name:",bg="#2C3E50",fg="white",font=large_font1)
branchname_label.place(x=30,y=120)
branchname_entry = tk.Entry(frame)
branchname_entry.place(x=160,y=120)

branch_hno_label = tk.Label(frame, text="Branch Hno:",bg="#2C3E50",fg="white",font=large_font1)
branch_hno_label.place(x=30,y=180)
branch_hno_entry = tk.Entry(frame)
branch_hno_entry.place(x=160,y=180)

branch_street_label = tk.Label(frame, text="Branch street:",bg="#2C3E50",fg="white",font=large_font1)
branch_street_label.place(x=30,y=240)
branch_street_entry = tk.Entry(frame)
branch_street_entry.place(x=160,y=240)

branch_city_label = tk.Label(frame, text="Enter City :",bg="#2C3E50",fg="white",font=large_font1)
branch_city_label.place(x=30,y=300)
branch_city_entry = tk.Entry(frame)
branch_city_entry.place(x=160,y=300)

branch_postal_code_label = tk.Label(frame, text="Enter postal Code:",bg="#2C3E50",fg="white",font=large_font1)
branch_postal_code_label.place(x=20,y=360)
branch_postal_code_entry = tk.Entry(frame)
branch_postal_code_entry.place(x=160,y=360)


submit_button = tk.Button(frame, text="Submit",bg="#1ABC9C", command=submit_data)
submit_button.place(x=140, y=450)

root.mainloop()


