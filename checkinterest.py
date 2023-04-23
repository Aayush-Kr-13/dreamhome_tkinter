import tkinter as tk
import mysql.connector
from tkinter import ttk
import os

def open_code_1():
    root.destroy()
    os.system("python userInterface.py")

def open_code_2():
    root.destroy()
    os.system("python checkinterest.py")

db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='12345',
        database='proj'
)

def display_table():
    client_id = client_id_entry.get()
    property_id = property_id_entry.get()
    tree.delete(*tree.get_children())
    cursor = db.cursor()
    cursor.execute("SELECT * FROM interests WHERE owner_no = %s and property_no=%s", (client_id,property_id))
    data = cursor.fetchall()
    for row in data:
        tree.insert("", "end", values=row)
    client_id_entry.delete(0, 'end')
    property_id_entry.delete(0, 'end')
    db.commit()
    db.close()

def search_database():
    client_id = client_id_entry.get()
    property_id = property_id_entry.get()
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM interests WHERE owner_no = %s and property_no=%s", (client_id,property_id))
    data = mycursor.fetchall()
    if len(data) > 0:
        success_label = tk.Label(root, text="Verification Successful!",bg="lightgreen")
        success_label.place(x=120, y=230)
        display_table()
    else:
        error_label = tk.Label(root, text=" No Interests",bg="Red")
        error_label.place(x=120, y=230)
        client_id_entry.delete(0, 'end')
        property_id_entry.delete(0, 'end')
        db.commit()
        db.close()

root = tk.Tk()
root.title("Property List")
root.geometry("1400x600")
frame = tk.Frame(root, width=1400, height=600, bg="#2C3E50")
frame.pack(fill=tk.BOTH, expand=True)

large_font = ('Verdana', 15)
large_font1 = ('Verdana', 10)

button1 = tk.Button(frame, text="Back",fg="red", command=open_code_1)
button1.place(x=5,y=3)

user_label = tk.Label(frame, text="Interested Person",bg="#2C3E50",fg="Orange",font=large_font)
user_label.pack()

client_id_label = tk.Label(root, text="Confirm Client ID:",bg="#2C3E50",fg="white",font=large_font1)
client_id_label.place(x=20,y=100)
client_id_entry = tk.Entry(root)
client_id_entry.place(x=180,y=100)

property_id_label = tk.Label(root, text="Confirm Property No:",bg="#2C3E50",fg="white",font=large_font1)
property_id_label.place(x=20,y=180)
property_id_entry = tk.Entry(root)
property_id_entry.place(x=180,y=180)

search_button = tk.Button(root, text="Search", command=search_database,bg="#1ABC9C")
search_button.place(x=150,y=270)

tree = ttk.Treeview(frame)
tree.pack(fill="both", expand=True)

tree["columns"] = ("one", "two", "three", "four", "five")

tree.heading("one", text="Your_id")
tree.heading("two", text="client_no")
tree.heading("three", text="property_no")
tree.heading("four", text="Yourr_ph_no")
tree.heading("five", text="Client_ph_no")

tree.column("one", width=100)
tree.column("two", width=100)
tree.column("three", width=100)
tree.column("four", width=100)
tree.column("five", width=100)

display_button = tk.Button(frame, text="Refresh", command=open_code_2,bg="#1ABC9C")
display_button.pack()

root.mainloop()
