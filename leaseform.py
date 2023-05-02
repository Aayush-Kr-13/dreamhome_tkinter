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
    lease_id = generate_random_string(6)
    sdate_id = sdate_entry.get()
    edate_id = edate_entry.get()
    cursor = db.cursor()
    sql = "INSERT INTO lease (lease_id , owner_id, client_id, property_no, city,sdate,edate) VALUES (%s, %s, %s, %s,%s,%s,%s)"
    values = (lease_id ,owner, client, property, city,sdate_id,edate_id)
    cursor.execute(sql, values)
    owner_entry.delete(0, tk.END)
    client_entry.delete(0, tk.END)
    db.commit()
    success_label = tk.Label(root, text="Registrartion Successful!",bg="lightgreen")
    success_label.place(x=120, y=460)
    clientid_label = tk.Label(root, text="Your Lease Id is :" + lease_id)
    clientid_label.place(x=120, y=490)
    lease_id=""
    delete_property()

def delete_property():
    property = property_entry.get()
    city = city_entry.get()
    mycursor = db.cursor()
    sql = "UPDATE properties SET available = false WHERE property_no = %s and city = %s;"
    values = (property,city)
    mycursor.execute(sql, values)
    property_entry.delete(0, tk.END)
    city_entry.delete(0, tk.END)
    sdate_entry.delete(0,tk.END)
    edate_entry.delete(0,tk.END)
    db.commit()
    db.close()

def open_code_1():
    root.destroy()
    os.system("python dreamhome_tkinter//staffinterface.py")
   
root = tk.Tk()
root.title("Lease Form")

root.geometry("500x550")
frame = tk.Frame(root, width=500, height=550, bg="#2C3E50")
frame.pack(fill=tk.BOTH, expand=True)

large_font = ('Verdana', 30)
large_font1 = ('Verdana', 13)

user_label = tk.Label(frame, text="Lease Form",bg="#2C3E50",fg="Orange",font=large_font)
user_label.place(x=120,y=25)

button1 = tk.Button(frame, text="Back",fg="red", command=open_code_1)
button1.place(x=10,y=10)

owner_label = tk.Label(frame, text="Owner Id:",font=large_font1)
owner_label.place(x=80,y=120)
owner_entry = tk.Entry(frame)
owner_entry.place(x=260,y=120)

client_label = tk.Label(frame, text="Client Id:",font=large_font1)
client_label.place(x=80,y=180)
client_entry = tk.Entry(frame)
client_entry.place(x=260,y=180)

property_label = tk.Label(frame, text="Property No :",font=large_font1)
property_label.place(x=80,y=240)
property_entry = tk.Entry(frame)
property_entry.place(x=260,y=240)

city_label = tk.Label(frame, text="City :",font=large_font1)
city_label.place(x=80,y=300)
city_entry = tk.Entry(frame)
city_entry.place(x=260,y=300)

sdate_label = tk.Label(frame, text="Start Date :",font=large_font1)
sdate_label.place(x=80,y=360)
sdate_entry = tk.Entry(frame)
sdate_entry.place(x=260,y=360)

edate_label = tk.Label(frame, text="End Date :",font=large_font1)
edate_label.place(x=80,y=420)
edate_entry = tk.Entry(frame)
edate_entry.place(x=260,y=420)

submit_button = tk.Button(frame, text="Submit",bg="#1ABC9C", command=submit_data,font=large_font1)
submit_button.place(x=180,y=505)

root.mainloop()


