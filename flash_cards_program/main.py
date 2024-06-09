import pandas

BACKGROUND_COLOR = "#B1DDC6"
LABEL_FONT = ("Ariel", 40, "italic")
TEXT_FONT = ("Ariel", 60, "bold")
from tkinter import *
import random
import time
import pandas as pd

current_card = {}
to_learn = {}


#FUNCTIONS---------------->
try:
    french_dataframe = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_dataframe = pd.read_csv("data/french_words.csv")
    to_learn = original_dataframe.to_dict(orient="records")
else:
    to_learn = french_dataframe.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    french_word = current_card['French']
    canvas.itemconfig(canvas_image, image=flash_front)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=f"{french_word}", fill="black")
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    global current_card
    english_word = current_card['English']
    canvas.itemconfig(canvas_image, image=flash_back)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=f"{english_word}", fill="white")

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

#create tkinter window
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# flip after 3 seconds
flip_timer = window.after(3000, func=flip_card)


#create canvas for flashcard
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_front = PhotoImage(file="images/card_front.png")
flash_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=flash_front)
title_text = canvas.create_text(400, 150, text="", fill="black", font=LABEL_FONT)
word_text = canvas.create_text(400, 263, text="", fill="black", font=TEXT_FONT)
canvas.grid(row=0, column=0, columnspan=2)


#create buttons for yes and no
yes_image = PhotoImage(file="images/right.png")
yes_button = Button(image=yes_image, highlightthickness=0, bg=BACKGROUND_COLOR, highlightcolor=BACKGROUND_COLOR, command=is_known)
yes_button.grid(row=1, column=1)

no_image = PhotoImage(file="images/wrong.png")
no_button = Button(image=no_image, highlightthickness=0, bg=BACKGROUND_COLOR, highlightcolor=BACKGROUND_COLOR, command=next_card)
no_button.grid(row=1, column=0)

next_card()

window.mainloop()
