from tkinter import *
from tkinter import ttk


def callback(num):
    furm = display.get() + num
    display.set(furm)

def calculate():
    try:
        furm = display.get()
        res = eval(furm)
        display.set(furm + "=" + str(res))
    except:
        display.set("Error!")

def clear():
    display.set("")

root = Tk()
frame = Frame(root)
root.title("计算器")

display = StringVar()
lbl = Label(root, relief="sunken", borderwidth=3, anchor=SE)
lbl.configure(background="white",height=2, width=25)
lbl['textvariable'] = display
lbl.grid(row=0, column=0, columnspan=4, sticky=SE)
lbl.bind('<Button-1>', display.set(''))

ttk.Button(root, text="7", width=5, command=lambda: callback("7")).grid(row=3, column=0)
ttk.Button(root, text="8", width=5, command=lambda: callback("8")).grid(row=3, column=1)
ttk.Button(root, text="9", width=5, command=lambda: callback("9")).grid(row=3, column=2)
ttk.Button(root, text="+", width=5, command=lambda: callback("+")).grid(row=3, column=3)
ttk.Button(root, text="4", width=5, command=lambda: callback("4")).grid(row=4, column=0)
ttk.Button(root, text="5", width=5, command=lambda: callback("5")).grid(row=4, column=1)
ttk.Button(root, text="6", width=5, command=lambda: callback("6")).grid(row=4, column=2)
ttk.Button(root, text="-", width=5, command=lambda: callback("-")).grid(row=4, column=3)
ttk.Button(root, text="1", width=5, command=lambda: callback("1")).grid(row=5, column=0)
ttk.Button(root, text="2", width=5, command=lambda: callback("2")).grid(row=5, column=1)
ttk.Button(root, text="3", width=5, command=lambda: callback("3")).grid(row=5, column=2)
ttk.Button(root, text="*", width=5, command=lambda: callback("*")).grid(row=5, column=3)
ttk.Button(root, text="0", width=5, command=lambda: callback("0")).grid(row=6, column=0)
ttk.Button(root, text=".", width=5, command=lambda: callback(".")).grid(row=6, column=1)
ttk.Button(root, text="%", width=5, command=lambda: callback("%")).grid(row=6, column=2)
ttk.Button(root, text="/", width=5, command=lambda: callback("/")).grid(row=6, column=3)
ttk.Button(root, text="clear", command=lambda:clear()).grid(row=7, column=0, columnspan=2)
ttk.Button(root, text="=", command=lambda: calculate()).grid(row=7, column=2, columnspan=2)

root.resizable(0, 0)
root.mainloop()