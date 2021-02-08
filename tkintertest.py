from tkinter import *
root = Tk()
e = Entry(root, width = 50)
e.grid(column = 0,row = 0)
x = 0
y = 0
def getter():
    global x
    x = str(e.get())
def close():
    root.quit()
var = BooleanVar()

chk = Checkbutton(root, text='foo', variable=var)
chk.grid(column = 1, row = 0)

lul = Label(root, text = 'Beans')
lul.grid(column =0,row =1)

des = Button(root, text ='Close', command = close )
des.grid(column = 0,row = 3)


# def stater()
#     if var.get():
#         sstate = NORMAL
#     else:
#         sstate = DISABLED
#     return sstate


s = Scale(root, from_ =500, to = 1500, orient = HORIZONTAL)
s.grid(column = 0, row = 2)
x = s.get()

root.mainloop()
print(x)
print("Hello World!")