from tkinter import Entry , Label ,Tk ,mainloop ,END
from random import choice
from time import sleep
from threading import Thread
from os import _exit


color = None
colors = ['red', 'black', 'yellow', 'pink', 'blue', 'green',"purple",'orange','white','brown']
win = Tk()
win.title('Color Game')
win['bg'] = '#527a7a'
win.resizable(False, False)
Label(win,fg='#ff0000',text='🖌  ',font=(("Dancing Script", 17, 'bold')),bg='#527a7a').grid(row=0,column=0)
Label(win,fg='#0033cc',text='Type ',font=(("Dancing Script", 17, 'bold')),bg='#527a7a').grid(row=0,column=1)
Label(win,fg='#660033',text='the ',font=(("Dancing Script", 17, 'bold')),bg='#527a7a').grid(row=0,column=2)
Label(win,fg='#00cc00',text='color ',font=(("Dancing Script", 17, 'bold')),bg='#527a7a').grid(row=0,column=3)
Label(win,fg='#662200',text='of ',font=(("Dancing Script", 17, 'bold')),bg='#527a7a').grid(row=0,column=4)
Label(win,fg='#e6e600',text='word ',font=(("Dancing Script", 17, 'bold')),bg='#527a7a').grid(row=0,column=5)
Label(win,fg='#400080',text='not ',font=(("Dancing Script", 17, 'bold')),bg='#527a7a').grid(row=0,column=6)
Label(win,fg='#663300',text='word ',font=(("Dancing Script", 17, 'bold')),bg='#527a7a').grid(row=0,column=7)
Label(win,fg='#ff66cc',text='text',font=(("Dancing Script", 17, 'bold')),bg='#527a7a').grid(row=0,column=8)
Label(win,fg='#00ffff',text='  🖌',font=(("Dancing Script", 17, 'bold')),bg='#527a7a').grid(row=0,column=9)

Label(win,bg='#527a7a',font=(("Times", 15, 'bold'))).grid(row=6)
timer = Label(win, text='time : 60', font=(("Times", 20, 'bold')),bg='#527a7a')
timer.grid(row=2,columnspan=10)
type_range = Entry(win,font=(("Times", 30, 'bold')),bg='pink',justify='center')
type_range.grid(row=4,columnspan=10)
word = Label(win)
word.grid(row=3,columnspan=10)


def next_word():
    global color , word
    text = choice(colors)
    color = choice(colors)
    if text == color:
        next_word()
    else:
        if color == 'brown':
            word.config(text=text,fg='#4d1300', font=(("Times", 60, 'bold')),bg='#527a7a')
        elif color == 'orange':
            word.config(text=text,fg='#ff3300', font=(("Times", 60, 'bold')),bg='#527a7a')
        elif color == 'pink':
            word.config(text=text,fg='#ff00bf', font=(("Times", 60, 'bold')),bg='#527a7a')
        elif color == 'purple':
            word.config(text=text,fg='#660066', font=(("Times", 60, 'bold')),bg='#527a7a')
        elif color == 'green':
            word.config(text=text,fg='#00cc00', font=(("Times", 60, 'bold')),bg='#527a7a')
        else:
            word.config(text=text,fg=color, font=(("Times", 60, 'bold')),bg='#527a7a')
        word.grid(row=3)


def Get_word():
    score = 0
    global color
    while True:
        sleep(0.01)  # Avoid from crush
        word_list = list(type_range.get())
        if len(word_list) != 0:
            if word_list[-1] == ' ':
                type_range.delete(0, END)
                if color + ' ' == "".join(word_list):
                    score += 1
                    scoreup(score)
                next_word()


def scoreup(score):
    show_score = Label(win, text='score = ' + str(score),font=(("Times", 20, 'bold')),bg='#527a7a')
    show_score.grid(row=1,columnspan=10)


def Timer():
    while True:
        sleep(0.01)  # Avoid from crush
        if type_range.get() != "":
            for time in range(59, -1, -1):
                timer.config(text="time : " + str(time),font=(("Times", 20, 'bold')),bg='#527a7a')
                timer.grid(row=2,columnspan=10)
                sleep(1)
            Exit()


def Exit():
    _exit(0)

def start():
    scoreup(0)
    next_word()
    Thread(target=Get_word).start()
    Thread(target=Timer).start()
    win.bind('<Return>', lambda e:type_range.insert(len(type_range.get()),' '))
    win.protocol("WM_DELETE_WINDOW", Exit)


start()
win.mainloop()
