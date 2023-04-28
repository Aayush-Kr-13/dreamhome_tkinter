import tkinter as tk
import mysql.connector
from tkinter import ttk
import os
from tempCodeRunnerFile import db

def open_code_1():
    root.destroy()
    os.system("python dreamhome_tkinter\\admininterface.py")

def display_table():
    city_id = city_id_entry.get()
    branch_id = branch_id_entry.get()
    tree.delete(*tree.get_children())
    cursor = db.cursor()
    cursor.execute("SELECT * FROM branches WHERE branch_city = %s and branch_id = %s", (city_id,branch_id))
    data = cursor.fetchall()
    for row in data:
        tree.insert("", "end", values=row)
    city_id_entry.delete(0, 'end')
    branch_id_entry.delete(0, "end")
    
def display_table1():
    tree.delete(*tree.get_children())
    cursor = db.cursor()
    cursor.execute("SELECT * FROM branches")
    data = cursor.fetchall()
    for row in data:
        tree.insert("", "end", values=row)
    city_id_entry.delete(0, 'end')
    branch_id_entry.delete(0, "end")

def search_database():
    city_id = city_id_entry.get()
    branch_id = branch_id_entry.get()
    mycursor = db.cursor()
    sql = "SELECT * FROM branches WHERE branch_city = %s and branch_id = %s"
    mycursor.execute(sql, (city_id,branch_id))
    data = mycursor.fetchall()
    if len(data) > 0:
        success_label = tk.Label(root, text="Branch Found!",bg="lightgreen")
        success_label.place(x=110, y=215)
        display_table()
    else:
        error_label = tk.Label(root, text="No Branch In This City",bg="Red")
        error_label.place(x=110, y=215)
        city_id_entry.delete(0, 'end')
        city_id_entry.delete(0, 'end')
        branch_id_entry.delete(0, "end")

root = tk.Tk()
root.title("Branch List")
root.geometry("1400x600")
frame = tk.Frame(root, width=1400, height=600, bg="#2C3E50")
frame.pack(fill=tk.BOTH, expand=True)

large_font = ('Verdana', 15)
large_font1 = ('Verdana', 10)

button1 = tk.Button(frame, text="Back",fg="red", command=open_code_1)
button1.place(x=5,y=3)

user_label = tk.Label(frame, text="Branch List",bg="#2C3E50",fg="Orange",font=large_font)
user_label.pack()

city_id_label = tk.Label(root, text="Enter City :",bg="#2C3E50",fg="white",font=large_font1)
city_id_label.place(x=20,y=100)
city_id_entry = tk.Entry(root)
city_id_entry.place(x=120,y=100)

branch_id_label = tk.Label(root, text="Branch Id:",bg="#2C3E50",fg="white",font=large_font1)
branch_id_label.place(x=20,y=180)
branch_id_entry = tk.Entry(root)
branch_id_entry.place(x=120,y=180)

search_button = tk.Button(root, text="Search", command=search_database,bg="#1ABC9C")
search_button.place(x=110,y=250)


tree = ttk.Treeview(frame)
tree.pack(fill="both", expand=True)

tree["columns"] = ("one", "two", "three", "four", "five", "six")

tree.heading("one", text="Branch ID")
tree.heading("two", text="Branch Name")
tree.heading("three", text="Branch Hno")
tree.heading("four", text="Branch Street")
tree.heading("five", text="City")
tree.heading("six", text="Postal Code")

tree.column("one", width=100)
tree.column("two", width=100)
tree.column("three", width=100)
tree.column("four", width=100)
tree.column("five", width=100)
tree.column("six", width=100)


display_button = tk.Button(frame, text="Display All Branches", command=display_table1,bg="#1ABC9C")
display_button.pack()

root.mainloop()