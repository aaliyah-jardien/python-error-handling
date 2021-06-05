# IMPORTING TKINTER
from tkinter import *
from tkinter import messagebox

# WINDOW FEATURES
window = Tk()
window.title("Authentication")
window.geometry("500x500")
window.resizable(0, 0)

# DEFINING FUNCTIONS
usernames = ["Aaliyah", "Thabo", "Uthmaan", "Zoe"]
password = ["1111", "2222", "3333", "4444"]

found = False

def participant():

    for x in range(len(password)):
        if name_entry.get() == usernames[x] and password_entry.get() == password[x]:
            found = True
    if found == True:
        messagebox.showinfo(title="Status", message="Access Granted!")
        window.destroy()
        import other
    else:
        messagebox.showerror(title="Error", message="Access Denied!")
        window.destroy()

def clear_btn():
    name_entry.delete(0, END)
    password_entry.delete(0, END)

def exit_btn():
    return window.destroy()

# FRAME
my_frame = Frame(window, bg="#0F164A")
my_frame.place(x=0, y=0, width=500, height=500)

# IMAGE
img = PhotoImage(file="malaysia(1).png")
canvas = Canvas(window, width=400, height=200)
canvas.create_image(0, 0, anchor=NW, image=img)
canvas.place(x=50, y=270)

# LABELS
Label_text = StringVar()

head_lab = Label(window, text="Please enter your login details", bg="#FFEC1C")
head_lab.place(x=150, y=25)

lab_1 = Label(window, text=" Username : ", bg="#FFEC1C")
lab_1.place(x=90, y=80)

lab_2 = Label(window, text=" Password :  ", bg="#FFEC1C")
lab_2.place(x=90, y=130)

# ENTRIES
name_entry = Entry(window)
name_entry.place(x=210, y=80)

password_entry = Entry(window, show="*")
password_entry.place(x=210, y=130)

# BUTTONS
btn_1 = Button(window, text="Login", command=participant, borderwidth="8", bg="#FFEC1C")
btn_1.place(x=90, y=200)

btn_2 = Button(window, text="Clear", command=clear_btn, borderwidth="8", bg="#FFEC1C")
btn_2.place(x=200, y=200)

btn_3 = Button(window, text="Exit", command=exit_btn, borderwidth="8", bg="#FFEC1C")
btn_3.place(x=310, y=200)

window.mainloop()
