import tkinter


def convert():
    answer = float(entry.get()) * 1.6
    answer_label.config(text=answer)


# Screen

window = tkinter.Tk()
window.title("Miles to Kilometers converter")


# Labels

miles_label = tkinter.Label(text="miles")
miles_label.grid(column=2, row=0)

is_equal_to_label = tkinter.Label(text="is_equal_to")
is_equal_to_label.grid(column=0, row=1)

answer_label = tkinter.Label(text="0")
answer_label.grid(column=1, row=1)

km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)


# Entry

entry = tkinter.Entry(width=8)
entry.grid(column=1, row=0)


# Button

button = tkinter.Button(text="Calculate", width=6, command=convert)
button.grid(column=1, row=2)


window.mainloop()
