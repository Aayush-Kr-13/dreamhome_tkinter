import tkinter as tk
import os

def open_code_1():
    root.destroy()
    os.system("python addbranch.py")

def open_code_2():
    root.destroy()
    os.system("python propertylist.py")
    
def open_code_3():
    root.destroy()
    os.system("python branchlist.py")
    
def open_code_4():
    root.destroy()
    os.system("python dreamhome_tkinter\\staffregisteration.py")
    

root = tk.Tk()
root.geometry("350x350")
frame = tk.Frame(root, width=350, height=350, bg="lightgreen")
frame.pack(fill=tk.BOTH, expand=True)

button1 = tk.Button(frame, text="Add Branch", command=open_code_1)
button2 = tk.Button(frame, text="List Property", command=open_code_2)
button3 = tk.Button(frame, text="List Branch", command=open_code_3)
button4 = tk.Button(frame, text="Register Staff", command=open_code_4)

button1.pack(pady=30)
button2.pack(pady=30)
button3.pack(pady=30)
button4.pack(pady=30)

root.mainloop()
