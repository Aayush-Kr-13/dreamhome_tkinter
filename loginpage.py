import tkinter as tk
import os

def open_code_1():
    root.destroy()
    os.system("python dreamhome_tkinter\\userlogin.py")

def open_code_2():
    root.destroy()
    os.system("python dreamhome_tkinter\\stafflogin.py")
    
def open_code_3():
    root.destroy()
    os.system("python dreamhome_tkinter\\adminlogin.py")
    
def open_code_4():
    root.destroy()
    os.system("python dreamhome_tkinter\\clientregisteration.py")

root = tk.Tk()
root.title("Main Page")
root.geometry("400x400")
frame = tk.Frame(root, width=350, height=500, bg="#2C3E50")
frame.pack(fill=tk.BOTH, expand=True)

large_font = ('Verdana', 25)
large_font1 = ('Verdana', 12)

login_label = tk.Label(frame, text="Dreamhome",bg="#2C3E50",fg="Orange",font=large_font)
login_label.place(x=100,y=35)

button1 = tk.Button(frame, text="User Login", command=open_code_1,font=large_font1)
button1.place(x=50,y=155)
button2 = tk.Button(frame, text="Staff Login", command=open_code_2,font=large_font1)
button2.place(x=245,y=155)
button3 = tk.Button(frame, text="Admin Login", command=open_code_3,font=large_font1)
button3.place(x=40,y=275)
button4 = tk.Button(frame, text="User Registeration", command=open_code_4,font=large_font1)
button4.place(x=215,y=275)


root.mainloop()
