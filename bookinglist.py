import tkinter as tk
import mysql.connector
from tkinter import ttk
import os

def open_code_1():
    root.destroy()
    os.system("python dreamhome_tkinter\\admininterface.py")

db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='12345',
        database='proj'
)

def display_table1():
    tree.delete(*tree.get_children())
    mycursor = db.cursor()
    sql = "SELECT * FROM lease"
    mycursor.execute(sql, ())
    data = mycursor.fetchall()
    for row in data:
        tree.insert("", "end", values=row)

def display_table():
    city_id = city_id_entry.get()
    property_id = property_id_entry.get()
    tree.delete(*tree.get_children())
    mycursor = db.cursor()
    sql = "SELECT * FROM lease WHERE city = %s and property_no = %s"
    mycursor.execute(sql, (city_id,property_id))
    data = mycursor.fetchall()
    for row in data:
        tree.insert("", "end", values=row)
    city_id_entry.delete(0, 'end')
    property_id_entry.delete(0, "end")

def search_database():
    city_id = city_id_entry.get()
    property_id = property_id_entry.get()
    mycursor = db.cursor()
    sql = "SELECT * FROM lease WHERE city = %s and property_no = %s"
    mycursor.execute(sql, (city_id,property_id))
    data = mycursor.fetchall()
    if len(data) > 0:
        success_label = tk.Label(root, text="Booking Found!",bg="lightgreen")
        success_label.place(x=110, y=215)
        display_table()
    else:
        error_label = tk.Label(root, text="Booking Not Found",bg="Red")
        error_label.place(x=110, y=215)
        city_id_entry.delete(0, 'end')
        property_id_entry.delete(0, "end")

root = tk.Tk()
root.title("Booking List")
root.geometry("1550x600")
frame = tk.Frame(root, width=1550, height=600, bg="#2C3E50")
frame.pack(fill=tk.BOTH, expand=True)

large_font = ('Verdana', 15)
large_font1 = ('Verdana', 10)

button1 = tk.Button(frame, text="Back",fg="red", command=open_code_1)
button1.place(x=5,y=3)

user_label = tk.Label(frame, text="Bookings",bg="#2C3E50",fg="Orange",font=large_font)
user_label.pack()

city_id_label = tk.Label(root, text="Enter City :",bg="#2C3E50",fg="white",font=large_font1)
city_id_label.place(x=5,y=100)
city_id_entry = tk.Entry(root)
city_id_entry.place(x=100,y=100)

property_id_label = tk.Label(root, text="Property No:",bg="#2C3E50",fg="white",font=large_font1)
property_id_label.place(x=5,y=180)
property_id_entry = tk.Entry(root)
property_id_entry.place(x=100,y=180)

search_button = tk.Button(root, text="Search", command=search_database,bg="#1ABC9C")
search_button.place(x=80,y=250)

tree = ttk.Treeview(frame)
tree.pack(fill="both", expand=True)

tree["columns"] = ("one", "two", "three", "four", "five")

tree.heading("one", text="Lease Id")
tree.heading("two", text="Owner Id")
tree.heading("three", text="Client Id")
tree.heading("four", text="Property No")
tree.heading("five", text="City")

tree.column("one", width=100)
tree.column("two", width=100)
tree.column("three", width=100)
tree.column("four", width=100)
tree.column("five", width=100)

display_button = tk.Button(frame, text="Display All Bookings", command=display_table1,bg="#1ABC9C")
display_button.pack()

root.mainloop()
