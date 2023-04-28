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
    os.system("python staffregisteration.py")
    
def open_code_5():
    root.destroy()
    os.system("python loginpage.py")

def open_code_6():
    root.destroy()
    os.system("python bookinglist.py")    

root = tk.Tk()
root.title("Admin Interface")
root.geometry("400x400")
frame = tk.Frame(root, width=400, height=400, bg="#2C3E50")
frame.pack(fill=tk.BOTH, expand=True)

button1 = tk.Button(frame, text="Log Out",fg="red", command=open_code_5)
button1.place(x=10,y=10)

large_font = ('Verdana', 30)
large_font1 = ('Verdana', 10)

admin_label = tk.Label(frame, text="Welcome Admin!",bg="#2C3E50",fg="Orange",font=large_font)
admin_label.place(x=35,y=55)

button1 = tk.Button(frame, text="Add Branch", command=open_code_1,font=large_font1)
button1.place(x=50,y=180)
button2 = tk.Button(frame, text="List Property", command=open_code_2,font=large_font1)
button2.place(x=260,y=180)
button3 = tk.Button(frame, text="List Branch", command=open_code_3,font=large_font1)
button3.place(x=50,y=320)
button4 = tk.Button(frame, text="Register Staff", command=open_code_4,font=large_font1)
button4.place(x=260,y=320)
button5 = tk.Button(frame, text="Bookings", command=open_code_6,font=large_font1)
button5.place(x=155,y=250)


root.mainloop()
