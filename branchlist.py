import tkinter as tk
import mysql.connector

def show_table():
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='12345',
        database='proj'
    )
    root.destroy()
    cursor = db.cursor()
    
    cursor.execute("SELECT * FROM branches")
    rows = cursor.fetchall()
    
    table = tk.Tk()
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            e = tk.Entry(table, width=15, fg='blue', font=('Arial', 14))
            e.grid(row=i, column=j)
            e.insert(tk.END, rows[i][j])
    
    table.mainloop()

root = tk.Tk()
root.geometry("350x350")
root.title("Branch Info")
frame = tk.Frame(root, width=350, height=350, bg="#2C3E50")
frame.pack(fill=tk.BOTH, expand=True)

button = tk.Button(frame, text="All Branch List", command=show_table)
button.pack(pady=20)

root.mainloop()
