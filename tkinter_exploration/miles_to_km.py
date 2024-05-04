from tkinter import *

def calculate_kms():
    miles = miles_input.get()
    print(miles)
    kms = round(float(miles) * 1.609)
    print(kms)
    kilo_result.config(text=f"{kms}")


window = Tk()
window.title("Miles to KM converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=10)
miles_input.insert(END, string="0")
miles_input.grid(column=1, row=0)


#labels
miles_label = Label(text="Miles", font=("Arial", 10))
miles_label.grid(column=2, row=0)

km_label = Label(text="Km", font=("Arial", 10))
km_label.grid(column=2, row=1)

eq_label = Label(text="is equal to", font=("Arial", 10))
eq_label.grid(column=0, row=1)

kilo_result = Label(text="0")
kilo_result.grid(column=1, row=1)


calculate_button = Button(text="Calculate", command = calculate_kms)
calculate_button.grid(column=1, row=2)


window.mainloop()