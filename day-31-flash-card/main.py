from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

# ---------------------Tick--------------------- #
def tick():
    global current_card
    try:
        word_dict.remove(current_card)
    except ValueError:
        canvas.itemconfig(card_title, text="Congratulation", fill="BLACK")
        canvas.itemconfig(card_word, text="Finished", fill="BLACK")
    df2 = pd.DataFrame(word_dict)
    df2.to_csv("./data/words_to_learn.csv", index=False)
    next_card()

# ---------------------Next Card--------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = word_dict[random.randint(0, len(word_dict))-1]
    canvas.itemconfig(card_img, image=front_img)
    canvas.itemconfig(card_title, text="French", fill="BLACK")
    canvas.itemconfig(card_word, text=current_card["French"], fill="BLACK")
    flip_timer = window.after(3000, flip_card)


# ---------------------Timer--------------------- #
def flip_card():
    canvas.itemconfig(card_img, image=back_img)
    canvas.itemconfig(card_title, text="English", fill="WHITE")
    canvas.itemconfig(card_word, text=current_card["English"], fill="WHITE")


# -------------------------UI------------------------- #
try:
    df = pd.read_csv("./data/words_to_learn.csv")
    word_dict = df.to_dict(orient="records")
    if len(word_dict) == 0:
        df = pd.read_csv("./data/french_words.csv")
        word_dict = df.to_dict(orient="records")
except (FileNotFoundError, pd.errors.EmptyDataError):
    df = pd.read_csv("./data/french_words.csv")
    word_dict = df.to_dict(orient="records")

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
right_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_img = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

right_button = Button(image=right_img, highlightthickness=0, bd=0, command=tick)
right_button.grid(column=1, row=1)
wrong_button = Button(image=wrong_img, highlightthickness=0, bd=0, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()

window.mainloop()
