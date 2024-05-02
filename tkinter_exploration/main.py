from tkinter import *

window = Tk()
window.title("My First GUI")
window.minsize(width=500, height=300)

#Label
my_label = Label(text="I am a label", font=("Arial", 24))
my_label.pack(side="top")


my_label.config(text="New text") #using config of the tcl commands

def button_clicked():
    to_display = input.get()
    my_label.config(text=to_display)

button = Button(text="Click me", command=button_clicked)
button.pack()


#entry
input = Entry(width=10)
input.pack()

window.mainloop()
