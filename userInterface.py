import tkinter as tk
import os

def open_code_1():
    root.destroy()
    os.system("python dreamhome_tkinter\\propertyregisteration.py")

def open_code_2():
    root.destroy()
    os.system("python dreamhome_tkinter\\propertylist.py")
    
def open_code_3():
    root.destroy()
    os.system("python dreamhome_tkinter\\loginpage.py")

root = tk.Tk()
root.title("Interface")
root.geometry("350x350")
frame = tk.Frame(root, width=350, height=350, bg="#2C3E50")
frame.pack(fill=tk.BOTH, expand=True)

large_font = ('Verdana', 30)
large_font1 = ('Verdana', 12)

button1 = tk.Button(frame, text="Log Out",fg="red", command=open_code_3)
button1.place(x=10,y=10)

admin_label = tk.Label(frame, text="Welcome User!",bg="#2C3E50",fg="Orange",font=large_font)
admin_label.place(x=25,y=45)

button1 = tk.Button(frame, text="Register Property", command=open_code_1,font=large_font1)
button1.place(x=90, y=140)
button2 = tk.Button(frame, text="Search For Property", command=open_code_2,font=large_font1)
button2.place(x=85,y=260)


root.mainloop()
