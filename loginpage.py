import tkinter as tk
import os

def open_code_1():
    root.destroy()
    os.system("python userlogin.py")

def open_code_2():
    root.destroy()
    os.system("python stafflogin.py")
    
def open_code_3():
    root.destroy()
    os.system("python adminlogin.py")

root = tk.Tk()
root.geometry("350x350")
frame = tk.Frame(root, width=350, height=350, bg="lightgreen")
frame.pack(fill=tk.BOTH, expand=True)

button1 = tk.Button(frame, text="User Login", command=open_code_1)
button2 = tk.Button(frame, text="Staff Login", command=open_code_2)
button3 = tk.Button(frame, text="Admin Login", command=open_code_3)

button1.pack(pady=30)
button2.pack(pady=30)
button3.pack(pady=30)

root.mainloop()
