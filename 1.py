from tkinter import *

def insert_txt(event):
    name = str(ent1.get()) + ".txt"
    with open(name, "r", encoding="utf-8") as file:
        lb = file.read()
        text.insert(1.0, lb)
def get_txt(event):
    name = str(ent1.get()) + ".txt"
    lb = text.get(1.0, END)
    with open(name, "w", encoding="utf-8") as file:
        file.write(lb)
def close(event):
    win.quit()

win = Tk()
win.geometry("350x395")

fr_top = Frame()
fr_bot = Frame()
fr_midle = Frame()

ent1 = Entry(fr_top, width=25, bg = 'gray')
but1 = Button(fr_top, text="Открыть",width=10)
but2 = Button(fr_top, text="Сохранить",width=10)
but3 = Button(fr_bot, text="Закрыть",width=100)

but1.bind("<Button-1>",insert_txt)
but2.bind("<Button-1>",get_txt)
but3.bind("<Button-1>",close)

#Вывод фреймов
fr_top.pack()
fr_midle.pack()
fr_bot.pack()

# Конструкция fr_top
ent1.pack(side=LEFT, padx = 2)
but1.pack(side=LEFT, padx = 2)
but2.pack(side=LEFT, padx = 2)

# Конструкция fr_bot
text = Text(fr_midle, width=40, height=20, wrap=NONE)
text.pack(side=LEFT)
#Ползунки
scroll1 = Scrollbar(fr_midle, command=text.yview)
scroll2 = Scrollbar(fr_bot,orient=HORIZONTAL, command=text.xview)
#Функция и расположение ползунков
scroll1.pack(side=LEFT, fill=Y)
text.config(yscrollcommand=scroll1.set)
scroll2.pack(side=TOP, fill=X)
but3.pack(side=BOTTOM, padx = 2)
text.config(xscrollcommand=scroll2.set)

win.mainloop()