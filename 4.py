from tkinter import *
import calendar
import datetime

def rs():
    win = Tk()
    win.title('Расписание')
    win.geometry("500x300")

    fr_top = Frame(win)
    fr_bot = Frame(win)

    lb1 = Label(fr_top , text='День', width=10, height=2, justify="left", bg= 'lightgray')
    lb2 = Label(fr_top , text='Событие', width=60, height=2, justify="left", bg= 'lightgray')
    lb3 = Label(fr_bot, text='День', width=10, height=2, justify="left", bg= 'lightgray')
    lb4 = Label(fr_bot, text='Событие', width=60, height=2, justify="left", bg= 'lightgray')

    with open('buf.txt', "r", encoding="utf-8") as file:
        lb = file.read().split(",")
        v = lb[3].split("\n")
        lb3["text"] = str(lb[0])
        lb4["text"] = ''.join(v)
    fr_top.pack()
    lb1.pack(side=LEFT)
    lb2.pack(side=LEFT)
    fr_bot.pack()
    lb3.pack(side=LEFT)
    lb4.pack(side=LEFT)

def zam():
    win = Tk()
    win.title('Создание заметки')


    def sz(event):
        z = [ent1.get(),ent2.get(),ent3.get(), text.get(1.0, END)]
        file = open('buf.txt', "w+", encoding="utf-8")
        for i in range(len(z)):
            fl = "".join(z[i])
            file.write(fl + ",")
        file.close()
        win.destroy()

    def ot(event):
        win.destroy()

    fr_top = Frame(win)
    fr_midle = Frame(win)
    fr_bot = Frame(win)

    lb1 = Label(fr_top, text='День', width=15, justify = "center")
    lb2 = Label(fr_top, text='Месяц', width=15, justify = "center")
    lb3 = Label(fr_top, text='Год', width=15, justify = "center")

    ent1 = Entry(fr_midle, width=15, justify = "center", bg= 'lightgray')
    ent2 = Entry(fr_midle, width=15, justify = "center", bg= 'lightgray')
    ent3 = Entry(fr_midle, width=15, justify = "center", bg= 'lightgray')
    text = Text(fr_midle,width=36, height=8, bg= 'lightgray')

    but_sz = Button(fr_bot,text="Создать", width=15, height=2)
    but_ot = Button(fr_bot,text="Отмена", width=15, height=2)

    but_sz.bind("<Button-1>", sz)
    but_ot.bind("<Button-1>",ot)

    fr_top.pack()
    lb1.pack(side=LEFT)
    lb2.pack(side=LEFT)
    lb3.pack(side=LEFT)

    fr_midle.pack()
    text.pack(side=BOTTOM, padx = 2)
    ent1.pack(side=LEFT, padx = 2)
    ent2.pack(side=LEFT, padx = 2)
    ent3.pack(side=LEFT, padx = 2)

    fr_bot.pack()
    but_sz.pack(side=LEFT)
    but_ot.pack(side=LEFT)
def ob():
    root.destroy()

def ex():
    exit()

def prew():
    global month, year
    month -= 1
    if month == 0:
        month = 12
        year -= 1
    fill()
def next():
    global month, year
    month += 1
    if month == 13:
        month = 1
        year += 1
    fill()

def fill():
    info_label['text'] = calendar.month_name[month] + ', '+ str(year)
    month_days = calendar.monthrange(year, month)[1]
    with open('buf.txt', "r", encoding="utf-8") as file:
        lb = file.read().split(",")
        z = lb[:-1]
        v = lb[3].split("\n")
    if month == 1:
        prew_month_days = calendar.monthrange(year-1, 12)[1]
    else:
        prew_month_days = calendar.monthrange(year, month - 1)[1]
    week_day = calendar.monthrange(year, month)[0]
    for n in range(month_days):
        days[n + week_day]['text'] = n + 1
        days[n + week_day]['fg'] = "black"
        if (n + 1 == int(z[0]) and year == int(z[2]) and month == int(z[1])):
            days[n + week_day]['fg'] = "blue"
        if year == now.year and month == now.month and n == now.day:
            days[n + week_day]['background'] = 'green'
        else:
            days[n + week_day]['background'] = 'lightgray'
        for n in range(week_day):
            days[week_day - n - 1]['text'] = prew_month_days - n
            days[week_day - n - 1]['fg'] = 'gray'
            days[week_day - n - 1]['background'] =  "#f3f3f3"
        for n in range(6 * 7 - month_days - week_day):
            days[week_day + month_days + n]['text'] = n + 1
            days[week_day + month_days + n]['fg'] = 'gray'
            days[week_day + month_days + n]['background'] = '#f3f3f3'

while True :
    root = Tk()
    root.title('Calendar')
    days = []
    now = datetime.datetime.now()
    year = now.year
    month = now.month

    prew_button = Button(root, text="<", command=prew)
    prew_button.grid(row=0, column=0, sticky='nsew')
    next_button = Button(root, text='>', command=next)
    next_button.grid(row=0, column=6, sticky='nsew')
    info_label = Label(root, text='8', width=1, height=1,
                                font=('Verdana', 16, 'bold'), fg='blue')
    info_label.grid(row=0, column=1, columnspan=5, sticky='nsew')

    but=Button(root,text="Создать заметку", command=zam, width=15, height=2)
    but.grid(row=10, column=2, sticky='nsew')
    but = Button(root, text="Обновить", command=ob, width=15, height=2)
    but.grid(row=10, column=3, sticky='nsew')
    but = Button(root, text="Расписание", command=rs, width=15, height=2)
    but.grid(row=10, column=4, sticky='nsew')
    but = Button(root, text="Закрыть", command=ex, width=15, height=2)
    but.grid(row=10, column=6, sticky='nsew')

    for n in range(7):
        lbl = Label(root, text=calendar.day_abbr[n], width=6, height=1,
                font=('Verdana', 10, 'normal'), fg='darkblue')
        lbl.grid(row=1, column=n, sticky='nsew')
    for row in range(6):
        for col in range(7):
            lbl = Label(root, text='0', width=6, height=2,
                    font=('Verdana', 16, 'bold'))
            lbl.grid(row=row+2, column=col, sticky='nsew')
            days.append(lbl)

    fill()
    root.mainloop()