import tkinter as tk
import os

bg="#2C3E50"
textColor = "white"
btnColor = "#5bc0be"

def open_code_1():
    root.destroy()
    os.system("python dreamhome_tkinter//addbranch.py")

def open_code_2():
    root.destroy()
    os.system("python dreamhome_tkinter//propertylista.py")
    
def open_code_3():
    root.destroy()
    os.system("python dreamhome_tkinter//branchlist.py")
    
def open_code_4():
    root.destroy()
    os.system("python dreamhome_tkinter//staffregisteration.py")
    
def open_code_5():
    root.destroy()
    os.system("python dreamhome_tkinter//loginpage.py")

def open_code_6():
    root.destroy()
    os.system("python dreamhome_tkinter//bookinglist.py")    

root = tk.Tk()
root.title("Admin Interface")
root.geometry("500x500")
frame = tk.Frame(root, width=500, height=500, bg="#2C3E50")
frame.pack(fill=tk.BOTH, expand=True)

button1 = tk.Button(frame, text="Log Out",fg="red", command=open_code_5)
button1.place(x=10,y=10)

large_font = ('Verdana', 35)
large_font1 = ('Verdana', 13)

admin_label = tk.Label(frame, text="Welcome Admin!",bg="#2C3E50",fg="Orange",font=large_font)
admin_label.place(x=45,y=65)


button1 = tk.Button(frame, text="Add Branch", command=open_code_1,font=large_font1,bg="#5bc0be")
button1.place(x=60,y=200)

button2 = tk.Button(frame, text="List Property", command=open_code_2,font=large_font1,bg="#5bc0be")
button2.place(x=290,y=200)
button3 = tk.Button(frame, text="List Branch", command=open_code_3,font=large_font1,bg="#5bc0be")
button3.place(x=60,y=390)
button4 = tk.Button(frame, text="Register Staff", command=open_code_4,font=large_font1,bg="#5bc0be")
button4.place(x=290,y=390)
button5 = tk.Button(frame, text="Bookings", command=open_code_6,font=large_font1,bg="#5bc0be")
button5.place(x=185,y=295)


root.mainloop()
