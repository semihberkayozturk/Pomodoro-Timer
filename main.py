from tkinter import *
import math
#-------CONSTANTS-----------
DARK = "#141E27"
FONT_NAME = "Courier"
WHITE = "#F7F7F7"
GREEN = "#357C3C"
BLUE = "#084594"
YELLOW = "#FFD32D"
WORK_MIN = 25
SHORT_BREAK = 5
LONG_BREAK = 20
reps = 0
timer = None
#-----------------------TIMER RESET--------------------
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0
#-----------------------TIMER MECHANISM-----------------
def start_timer():
    global reps 
    reps += 1

    work_sec = WORK_MIN*60
    short_break = SHORT_BREAK*60
    long_break = LONG_BREAK*60

    if reps % 8 == 0:
        count_down(long_break)
        title_label.config(text="Long Break",fg=BLUE)
    if reps % 2 == 0:
        count_down(short_break)
        title_label.config(text="Short Break",fg=YELLOW)
    else:
        count_down(work_sec)
        title_label.config(text="Work",fg=WHITE)

#-----------------------COUNTDOWN MECHANISM----------------
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)

#------------------------USER INTERFACE-------------------
window = Tk()
window.title("Python Pomodoro")
window.config(padx=100,pady=50,bg=DARK)

title_label = Label(text="Timer",fg=WHITE,bg=DARK,font=(FONT_NAME,36))
title_label.grid(column=1,row=0)

canvas = Canvas(width=200,height=224,bg=DARK,highlightthickness=0)
python_image = PhotoImage(file="python.png")
canvas.create_image(100,112,image = python_image)
timer_text = canvas.create_text(100,88,text="00:00",fill="white",font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1,row=1)

start_button = Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(column=2,row=2)

check_marks = Label(text="✔",fg=GREEN,bg=DARK,font=(FONT_NAME,28))
check_marks.grid(column=1,row=3)

window.mainloop()