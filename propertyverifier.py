import tkinter as tk
import mysql.connector
import os

def open_code_1():
  verify_button.config(background="Green")
  verify_button.config(background="Green")
  window.destroy()
  os.system("python propertyverifier.py")

def open_code_2():
  window.destroy()
  os.system("python loginpage.py")
  
def back_button():
  window.destroy()
  os.system("python staffinterface.py")

db = mysql.connector.connect(
  host='localhost',
  user='root',
  password='12345',
  database='proj'
)

cursor = db.cursor()

def verify_property():
  property_number = property_number_entry.get()
  fullName = fullName_entry.get()
  query = f"UPDATE properties SET verificiation = TRUE WHERE property_no = '{property_number}' AND owner_name='{fullName}'"
  cursor.execute(query)
  db.commit()
  property_number_entry.delete(0, 'end')
  fullName_entry.delete(0, 'end')
  if cursor.rowcount > 0:
    result_label.config(text="Property verified")
    open_code_1()
  else:
    result_label.config(text="Property not found")


window = tk.Tk()
window.geometry("350x350")
window.title("Property Verifier")
frame = tk.Frame(window, width=350, height=350, bg="#2C3E50")
frame.pack(fill=tk.BOTH, expand=True)

large_font = ('Verdana', 15)
large_font1 = ('Verdana', 10)

button1 = tk.Button(frame, text="Log Out",fg="red", command=open_code_2)
button1.place(x=10,y=10)

staff_label = tk.Label(frame, text="Verify Property!",bg="#2C3E50",fg="Orange",font=large_font)
staff_label.place(x=100,y=35)

property_number_label = tk.Label(frame, text="Property number:",bg="#2C3E50",fg="white",font=large_font1)
property_number_label.place(x=30,y=100)
property_number_entry = tk.Entry(frame)
property_number_entry.place(x=180,y=100)

fullName_label = tk.Label(frame, text="Owner Name:",bg="#2C3E50",fg="white",font=large_font1)
fullName_label.place(x=30,y=180)
fullName_entry = tk.Entry(frame)
fullName_entry.place(x=180,y=180)

verify_button = tk.Button(frame, text="Verify", command=verify_property,bg="#1ABC9C")
verify_button.place(x=110,y=260)

back_button = tk.Button(frame, text="Back", command=back_button,bg="grey")
back_button.place(x=180,y=260)

result_label = tk.Label(frame, text="")


window.mainloop()
