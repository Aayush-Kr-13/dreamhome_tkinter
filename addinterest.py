import tkinter as tk
import mysql.connector
import os
from tempCodeRunnerFile import db

def open_code_2():
  root.destroy()
  os.system("python dreamhome_tkinter//userInterface.py")

def search_database():
    client_id = client_id_entry.get()
    last_name = last_name_entry.get()
    property_no = property_no_entry.get()
    
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM clients WHERE lname = %s and clientno=%s", (last_name,client_id))
    client = mycursor.fetchone()
    
    if client is not None:
        mycursor.execute("SELECT owner_number FROM properties WHERE property_no = %s", (property_no,))
        property_info = mycursor.fetchone()
        if property_info is not None:
            mycursor.execute("UPDATE properties SET rating=rating+1 WHERE property_no = %s", (property_no,))
            owner_ph_no = property_info[0]
            mycursor.execute("SELECT telno FROM clients WHERE clientno = %s", (client_id,))
            client_ph_no = mycursor.fetchone()[0]
            mycursor.execute("SELECT clientno FROM clients WHERE telno = %s", (owner_ph_no,))
            owner_no = mycursor.fetchone()[0]
            mycursor.execute("INSERT INTO INTERESTS(owner_no,client_no,property_no,owner_ph_no,client_ph_no) VALUES(%s,%s,%s,%s,%s)", (owner_no,client_id,property_no,owner_ph_no,client_ph_no))
            db.commit()
            db.close()
            success_label = tk.Label(root, text="Registration Successful!",bg="lightgreen")
            success_label.place(x=130, y=260)
        else:
            error_label = tk.Label(root, text="Incorrect Credentials",bg="Red")
            error_label.place(x=130, y=260)
    else:
        error_label = tk.Label(root, text="Incorrect Credentials",bg="Red")
        error_label.place(x=130, y=260)

root = tk.Tk()
root.title("Client Search")
root.geometry("350x350")
frame = tk.Frame(root, width=350, height=350, bg="#2C3E50")
frame.pack(fill=tk.BOTH, expand=True)

large_font = ('Verdana', 20)
large_font1 = ('Verdana', 10)

button1 = tk.Button(frame, text="Back",fg="red", command=open_code_2)
button1.place(x=5,y=5)

staff_label = tk.Label(frame, text="Add Interest",bg="#2C3E50",fg="Orange",font=large_font)
staff_label.place(x=75,y=35)

client_id_label = tk.Label(root, text="User ID:",bg="#2C3E50",fg="white",font=large_font1)
client_id_label.place(x=40,y=100)
client_id_entry = tk.Entry(root)
client_id_entry.place(x=180,y=100)

last_name_label = tk.Label(root, text="Last Name:", bg="#2C3E50",fg="white",font=large_font1)
last_name_label.place(x=40,y=160)
last_name_entry = tk.Entry(root)
last_name_entry.place(x=180,y=160)

property_no_label = tk.Label(root, text="Property Number:",bg="#2C3E50",fg="white",font=large_font1)
property_no_label.place(x=40,y=220)
property_no_entry = tk.Entry(root)
property_no_entry.place(x=180,y=220)
    
search_button = tk.Button(root, text="Search and Add Interest", command=search_database,bg="#1ABC9C")
search_button.place(x=100,y=300)

root.mainloop()
