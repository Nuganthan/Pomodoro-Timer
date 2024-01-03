from tkinter import *
import math
# ----------------------------------CONSTATNTS------------------------------------
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# -----------------------------------TIMER RESET----------------------------------
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    check_mark_label.config(text="")
    timer_label.config(text="Timer", fg=GREEN)
    global reps
    reps = 0
# -----------------------------------TIMER MECHANISM------------------------------
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        countdown(LONG_BREAK_MIN * 60)
        timer_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        countdown(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=RED)
    else:
        countdown(WORK_MIN * 60)
        timer_label.config(text="Work", fg=GREEN)

# -----------------------------------COUNTDOWN MECHANISM--------------------------
def countdown(count):
    min = math.floor(count/60)
    if min < 10:
        min = f"0{min}"

    sec = count % 60
    if sec < 10:
        sec = f"0{sec}"

    canvas.itemconfig(timer_text, text=f"{min} : {sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        marks = ""
        for _ in range(reps//2):
            marks += "✔"
        check_mark_label.config(text=marks)


# -----------------------------------UI SETUP-------------------------------------
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=("Bauhaus 93", 50), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

canvas = Canvas(height=300, width=300, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(150, 150,image=tomato_img)
timer_text = canvas.create_text(150, 170, text="00:00", fill="white", font=("Impact",28))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", font=("Berlin Sans FB", 14), command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", font=("Berlin Sans FB", 14), command=reset_timer)
reset_button.grid(row=2, column=2)

check_mark_label = Label(text="", font=(100), fg=GREEN, bg=YELLOW)
check_mark_label.grid(row=3, column=1)

window.mainloop()