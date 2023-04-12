import tkinter as tk
import mysql.connector
import string
import os

def submit_data():
    branch_id = branchid_entry.get()
    branch_name = branchname_entry.get()
    branch_hno = branch_hno_entry.get()
    branch_street = branch_street_entry.get()
    branch_city=branch_city_entry.get()
    branch_postal_code=branch_postal_code_entry.get()
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Aayush@2301',
        database='Dreamhouse'
    )
    cursor = db.cursor()
    sql = "INSERT INTO branches (branch_id, branch_name, branch_hno, branch_street, branch_city, branch_postal_code) VALUES (%s, %s, %s, %s,%s,%s)"
    values = (branch_id, branch_name, branch_hno, branch_street, branch_city, branch_postal_code)
    cursor.execute(sql, values)
    db.commit()
    db.close()
    branchid_entry.delete(0, tk.END)
    branchname_entry.delete(0, tk.END)
    branch_hno_entry.delete(0, tk.END)
    branch_street_entry .delete(0, tk.END)
    branch_city_entry.delete(0, tk.END)
    branch_postal_code_entry.delete(0, tk.END)
    root.destroy()
    open_code_2()
    tk.messagebox.showinfo("Success", "Data submitted successfully")

def open_code_1():
    root.destroy()
    os.system("python admininterface.py")
    
def open_code_2():
    root.destroy()
    os.system("python addbranch.py")

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

branchid_label = tk.Label(frame, text="branchid:",bg="#2C3E50",fg="white",font=large_font1)
branchid_label.place(x=70,y=90)
branchid_entry = tk.Entry(frame)
branchid_entry.place(x=160,y=90)

branchname_label = tk.Label(frame, text="Branch Name:",bg="#2C3E50",fg="white",font=large_font1)
branchname_label.place(x=50,y=150)
branchname_entry = tk.Entry(frame)
branchname_entry.place(x=160,y=150)

branch_hno_label = tk.Label(frame, text="Branch Hno:",bg="#2C3E50",fg="white",font=large_font1)
branch_hno_label.place(x=60,y=210)
branch_hno_entry = tk.Entry(frame)
branch_hno_entry.place(x=160,y=210)

branch_street_label = tk.Label(frame, text="Branch street:",bg="#2C3E50",fg="white",font=large_font1)
branch_street_label.place(x=50,y=270)
branch_street_entry = tk.Entry(frame)
branch_street_entry.place(x=160,y=270)

branch_city_label = tk.Label(frame, text="Enter City :",bg="#2C3E50",fg="white",font=large_font1)
branch_city_label.place(x=60,y=330)
branch_city_entry = tk.Entry(frame)
branch_city_entry.place(x=160,y=330)

branch_postal_code_label = tk.Label(frame, text="Enter postal Code:",bg="#2C3E50",fg="white",font=large_font1)
branch_postal_code_label.place(x=20,y=390)
branch_postal_code_entry = tk.Entry(frame)
branch_postal_code_entry.place(x=160,y=390)


submit_button = tk.Button(frame, text="Submit",bg="#1ABC9C", command=submit_data)
submit_button.place(x=140, y=450)

root.mainloop()


