import tkinter as tk
import mysql.connector
import string
import os

def submit_data():
    branch_id = branchid_entry.get()
    branch_name = branchname_entry.get()
    branch_hno = branch_hno_entry.get()
    branch_street = branch_street_entry.get()
    branch_city=branch_city_entry.get()
    branch_postal_code=branch_postal_code_entry.get()
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='12345',
        database='proj'
    )
    cursor = db.cursor()
    sql = "INSERT INTO branches (branch_id, branch_name, branch_hno, branch_street, branch_city, branch_postal_code) VALUES (%s, %s, %s, %s,%s,%s)"
    values = (branch_id, branch_name, branch_hno, branch_street, branch_city, branch_postal_code)
    cursor.execute(sql, values)
    db.commit()
    db.close()
    branchid_entry.delete(0, tk.END)
    branchname_entry.delete(0, tk.END)
    branch_hno_entry.delete(0, tk.END)
    branch_street_entry .delete(0, tk.END)
    branch_city_entry.delete(0, tk.END)
    branch_postal_code_entry.delete(0, tk.END)
    tk.messagebox.showinfo("Success", "Data submitted successfully")

def open_code_1():
    root.destroy()
    os.system("python main.py")

root = tk.Tk()
root.geometry("350x500")
frame = tk.Frame(root, width=350, height=500, bg="lightgreen")
frame.pack(fill=tk.BOTH, expand=True)

root.title("Property Registration")

button1 = tk.Button(frame, text="Home",fg="red", command=open_code_1)
button1.grid(row=0,column=1,columnspan=2,pady=10)

branchid_label = tk.Label(frame, text="branchid:")
branchid_label.grid(row=1, column=1, padx=10, pady=10)
branchid_entry = tk.Entry(frame)
branchid_entry.grid(row=1, column=2)

branchname_label = tk.Label(frame, text="Branch Name:")
branchname_label.grid(row=2, column=1, padx=10, pady=10)
branchname_entry = tk.Entry(frame)
branchname_entry.grid(row=2, column=2)

branch_hno_label = tk.Label(frame, text="Branch Hno:")
branch_hno_label.grid(row=3, column=1, padx=10, pady=10)
branch_hno_entry = tk.Entry(frame)
branch_hno_entry.grid(row=3, column=2)

branch_street_label = tk.Label(frame, text="Branch street:")
branch_street_label.grid(row=4, column=1, padx=10, pady=10)
branch_street_entry = tk.Entry(frame)
branch_street_entry.grid(row=4, column=2)

branch_city_label = tk.Label(frame, text="Enter City :")
branch_city_label.grid(row=6, column=1, padx=10, pady=10)
branch_city_entry = tk.Entry(frame)
branch_city_entry.grid(row=6, column=2)

branch_postal_code_label = tk.Label(frame, text="Enter postal Code:")
branch_postal_code_label.grid(row=7, column=1, padx=10, pady=10)
branch_postal_code_entry = tk.Entry(frame)
branch_postal_code_entry.grid(row=7, column=2)


submit_button = tk.Button(frame, text="Submit",fg="brown", command=submit_data)
submit_button.grid(row=11, column=1, columnspan=3, padx=30, pady=10)

root.mainloop()


