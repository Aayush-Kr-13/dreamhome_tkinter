import tkinter as tk
import mysql.connector

def show_table(city):
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Aayush@2301',
        database='Dreamhouse'
    )
    root.destroy()
    cursor = db.cursor()
    
    cursor.execute("SELECT * FROM properties WHERE city = %s", (city,))
    rows = cursor.fetchall()
    
    table = tk.Tk()
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            e = tk.Entry(table, width=10, fg='blue', font=('Arial', 16))
            e.grid(row=i, column=j)
            e.insert(tk.END, rows[i][j])
    table.mainloop()

root = tk.Tk()
root.title("Property List")
root.geometry("350x350")
frame = tk.Frame(root, width=350, height=350, bg="#2C3E50")
frame.pack(fill=tk.BOTH, expand=True)

city_label = tk.Label(frame, text="Enter city name:")
city_label.pack(pady=10)

inp_city = tk.Entry(frame)
inp_city.pack(pady=5)

button = tk.Button(frame, text="Available Properties", command=lambda: show_table(inp_city.get()))
button.pack(pady=20)

root.mainloop()
