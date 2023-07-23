from tkinter import *
from tkinter.font import Font

w = Tk()
w.geometry("1200x800")
w.configure(background="#1f1f1f")
w.title("To-Do List")

f = Font(family="Calibri", size=32)
frame = Frame(w)
frame.pack(pady=8)
list = Listbox(frame, font=f, width="50", height="10", bg="#050505",
               bd=0, fg="#ffffff", highlightthickness=0,
               selectbackground="#82e8e0", activestyle="none")
list.pack(side=LEFT, fill=BOTH)

s = Scrollbar(frame)
s.pack(side=RIGHT, fill=BOTH)
list.config(yscrollcommand=s.set)
s.config(command=list.yview)

entries = Entry(w, font=("Calibri", 32), width=30, bg="#cf9fff")
entries.pack(pady=20)

button_frame = Frame(w, bg="#1f1f1f")
button_frame.pack(pady=20)


def delete():
    list.delete(ANCHOR)


def add():
    list.insert(END, entries.get())
    entries.delete(0, END)


def cross():
    if list.itemcget(list.curselection(), "fg") == "#3fdb30":
        list.itemconfig(list.curselection(), fg="#ffffff")
        list.selection_clear(0, END)
    else:
        list.itemconfig(list.curselection(), fg="#3fdb30")
        list.selection_clear(0, END)
    


def delete_crossed():
    count = 0
    while count < list.size():
        if list.itemcget(count, "fg") == "#3fdb30":
            list.delete(list.index(count))
        else:
            count += 1


delete_button = Button(button_frame, text="Delete", command=delete,
                       bg="#d93434", font=("Calibri", 12))
add_button = Button(button_frame, text="Add", command=add, bg="#d93434",
                    font=("Calibri", 12))
cross_button = Button(button_frame, text="Cross/Uncross", command=cross,
                      bg="#d93434", font=("Calibri", 12))
dc_button = Button(button_frame, text="Delete All Crossed",
                   command=delete_crossed, bg="#d93434", font=("Calibri", 12))

delete_button.grid(row=0, column=0)
add_button.grid(row=0, column=1, padx=20)
cross_button.grid(row=0, column=2)
dc_button.grid(row=0, column=4)

w.mainloop()
