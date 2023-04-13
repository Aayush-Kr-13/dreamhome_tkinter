import tkinter as tk
import mysql.connector

# Connect to MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345",
  database="proj"
)

# Create tkinter window
root = tk.Tk()
root.title("Client Search")

# Set window size and background color
root.geometry("400x250")
root.configure(bg="#c1f0c1")

# Create labels and entry fields for client ID, last name, and property number
client_id_label = tk.Label(root, text="Client ID:", bg="#c1f0c1")
client_id_label.grid(row=0, column=0, padx=10, pady=10)
client_id_entry = tk.Entry(root)
client_id_entry.grid(row=0, column=1, padx=10, pady=10)

last_name_label = tk.Label(root, text="Last Name:", bg="#c1f0c1")
last_name_label.grid(row=1, column=0, padx=10, pady=10)
last_name_entry = tk.Entry(root)
last_name_entry.grid(row=1, column=1, padx=10, pady=10)

property_no_label = tk.Label(root, text="Property Number:", bg="#c1f0c1")
property_no_label.grid(row=2, column=0, padx=10, pady=10)
property_no_entry = tk.Entry(root)
property_no_entry.grid(row=2, column=1, padx=10, pady=10)

def show_message():
    popup = tk.Toplevel()
    popup.title("Message")
    popup.geometry("200x100")
    popup_label = tk.Label(popup, text="Property not found")
    popup_label.pack(padx=10, pady=10)

# Create function to search for client and property details in MySQL database
def search_database():
    # Get values from entry fields
    client_id = client_id_entry.get()
    last_name = last_name_entry.get()
    property_no = property_no_entry.get()
    
    # Query MySQL database for client details
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM clients WHERE lname = %s and clientno=%s", (last_name,client_id))
    client = mycursor.fetchone()
    
    # If client exists, get client number and telephone number from properties table
    if client is not None:
        mycursor.execute("SELECT owner_number FROM properties WHERE property_no = %s", (property_no,))
        property_info = mycursor.fetchone()
        if property_info is not None:
            owner_ph_no = property_info[0]
            mycursor.execute("SELECT telno FROM clients WHERE clientno = %s", (client_id,))
            client_ph_no = mycursor.fetchone()[0]
            mycursor.execute("SELECT clientno FROM clients WHERE telno = %s", (owner_ph_no,))
            owner_no = mycursor.fetchone()[0]
            mycursor.execute("INSERT INTO INTERESTS(owner_no,client_no,property_no,owner_ph_no,client_ph_no) VALUES(%s,%s,%s,%s,%s)", (owner_no,client_id,property_no,owner_ph_no,client_ph_no))
            mydb.commit()
            mydb.close()
            result_label.config(text="Interest added successfully.", fg="green")
        else:
            show_message()
            result_label.config(text="Incorrect Credentials.", fg="red")
    else:
        show_message()
        result_label.config(text="Incorrect Credentials.", fg="red")
    
# Create button to search database and add interest
search_button = tk.Button(root, text="Search and Add Interest", command=search_database)
search_button.grid(row=3, column=1, padx=10, pady=10)

# Create label to display search result
result_label = tk.Label(root, bg="#c1f0c1")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Run tkinter main loop
root.mainloop()
