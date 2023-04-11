import tkinter as tk
import mysql.connector
import string

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
        password='Aayush@2301',
        database='Dreamhouse'
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
    tk.messagebox.showinfo("Success", "Data submitted successfully")
    
root = tk.Tk()
root.title("Property Registration")

property_no_label = tk.Label(root, text="Property Number:")
property_no_label.grid(row=0, column=0)
property_no_entry = tk.Entry(root)
property_no_entry.grid(row=0, column=1)

property_type_label = tk.Label(root, text="Property Type:")
property_type_label.grid(row=1, column=0)
property_type_entry = tk.Entry(root)
property_type_entry.grid(row=1, column=1)

rooms_label = tk.Label(root, text="Number Of Rooms:")
rooms_label.grid(row=2, column=0)
rooms_entry = tk.Entry(root)
rooms_entry.grid(row=2, column=1)

rent_label = tk.Label(root, text="Enter Rent:")
rent_label.grid(row=3, column=0)
rent_entry = tk.Entry(root)
rent_entry.grid(row=3, column=1)

Address_hno_label = tk.Label(root, text="Enter House Number:")
Address_hno_label.grid(row=4, column=0)
Address_hno_entry = tk.Entry(root)
Address_hno_entry.grid(row=4, column=1)

Address_street_label = tk.Label(root, text="Enter Street Name:")
Address_street_label.grid(row=5, column=0)
Address_street_entry = tk.Entry(root)
Address_street_entry.grid(row=5, column=1)

city_label = tk.Label(root, text="Enter City:")
city_label.grid(row=6, column=0)
city_entry = tk.Entry(root)
city_entry.grid(row=6, column=1)

postal_code_label = tk.Label(root, text="Enter Postal Code:")
postal_code_label.grid(row=7, column=0)
postal_code_entry = tk.Entry(root)
postal_code_entry.grid(row=7, column=1)

owner_name_label = tk.Label(root, text="Enter Owner Name:")
owner_name_label.grid(row=8, column=0)
owner_name_entry = tk.Entry(root)
owner_name_entry.grid(row=8, column=1)

owner_number_label = tk.Label(root, text="Enter Owner Number:")
owner_number_label.grid(row=9, column=0)
owner_number_entry = tk.Entry(root)
owner_number_entry.grid(row=9, column=1)

submit_button = tk.Button(root, text="Submit", command=submit_data)
submit_button.grid(row=10, column=0, columnspan=2)

root.mainloop()


