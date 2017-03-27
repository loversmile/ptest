from Tkinter import *
import string

root = Tk()
frame = Frame(root)
root.title("my")

def discuss():
    error = 0
    try:
        salary = string.atof(e1.get())
    except:
        e1.set("Please Enter Number.")
        error = 1
    try:
        no_duty = string.atof(e2.get())
    except:
        e2.set("Please Enter Number.")
        error = 1
    if error == 1:
        return

    need = salary - no_duty - 3500

    duty = 0.0
    if need <= 1499.999999:
        duty = need * 0.03
        level.set("0.03")
    elif need > 1499.999999 and need <= 4499.999999:
        duty = need * 0.1 - 105
        level.set("0.10")
    elif need > 4499.999999 and need <= 8999.999999:
        duty = need * 0.2 - 555
        level.set("0.20")
    elif need > 8999.999999 and need <= 34999.999999:
        duty = need * 0.25 - 1005
        level.set("0.25")
    elif need > 34999.999999 and need <= 54999.999999:
        duty = need * 0.3 - 2755
        level.set("0.30")
    elif need > 54999.999999 and need <= 79999.999999:
        duty = need * 0.35 - 5505
        level.set("0.35")
    elif need > 79999.999999:
        duty = need * 0.45 - 13505
        level.set("0.45")
    
    e3.set(str(duty))
    leave = salary - no_duty - duty
    e4.set(str(leave))
    
    need_g.set(need)
    label5.pack()
    label6.pack()
    
e1 = StringVar()
e2 = StringVar()
e3 = StringVar()
e4 = StringVar()
ee = StringVar()

level = StringVar()
need_g = StringVar()


entry1 = Entry(root, text = e1)
entry2 = Entry(root, text = e2)
entry3 = Entry(root, text = e3)
entry4 = Entry(root, text = e4)
entrye = Entry(root, text = ee)

#entry2.bind('<Enter>', command=lambda: discuss())

def printkey(event):
    #print('Press  :  ' + event.char)
    discuss()

entry1.bind('<Return>', printkey)
entry2.bind('<Return>', printkey)
entry3.bind('<Return>', printkey)
entry4.bind('<Return>', printkey)

entry1.bind('<Esc>', printkey)
entry2.bind('<Esc>', printkey)
entry3.bind('<Esc>', printkey)
entry4.bind('<Esc>', printkey)

btn = Button(root, text = "OK", command=lambda: discuss(), width = 30)

def bind_event(event):
    print event.char
    discuss()

btn.bind('Return>')
#btn.focus_set()

label1 = Label(root, text = "All Salary")
label2 = Label(root, text = "shebao gongji jin")
label3 = Label(root, text = "duty")
label4 = Label(root, text = "leave")
label5 = Label(root, textvariable = level)
label6 = Label(root, textvariable = need_g)
#btnn = Button(root, textvariable = level, width = 30)


label1.pack()
entry1.pack()
label2.pack()
entry2.pack()
btn.pack()
label3.pack()
entry3.pack()
label4.pack()
entry4.pack()
#label5.pack()

#entrye.pack()

root.resizable(30, 0)
root.mainloop()