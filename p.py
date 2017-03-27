

from tkinter import * 
root = Tk()

li     = ['C','python','php','html','SQL','java']
movie  = ['CSS','jQuery','Bootstrap']
listb  = Listbox(root)
listb2 = Listbox(root)

def helloButton():
    print ("HEEEEEEEE!|\n")

button1 = Button(root,text = 'Hello Button',command = helloButton)
button2 = Button(root, text = "Second", relief = RAISED,  bd = 4)
for item in li:
    listb.insert(0,item)

for item in movie:
    listb2.insert(0,item)
#listb.insert(0, button1)

label = Label(root,text = "I am here for tk!", fg = 'red',bg = '#0000FF', width=30, height=2)

#bm = PhotoImage(file = 'E:\\ptest\\th.jpg')
#label2 = Label(root,image = bm)
#label2.bm = bm

listb.pack()
button2.pack()
listb2.pack()
button1.pack()

label.pack()
#label2.pack()

entry1 = Entry(root,text = 'input your text here')
entry1.pack()

def changeText():
    if b['text'] == 'text':
        v.set('change')
        print ('change')
    else:
        v.set('text')
        print ('text')
v = StringVar()
b = Button(root,textvariable = v,command = changeText)
v.set('text')
b.pack()


e = StringVar()
def validateText(contents):
    print (contents)
    return contents.isalnum()

entry = Entry(root,validate = 'key',textvariable = e,validatecommand = validateText)
entry.pack()


root.mainloop()