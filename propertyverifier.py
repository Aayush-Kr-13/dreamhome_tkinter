import tkinter as tk
import mysql.connector

# Establish connection to MySQL database
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345",
  database="proj"
)

# Create cursor object to execute MySQL queries
cursor = db.cursor()

# Define function to verify property
def verify_property():
  property_number = property_number_entry.get()
  fullName = fullName_entry.get()
  # Execute MySQL query to update verification field
  query = f"UPDATE properties SET verificiation = TRUE WHERE property_no = '{property_number}' AND owner_name='{fullName}'"
  cursor.execute(query)
  db.commit()
  property_number_entry.delete(0, 'end')
  fullName_entry.delete(0, 'end')
  # Check if any rows were affected by the query
  if cursor.rowcount > 0:
    result_label.config(text="Property verified")
  else:
    result_label.config(text="Property not found")


# Create main tkinter window
window = tk.Tk()
window.geometry("350x500")
frame = tk.Frame(window, width=350, height=350, bg="lightgreen")
frame.pack(fill=tk.BOTH, expand=True)

# Add form elements to window
property_number_label = tk.Label(frame, text="Property number:")
property_number_label.grid(row = 0, column = 0 , padx=20,pady=30)
property_number_entry = tk.Entry(frame)
property_number_entry.grid(row = 0, column = 1 , padx=20,pady=30)

fullName_label = tk.Label(frame, text="Owner LName:")
fullName_label.grid(row = 1, column = 0 , padx=20,pady=30)
fullName_entry = tk.Entry(frame)
fullName_entry.grid(row = 1, column = 1 , padx=20,pady=30)

verify_button = tk.Button(frame, text="Verify", command=verify_property)
verify_button.grid(row = 2, column = 0 , columnspan=2)
result_label = tk.Label(frame, text="")


window.mainloop()
