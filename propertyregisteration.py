import tkinter as tk
import mysql.connector
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
    owner_number=owner_number_entry.get()
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='12345',
        database='proj'
    )
    cursor = db.cursor()
    sql = "INSERT INTO properties (property_no, property_type, rooms, rent, Address_hno, Address_street, city, postal_code, owner_name, owner_number) VALUES (%s, %s, %s, %s,%s,%s, %s, %s, %s,%s)"
    values = (property_no, property_type, rooms, rent, Address_hno, Address_street, city, postal_code, owner_name, owner_number)
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
    owner_number_entry.delete(0, tk.END)
    open_code_1()
    tk.messagebox.showinfo("Success", "Data submitted successfully")

def open_code_1():
    root.destroy()
    os.system("python userinterface.py")

root = tk.Tk()
root.geometry("350x500")
frame = tk.Frame(root, width=350, height=500, bg="lightgreen")
frame.pack(fill=tk.BOTH, expand=True)

root.title("Property Registration")

button1 = tk.Button(frame, text="Home",fg="red", command=open_code_1)
button1.grid(row=0,column=1,columnspan=2,pady=10)

property_no_label = tk.Label(frame, text="Property Number:")
property_no_label.grid(row=1, column=1, padx=10, pady=10)
property_no_entry = tk.Entry(frame)
property_no_entry.grid(row=1, column=2)

property_type_label = tk.Label(frame, text="Property Type:")
property_type_label.grid(row=2, column=1, padx=10, pady=10)
property_type_entry = tk.Entry(frame)
property_type_entry.grid(row=2, column=2)

rooms_label = tk.Label(frame, text="Number Of Rooms:")
rooms_label.grid(row=3, column=1, padx=10, pady=10)
rooms_entry = tk.Entry(frame)
rooms_entry.grid(row=3, column=2)

rent_label = tk.Label(frame, text="Enter Rent:")
rent_label.grid(row=4, column=1, padx=10, pady=10)
rent_entry = tk.Entry(frame)
rent_entry.grid(row=4, column=2)

Address_hno_label = tk.Label(frame, text="Enter House Number:")
Address_hno_label.grid(row=5, column=1, padx=10, pady=10)
Address_hno_entry = tk.Entry(frame)
Address_hno_entry.grid(row=5, column=2)

Address_street_label = tk.Label(frame, text="Enter Street Name:")
Address_street_label.grid(row=6, column=1, padx=10, pady=10)
Address_street_entry = tk.Entry(frame)
Address_street_entry.grid(row=6, column=2)

city_label = tk.Label(frame, text="Enter City:")
city_label.grid(row=7, column=1, padx=10, pady=10)
city_entry = tk.Entry(frame)
city_entry.grid(row=7, column=2)

postal_code_label = tk.Label(frame, text="Enter Postal Code:")
postal_code_label.grid(row=8, column=1, padx=10, pady=10)
postal_code_entry = tk.Entry(frame)
postal_code_entry.grid(row=8, column=2)

owner_name_label = tk.Label(frame, text="Enter Owner Name:")
owner_name_label.grid(row=9, column=1, padx=10, pady=10)
owner_name_entry = tk.Entry(frame)
owner_name_entry.grid(row=9, column=2)

owner_number_label = tk.Label(frame, text="Enter Owner Number:")
owner_number_label.grid(row=10, column=1, padx=10, pady=10)
owner_number_entry = tk.Entry(frame)
owner_number_entry.grid(row=10, column=2)

submit_button = tk.Button(frame, text="Submit",fg="brown", command=submit_data)
submit_button.grid(row=11, column=1, columnspan=3, padx=30, pady=10)

root.mainloop()


