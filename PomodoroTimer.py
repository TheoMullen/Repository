import tkinter

import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
TIMER_FONT = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
can_press_start = True

# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    window.after_cancel(timer)
    canvas.itemconfigure(canvas_text, text="25:00")
    checkmark_label.configure(text="")
    timer_label.configure(text="Timer")
    global reps
    reps = 0
    global can_press_start
    can_press_start = True


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    global can_press_start
    if can_press_start:

        global reps
        reps += 1

        if reps % 2 != 0:
            timer_label.configure(text="Work", fg=GREEN)
            count_down(work_sec)
        elif reps % 8 == 0:
            timer_label.configure(text="Long Break", fg=RED)
            count_down(long_break_sec)
        else:
            timer_label.configure(text="Short Break", fg=PINK)
            count_down(short_break_sec)

        can_press_start = False

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(time):

    count_min = math.floor(time / 60)
    count_sec = time % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(canvas_text, text=f"{count_min}:{count_sec}")


    if time > 0:
        global timer
        timer = window.after(1000, count_down, time - 1)
    else:
        global  can_press_start
        can_press_start = True
        start_timer()
        points = range(math.floor(reps / 2))
        checkmarks = ["✔" for point in points]
        checkmark_label.configure(text=checkmarks, bg="white", fg=GREEN)



# ---------------------------- UI SETUP ------------------------------- #

# window
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg="white")


# images
tomato = tkinter.PhotoImage(file="tomato.png")


# canvas
canvas = tkinter.Canvas(width=200, height=224, bg="white", highlightthickness=0)
canvas.create_image(100, 112, image=tomato)
canvas_text = canvas.create_text(100, 130, text="25:00", fill="white", font=(TIMER_FONT, 35, "bold"))
canvas.grid(column=1, row=1)


# labels
checkmark_label = tkinter.Label(text="", bg="white", fg=GREEN)
checkmark_label.grid(column=1, row=4)

timer_label = tkinter.Label(text="Timer", font=("Arial", 40, "bold"), fg=GREEN, bg="white")
timer_label.grid(column=1, row=0)


# buttons
start = tkinter.Button(text="Start", highlightthickness=0, fg=GREEN, command=start_timer)
start.grid(column=0, row=2)
reset = tkinter.Button(text="Reset", highlightthickness=0, fg=GREEN, command=reset)
reset.grid(column=2, row=2)






window.mainloop()