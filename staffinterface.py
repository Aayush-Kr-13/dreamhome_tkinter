import tkinter as tk
import os

btnColor = "#5bc0be"

def open_code_1():
    root.destroy()
    os.system("python dreamhome_tkinter\\propertyverifier.py")

def open_code_2():
    root.destroy()
    os.system("python dreamhome_tkinter\\propertylists.py")
    
def open_code_3():
    root.destroy()
    os.system("python dreamhome_tkinter\\leaseform.py")

def open_code_4():
    root.destroy()
    os.system("python dreamhome_tkinter\\loginpage.py")  

root = tk.Tk()
root.title("Staff Interface")
root.geometry("400x400")
frame = tk.Frame(root, width=400, height=400, bg="#2C3E50")
frame.pack(fill=tk.BOTH, expand=True)

large_font = ('Verdana', 30)
large_font1 = ('Verdana', 12)

staff_label = tk.Label(frame, text="Welcome Staff!",bg="#2C3E50",fg="Orange",font=large_font)
staff_label.place(x=50,y=55)

button1 = tk.Button(frame, text="Log Out",fg="red", command=open_code_4,font=large_font1)
button1.place(x=10,y=10)

button1 = tk.Button(frame, text="Verify Property", command=open_code_1,bg=btnColor,fg="black",font=large_font1)
button1.place(x=130,y=160)
button2 = tk.Button(frame, text="List Property", command=open_code_2,bg=btnColor,fg="black",font=large_font1)
button2.place(x=135,y=240)
button3 = tk.Button(frame, text="Lease Form", command=open_code_3,bg=btnColor,fg="black",font=large_font1)
button3.place(x=140,y=330)

root.mainloop()
