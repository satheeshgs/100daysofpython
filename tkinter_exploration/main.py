from tkinter import *

def button_clicked():
    to_display = input.get()
    my_label.config(text=to_display)


window = Tk()
window.title("My First GUI")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

#Label
my_label = Label(text="I am a label", font=("Arial", 24))
my_label.grid(column=0, row=0)
my_label.config(text="New text") #using config of the tcl commands

button1 = Button(text="Click me", command=button_clicked)
button1.grid(column=1, row=1)

button2 = Button(text="Click me2")
button2.grid(column=2, row=0)

#entry
input = Entry(width=10)
input.grid(column=3, row=2)

window.mainloop()
