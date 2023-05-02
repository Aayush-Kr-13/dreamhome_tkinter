import tkinter as tk
from tempCodeRunnerFile import db
import string
import os

def submit_data():
    property_no = property_no_entry.get()
    property_type = property_type_entry.get()
    rooms = rooms_entry.get()
    rent = rent_entry.get()
    Address_hno=Address_hno_entry.get()
    Address_street=Address_street_entry.get()
    city=city_entry.get()
    postal_code=postal_code_entry.get()
    owner_name=owner_name_entry.get()
    owner_id=owner_id_entry.get()
    cursor = db.cursor()
    sql = "INSERT INTO properties (property_no, property_type, rooms, rent, Address_hno, Address_street, city, postal_code, owner_name, owner_id) VALUES (%s, %s, %s, %s,%s,%s, %s, %s, %s,%s)"
    values = (property_no, property_type, rooms, rent, Address_hno, Address_street, city, postal_code, owner_name, owner_id)
    cursor.execute(sql, values)
    db.commit()
    db.close()
    property_no_entry.delete(0, tk.END)
    property_type_entry.delete(0, tk.END)
    rooms_entry.delete(0, tk.END)
    rent_entry.delete(0, tk.END)
    Address_hno_entry.delete(0, tk.END)
    Address_street_entry.delete(0, tk.END)
    city_entry.delete(0, tk.END)
    postal_code_entry.delete(0, tk.END)
    owner_name_entry.delete(0, tk.END)
    owner_id_entry.delete(0, tk.END)
    open_code_1()
    tk.messagebox.showinfo("Success", "Data submitted successfully")

def open_code_1():
    root.destroy()
    os.system("python dreamhome_tkinter\\userinterface.py")

root = tk.Tk()
root.geometry("400x700")
frame = tk.Frame(root, width=350, height=700, bg="#2C3E50")
frame.pack(fill=tk.BOTH, expand=True)

root.title("Property Registration")

large_font = ('Verdana', 19)
large_font1 = ('Verdana', 10)

user_label = tk.Label(frame, text="Property Registration",bg="#2C3E50",fg="Orange",font=large_font)
user_label.place(x=70,y=22)

button1 = tk.Button(frame, text="Back",fg="red", command=open_code_1)
button1.place(x=10,y=10)

property_no_label = tk.Label(frame, text="Property Number:")
property_no_label.place(x=30,y=80)
property_no_entry = tk.Entry(frame)
property_no_entry.place(x=180,y=80)

property_type_label = tk.Label(frame, text="Property Type:")
property_type_label.place(x=30,y=140)
property_type_entry = tk.Entry(frame)
property_type_entry.place(x=180,y=140)

rooms_label = tk.Label(frame, text="Number Of Rooms:")
rooms_label.place(x=30,y=200)
rooms_entry = tk.Entry(frame)
rooms_entry.place(x=180,y=200)

rent_label = tk.Label(frame, text="Enter Rent:")
rent_label.place(x=30,y=260)
rent_entry = tk.Entry(frame)
rent_entry.place(x=180,y=260)

Address_hno_label = tk.Label(frame, text="Enter House Number:")
Address_hno_label.place(x=30,y=320)
Address_hno_entry = tk.Entry(frame)
Address_hno_entry.place(x=180,y=320)

Address_street_label = tk.Label(frame, text="Enter Street Name:")
Address_street_label.place(x=30,y=380)
Address_street_entry = tk.Entry(frame)
Address_street_entry.place(x=180,y=380)

city_label = tk.Label(frame, text="Enter City:")
city_label.place(x=30,y=440)
city_entry = tk.Entry(frame)
city_entry.place(x=180,y=440)

postal_code_label = tk.Label(frame, text="Enter Postal Code:")
postal_code_label.place(x=30,y=500)
postal_code_entry = tk.Entry(frame)
postal_code_entry.place(x=180,y=500)

owner_name_label = tk.Label(frame, text="Enter Owner Name:")
owner_name_label.place(x=30,y=560)
owner_name_entry = tk.Entry(frame)
owner_name_entry.place(x=180,y=560)

owner_id_label = tk.Label(frame, text="Enter Owner Id:")
owner_id_label.place(x=30,y=620)
owner_id_entry = tk.Entry(frame)
owner_id_entry.place(x=180,y=620)

submit_button = tk.Button(frame, text="Submit",bg="#1ABC9C", command=submit_data)
submit_button.place(x=160,y=660)

root.mainloop()


