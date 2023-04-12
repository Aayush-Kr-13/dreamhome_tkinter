import tkinter as tk
import mysql.connector

def show_table():
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Aayush@2301',
        database='Dreamhouse'
    )
    root.destroy()
    cursor = db.cursor()
    
    cursor.execute("SELECT * FROM properties")
    rows = cursor.fetchall()
    
    table = tk.Tk()
    for i in range(len(rows)):
        for j in range(1,len(rows[i])):
            e = tk.Entry(table, width=10, fg='blue', font=('Arial', 16))
            e.grid(row=i, column=j)
            e.insert(tk.END, rows[i][j])
    
    table.mainloop()

root = tk.Tk()
root.geometry("350x350")
frame = tk.Frame(root, width=350, height=350, bg="lightgreen")
frame.pack(fill=tk.BOTH, expand=True)

button = tk.Button(frame, text="Available Properties", command=show_table)
button.pack(pady=20)

root.mainloop()
