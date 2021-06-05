# IMPORTING TKINTER
from tkinter import *
from tkinter import messagebox

# WINDOW FEATURES
window = Tk()
window.title("Exception Handling")
window.geometry("500x250")
window.config(bg="#0F164A")
window.resizable(0, 0)

# DEFINING FUNCTIONS
def qualification():
    try:
        money = float(amount.get())
        if money < 3000:
            messagebox.showerror("Insufficient funds, Please deposit more funds for this excursion.")
            amount.delete(0, END)
        else:
            messagebox.showinfo("Accepted", "CONGRATULATIONS!!! You qualify to go to Malaysia.")
            amount.delete(0, END)
    except ValueError:
        messagebox.showerror("Invalid input", "Please insert the amount in digits.")
        amount.delete(0, END)

def clear():
    amount.delete(0, END)

def exit():
    window.destroy()

# HEADING
label = Label(window, text="  Please enter your amount of funds : ", bg="#FFEC1C")
label.place(x=120, y=30)

# ENTRY
amount = Entry(window)
amount.place(x=120, y=70, width=250)

# BUTTON
btn1 = Button(window, text="Check qualification", borderwidth="8", bg="#FFEC1C", command=qualification)
btn1.place(x=120, y=110, width=250)

btn2 = Button(window, text="Clear", borderwidth="5", bg="#FFEC1C", command=clear)
btn2.place(x=120, y=170, width=115)

btn3 = Button(window, text="Exit", borderwidth="5", bg="#FFEC1C", command=exit)
btn3.place(x=250, y=170, width=115)

window.mainloop()
