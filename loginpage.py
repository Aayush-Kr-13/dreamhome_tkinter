import tkinter as tk
import os

bg="#2C3E50"
textColor = "white"
btnColor = "#5bc0be"

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
root.geometry("500x500")
frame = tk.Frame(root, width=500, height=500, bg=bg)
frame.pack(fill=tk.BOTH, expand=True)

large_font = ('Verdana', 40)
large_font1 = ('Verdana', 12)
large_font2 = ('Verdana', 15)
large_font3 = ('Arial', 10,'italic')

motto_label = tk.Label(frame, text=" find your home away from home",bg=bg,fg=textColor,font=large_font3)
motto_label.place(x=150,y=105)

login_label = tk.Label(frame, text="DreamHome",bg=bg,fg="orange",font=large_font)
login_label.place(x=70,y=35)

user_label = tk.Label(frame, text="Already a user?",bg=bg,fg=textColor,font=large_font2)
user_label.place(x=40,y=160)

button1 = tk.Button(frame, text="User Login",bg=btnColor,fg="black", command=open_code_1,font=large_font1)
button1.place(x=60,y=225)

staff_label = tk.Label(frame, text="Are you staff?",bg=bg,fg=textColor,font=large_font2)
staff_label.place(x=300,y=160)

button2 = tk.Button(frame, text="Staff Login",bg=btnColor,fg="black", command=open_code_2,font=large_font1)
button2.place(x=315,y=225)

admin_label = tk.Label(frame, text="Are you admin?",bg=bg,fg=textColor,font=large_font2)
admin_label.place(x=40,y=325)

button3 = tk.Button(frame, text="Admin Login",bg=btnColor,fg="black", command=open_code_3,font=large_font1)
button3.place(x=60,y=385)

new_label = tk.Label(frame, text="Are you new user?",bg=bg,fg=textColor,font=large_font2)
new_label.place(x=290,y=325)

button4 = tk.Button(frame, text="User Registeration",bg=btnColor,fg="black", command=open_code_4,font=large_font1)
button4.place(x=305,y=385)

root.mainloop()
