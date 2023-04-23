import tkinter as tk
import os

def open_code_1():
    root.destroy()
    os.system("python propertyregisteration.py")

def open_code_2():
    root.destroy()
    os.system("python propertylist.py")
    
def open_code_3():
    root.destroy()
    os.system("python loginpage.py")
    
def open_code_4():
    root.destroy()
    os.system("python checkinterest.py")

def open_code_5():
    root.destroy()
    os.system("python dreamhome_tkinter\\addinterest.py")

root = tk.Tk()
root.title("Interface")
root.geometry("400x400")
frame = tk.Frame(root, width=400, height=400, bg="#2C3E50")
frame.pack(fill=tk.BOTH, expand=True)

large_font = ('Verdana', 20)
large_font1 = ('Verdana', 12)

button1 = tk.Button(frame, text="Log Out",fg="red", command=open_code_3)
button1.place(x=10,y=10)

admin_label = tk.Label(frame, text="Welcome User!",bg="#2C3E50",fg="Orange",font=large_font)
admin_label.place(x=80,y=45)

button1 = tk.Button(frame, text="Register Property", command=open_code_1,font=large_font1,bg="#1ABC9C")
button1.place(x=105, y=130)
button2 = tk.Button(frame, text="Search For Property", command=open_code_2,font=large_font1,bg="#1ABC9C")
button2.place(x=95,y=200)
button3 = tk.Button(frame, text="Check For Interest", command=open_code_4,font=large_font1,bg="#1ABC9C")
button3.place(x=95,y=280)
button4 = tk.Button(frame, text="Add Interest", command=open_code_5,font=large_font1,bg="#1ABC9C")
button4.place(x=115,y=360)

root.mainloop()
