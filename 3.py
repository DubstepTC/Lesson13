from tkinter import *

win = Tk()
win.geometry("446x200")
lb = []
lb2 = []
# Первый список связан с файлом "Покупки.txt", который можно создать с помощью задания 1
# Функция заполняет первый список
def inf():
    for i in open("Покупки.txt"):
        lb.append(i[:])
    for i in (lb):
        sp1.insert(0, i)
#Обмен данными между списками
def swap(event,f):
    if f == 1 :
        select = list(sp1.curselection())
        select.reverse()
        print(select)
        for i in select:
            sp2.insert(0, sp1.get(i))
            sp1.delete(i)
    elif f == 2 :
        select = list(sp2.curselection())
        select.reverse()
        print(select)
        for i in select:
            sp1.insert(0, sp2.get(i))
            sp2.delete(i)

fr_left = Frame()
fr_midle = Frame()
fr_right = Frame()


sp1 = Listbox(fr_left, bg = "#d7d7d7", selectmode=EXTENDED, width = 25)
scroll1 = Scrollbar(command=sp1.yview)
sp2 = Listbox(fr_right, bg = "#d7d7d7", selectmode=EXTENDED, width = 25)
scroll2 = Scrollbar(command=sp2.yview)
but1 = Button(fr_midle, bg = "#d7d7d7", text='>>', width = 10)
but2 = Button(fr_midle, bg = "#d7d7d7", text='<<', width = 10)

but1.bind("<Button-1>", lambda event, f = 1 : swap(event, f))
but2.bind("<Button-1>", lambda event, f = 2 : swap(event, f))

inf()

fr_left.pack(side=LEFT, padx = 3)
sp1.pack(side=LEFT)
scroll1.pack(side=LEFT, fill=Y)
fr_midle.pack(side=LEFT, padx = 3)
but1.pack()
but2.pack(side=BOTTOM)
fr_right.pack(side=LEFT, padx = 3)
sp2.pack(side=LEFT)
scroll2.pack(side=LEFT, fill=Y)

win.mainloop()