import tkinter as tk
import os

def open_code_1():
    root.destroy()
    os.system("python propertyregisteration.py")

def open_code_2():
    root.destroy()
    os.system("python propertylist.py")

root = tk.Tk()
root.geometry("350x350")
frame = tk.Frame(root, width=350, height=350, bg="lightgreen")
frame.pack(fill=tk.BOTH, expand=True)

button1 = tk.Button(frame, text="Register Property", command=open_code_1)
button2 = tk.Button(frame, text="Search For Property", command=open_code_2)

button1.pack(pady=30)
button2.pack(pady=30)


root.mainloop()
