import tkinter

window = tkinter.Tk()
window.title("My First GUI")
window.minsize(width=500, height=300)

#Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24))
my_label.pack(side="top")






window.mainloop()
