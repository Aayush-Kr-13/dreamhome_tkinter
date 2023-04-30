import tkinter as tk
import os

bg="#2C3E50"
textColor = "white"
btnColor = "#5bc0be"

def open_code_1():
    root.destroy()
    os.system("python dreamhome_tkinter\\propertyregisteration.py")

def open_code_2():
    root.destroy()
    os.system("python dreamhome_tkinter\\propertylist.py")
    
def open_code_3():
    root.destroy()
    os.system("python dreamhome_tkinter\\loginpage.py")
    
def open_code_4():
    root.destroy()
    os.system("python dreamhome_tkinter\\checkinterest.py")

def open_code_5():
    root.destroy()
    os.system("python dreamhome_tkinter\\addinterest.py")

root = tk.Tk()
root.title("User Interface")
root.geometry("500x500")
frame = tk.Frame(root, width=500, height=500, bg="#2C3E50")
frame.pack(fill=tk.BOTH, expand=True)

large_font = ('Verdana',30)
large_font1 = ('Verdana', 12)
large_font2 = ('Verdana', 15)

button1 = tk.Button(frame, text="Log Out",fg="red", command=open_code_3)
button1.place(x=10,y=10)

admin_label = tk.Label(frame, text="Welcome User!",bg="#2C3E50",fg="Orange",font=large_font)
admin_label.place(x=80,y=45)

register_label = tk.Label(frame, text="Register property?",bg=bg,fg=textColor,font=large_font2)
register_label.place(x=30,y=160)

button1 = tk.Button(frame, text="Register Property", command=open_code_1,font=large_font1,bg="#5bc0be")
button1.place(x=40, y=220)

search_label = tk.Label(frame, text="Want to search?",bg=bg,fg=textColor,font=large_font2)
search_label.place(x=285,y=160)

button2 = tk.Button(frame, text="Search For Property", command=open_code_2,font=large_font1,bg="#5bc0be")
button2.place(x=285,y=220)

check_label = tk.Label(frame, text="Check for interest?",bg=bg,fg=textColor,font=large_font2)
check_label.place(x=30,y=330)

button3 = tk.Button(frame, text="Check For Interest", command=open_code_4,font=large_font1,bg="#5bc0be")
button3.place(x=45,y=390)

new_label = tk.Label(frame, text="Have a intrest?",bg=bg,fg=textColor,font=large_font2)
new_label.place(x=290,y=330)

button4 = tk.Button(frame, text="Add Interest", command=open_code_5,font=large_font1,bg="#5bc0be")
button4.place(x=315,y=390)

root.mainloop()
