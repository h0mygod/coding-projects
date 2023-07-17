import tkinter
from time import strftime

window = tkinter.Tk()
window.title("Digital Clock")


def time():
    s = strftime("%H:%M:%S %p")
    showtime.config(text=s)
    showtime.after(1000, time)


def mainloop():
    while 1:
        time()


showtime = tkinter.Label(window, font=("Helvetica", 90, "bold"),
                         foreground="black")
showtime.pack(anchor="center")
time()

tkinter.mainloop()
