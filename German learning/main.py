import tkinter as tk
from tkinter import messagebox
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
GERMAN = "German"
ENGLISH = "English"

try:
    data=pd.read_csv("words_to_learn.csv", sep=";").to_dict(orient="records")
except FileNotFoundError:
    data=pd.read_csv("most-common-1000-german-words.csv", sep=";").to_dict(orient="records")

current_card={}

def next_word():
    global current_card, flip_timer
    if len(data)==0:
        tk.messagebox.showinfo(title="Congratulation", message="Congratulation! You've completed your course!")
        exit(0)
    window.after_cancel(flip_timer)
    current_card=random.choice(data)
    canvas.itemconfig(word_label, text=current_card[GERMAN], fill="black")
    canvas.itemconfig(language_label, text=GERMAN, fill="black")
    canvas.itemconfig(card_side, image=front_card_img)
    flip_timer = window.after(3000, flip)

def flip():
    canvas.itemconfig(card_side, image=back_card_img)
    canvas.itemconfig(word_label, text=current_card[ENGLISH], fill="white")
    canvas.itemconfig(language_label, text=ENGLISH, fill="white")

def remembered_word():
    data.remove(current_card)
    pd.DataFrame(data).to_csv("words_to_learn.csv", sep=";", index=False)
    next_word()

window = tk.Tk()
window.title("Flashy")
window.config( bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip)

canvas=tk.Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_img=tk.PhotoImage(file="images/card_front.png")
back_card_img=tk.PhotoImage(file="images/card_back.png")
card_side = canvas.create_image(400,263, image=front_card_img)
canvas.grid(column=0, columnspan=2, row=0)
language_label=canvas.create_text(400,150, text=GERMAN, font=("Ariel", 40, "italic"))
word_label = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

right_image=tk.PhotoImage(file="images/right.png")
right_button = tk.Button(image=right_image, highlightthickness=0, command=remembered_word)
right_button.grid(column=0, row=1)

wrong_image=tk.PhotoImage(file="images/wrong.png")
wrong_button = tk.Button(image=wrong_image, highlightthickness=0, command=next_word)
wrong_button.grid(column=1, row=1)

next_word()

window.mainloop()