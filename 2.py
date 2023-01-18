from tkinter import *

win = Tk()
win.geometry("350x75")

var = IntVar()
var.set(0)

fr_left = Frame()
fr_right = Frame()

def inf(f):
    if f == 1:
        lable["text"] = "Валентин с балкона \n уронил рояль, \n Грустно для Олега \n кончился февраль."
    elif f == 2:
        lable["text"] = "Просто челик"
    elif f == 3:
        lable["text"] = "Расписание утра \n 9:00 - Проснуться \n 9:10 - Поесть \n 10:00 - Пойти в школу"

but1 = Radiobutton( fr_left,bg="gray", text="Олег",width=25, indicatoron=0, command=lambda f = 1: inf(1), variable=var, value=1)
but2 = Radiobutton(fr_left,bg="gray", text="Максим",width=25, indicatoron=0, command=lambda f = 2: inf(2), variable=var, value=3)
but3 = Radiobutton(fr_left,bg="gray", text="Алиса",width=25, indicatoron=0, command=lambda f = 3: inf(3), variable=var, value=2)
lable = Label(fr_right,text="Тут будет инфа", height=150,width=25)


fr_left.pack(side=LEFT)
but1.pack(anchor=W)
but2.pack(anchor=W)
but3.pack(anchor=W)

fr_right.pack(side=LEFT)
lable.pack()


win.mainloop()