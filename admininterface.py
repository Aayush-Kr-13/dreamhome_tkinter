import tkinter as tk
import os

def open_code_1():
    root.destroy()
    os.system("python dreamhome_tkinter\\addbranch.py")

def open_code_2():
    root.destroy()
    os.system("python dreamhome_tkinter\\propertylist.py")
    
def open_code_3():
    root.destroy()
    os.system("python dreamhome_tkinter\\branchlist.py")
    
def open_code_4():
    root.destroy()
    os.system("python dreamhome_tkinter\\staffregisteration.py")
    
def open_code_5():
    root.destroy()
    os.system("python dreamhome_tkinter\\loginpage.py")
    

root = tk.Tk()
root.geometry("400x400")
frame = tk.Frame(root, width=400, height=400, bg="#2C3E50")
frame.pack(fill=tk.BOTH, expand=True)

button1 = tk.Button(frame, text="Log Out",fg="red", command=open_code_5)
button1.place(x=10,y=10)

large_font = ('Verdana', 20)
large_font1 = ('Verdana', 10)

admin_label = tk.Label(frame, text="Welcome Admin!",bg="#2C3E50",fg="Orange",font=large_font)
admin_label.place(x=100,y=35)

button1 = tk.Button(frame, text="Add Branch", command=open_code_1)
button1.place(x=160,y=130)
button2 = tk.Button(frame, text="List Property", command=open_code_2)
button2.place(x=160,y=200)
button3 = tk.Button(frame, text="List Branch", command=open_code_3)
button3.place(x=160,y=270)
button4 = tk.Button(frame, text="Register Staff", command=open_code_4)
button4.place(x=160,y=340)

root.mainloop()
