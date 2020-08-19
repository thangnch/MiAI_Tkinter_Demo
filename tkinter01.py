from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import tkinter

window = Tk()
window.title("Mì AI Form")
window.geometry("800x600")

# Thêm label
lbl = tkinter.Label(window, text="Hello Mì AI", fg="red", font=("Arial", 50))
lbl.grid(column=0, row=0)

# Thêm textbox
txt = Entry(window, width=20)
txt.grid(column=0, row=1)

def handleButton():
    lbl.configure(text = "Hi," + txt.get())
    return

# Thêm button
btnHello = Button(window, text="Say Hello", command=handleButton)
btnHello.grid(column=1, row=1)

# Thêm combobox

combo = Combobox(window)
combo['values'] = ("Bạn 1", "Bạn 2", "Bạn 3")
combo.current(0)
combo.grid(column=0, row=2 )


def handleButton1():
    #lbl.configure(text = "Hi," + combo.get())
    messagebox.showinfo("Mì AI Test", "Hi," + combo.get())
    return

# Thêm button
btnHello1 = Button(window, text="Say Hello Combo", command=handleButton1)
btnHello1.grid(column=1, row=2)


window.mainloop()
