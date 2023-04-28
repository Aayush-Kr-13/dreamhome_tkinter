import tkinter as tk
import random
import string
import os
from tempCodeRunnerFile import db

def generate_random_string(length):
    all_chars = list(string.digits + string.ascii_letters.upper())
    random.shuffle(all_chars)
    random_chars = random.sample(all_chars, length)
    return ''.join(random_chars)

def submit_data():
    owner = owner_entry.get()
    client = client_entry.get()
    property = property_entry.get()
    city = city_entry.get()
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='12345',
        database='proj'
    )
    lease_id = generate_random_string(6)
    cursor = db.cursor()
    sql = "INSERT INTO lease (lease_id , owner_id, client_id, property_no, city) VALUES (%s, %s, %s, %s,%s)"
    values = (lease_id ,owner, client, property, city)
    cursor.execute(sql, values)
    owner_entry.delete(0, tk.END)
    client_entry.delete(0, tk.END)
    db.commit()
    success_label = tk.Label(root, text="Registrartion Successful!",bg="lightgreen")
    success_label.place(x=120, y=330)
    clientid_label = tk.Label(root, text="Your Lease Id is :" + lease_id)
    clientid_label.place(x=120, y=370)
    lease_id=""
    delete_property()

def delete_property():
    property = property_entry.get()
    city = city_entry.get()
    mycursor = db.cursor()
    sql = "DELETE FROM properties WHERE property_no = %s and city = %s;"
    values = (property,city)
    mycursor.execute(sql, values)
    property_entry.delete(0, tk.END)
    city_entry.delete(0, tk.END)
    db.commit()
    db.close()

def open_code_1():
    root.destroy()
    os.system("python staffinterface.py")
   
root = tk.Tk()
root.title("Lease Form")

root.geometry("350x450")
frame = tk.Frame(root, width=350, height=450, bg="#2C3E50")
frame.pack(fill=tk.BOTH, expand=True)

large_font = ('Verdana', 19)
large_font1 = ('Verdana', 10)

user_label = tk.Label(frame, text="Lease Form",bg="#2C3E50",fg="Orange",font=large_font)
user_label.place(x=100,y=35)

button1 = tk.Button(frame, text="Back",fg="red", command=open_code_1)
button1.place(x=10,y=10)

owner_label = tk.Label(frame, text="Owner Id:")
owner_label.place(x=60,y=110)
owner_entry = tk.Entry(frame)
owner_entry.place(x=180,y=110)

client_label = tk.Label(frame, text="Client Id:")
client_label.place(x=60,y=170)
client_entry = tk.Entry(frame)
client_entry.place(x=180,y=170)

property_label = tk.Label(frame, text="Property No:")
property_label.place(x=60,y=230)
property_entry = tk.Entry(frame)
property_entry.place(x=180,y=230)

city_label = tk.Label(frame, text="City:")
city_label.place(x=60,y=290)
city_entry = tk.Entry(frame)
city_entry.place(x=180,y=290)

submit_button = tk.Button(frame, text="Submit",bg="#1ABC9C", command=submit_data)
submit_button.place(x=150,y=400)

root.mainloop()


