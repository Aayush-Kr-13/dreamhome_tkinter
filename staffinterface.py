import tkinter as tk
import os

def open_code_1():
    root.destroy()
    os.system("python propertyverifier.py")

def open_code_2():
    root.destroy()
    os.system("python propertylist.py")
    
def open_code_3():
    root.destroy()
    os.system("python dreamhome_tkinter\\leaseform.py")

def open_code_4():
    root.destroy()
    os.system("python dreamhome_tkinter\\loginpage.py")  

root = tk.Tk()
root.title("Staff Interface")
root.geometry("350x350")
frame = tk.Frame(root, width=350, height=350, bg="#2C3E50")
frame.pack(fill=tk.BOTH, expand=True)

large_font = ('Verdana', 25)
large_font1 = ('Verdana', 10)

staff_label = tk.Label(frame, text="Welcome Staff!",bg="#2C3E50",fg="Orange",font=large_font)
staff_label.place(x=40,y=45)

button1 = tk.Button(frame, text="Log Out",fg="red", command=open_code_4,font=large_font1)
button1.place(x=10,y=10)

button1 = tk.Button(frame, text="Verify Property", command=open_code_1,bg="#1ABC9C",font=large_font1)
button1.place(x=120,y=140)
button2 = tk.Button(frame, text="List Property", command=open_code_2,bg="#1ABC9C",font=large_font1)
button2.place(x=125,y=220)
button3 = tk.Button(frame, text="Lease Form", command=open_code_3,bg="#1ABC9C",font=large_font1)
button3.place(x=125,y=300)

root.mainloop()
