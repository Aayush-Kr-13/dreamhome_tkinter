import tkinter as tk
import mysql.connector
from tkinter import ttk
import os

def open_code_1():
    root.destroy()
    os.system("python dreamhome_tkinter\\userInterface.py")

db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Aayush@2301',
        database='Dreamhouse'
)
    
def display_table():
    tree.delete(*tree.get_children())
    cursor = db.cursor()
    cursor.execute("SELECT * FROM properties")
    data = cursor.fetchall()
    for row in data:
        tree.insert("", "end", values=row)

root = tk.Tk()
root.title("Property List")
root.geometry("1400x600")
frame = tk.Frame(root, width=1400, height=600, bg="#2C3E50")
frame.pack(fill=tk.BOTH, expand=True)

large_font = ('Verdana', 15)

button1 = tk.Button(frame, text="Back",fg="red", command=open_code_1)
button1.place(x=5,y=3)

user_label = tk.Label(frame, text="Property List",bg="#2C3E50",fg="Orange",font=large_font)
user_label.pack()


tree = ttk.Treeview(frame)
tree.pack(fill="both", expand=True)

tree["columns"] = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven")

tree.heading("one", text="Property No")
tree.heading("two", text="Property Type")
tree.heading("three", text="Rooms")
tree.heading("four", text="Rent")
tree.heading("five", text="Address Hno")
tree.heading("six", text="Address Street")
tree.heading("seven", text="City")
tree.heading("eight", text="Postal Code")
tree.heading("nine", text="Owner Name")
tree.heading("ten", text="Owner Number")
tree.heading("eleven", text="Verified")

tree.column("one", width=100)
tree.column("two", width=100)
tree.column("three", width=100)
tree.column("four", width=100)
tree.column("five", width=100)
tree.column("six", width=100)
tree.column("seven", width=100)
tree.column("eight", width=100)
tree.column("nine", width=100)
tree.column("ten", width=100)
tree.column("eleven", width=100)

display_button = tk.Button(frame, text="Display Properties", command=display_table,bg="#1ABC9C")
display_button.pack()

root.mainloop()
