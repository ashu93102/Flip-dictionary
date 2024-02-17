import tkinter as tk
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
window = tk.Tk()
window.title("Translate")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# ------------------------ Data Read from CSV ------------------------ #
data = pandas.read_csv("data/letters.csv").to_dict(orient="records")
new_word = {}


def word_change():
    global new_word, flip_timer
    window.after_cancel(flip_timer)
    new_word = random.choice(data)
    card.itemconfig(word_image, image=card_front)
    card.itemconfig(initial_word, text="English", fill="black")
    card.itemconfig(translation, text=new_word["word"], fill="black")
    flip_timer = window.after(3000, func=change_word)


def change_word():
    card.itemconfig(word_image, image=card_back)
    card.itemconfig(initial_word, text="Hindi", fill="white")
    card.itemconfig(translation, text=new_word["hindi"], fill="white")


flip_timer = window.after(3000, func=change_word)
# --------------------------- Images -------------------------------- #
card_front = tk.PhotoImage(file="images/card_front.png")
card_back = tk.PhotoImage(file="images/card_back.png")
right_logo = tk.PhotoImage(file="images/right.png")
wrong_logo = tk.PhotoImage(file="images/wrong.png")

# -------------------------------- UI SETUP ------------------------------ #
card = tk.Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
word_image = card.create_image(400, 263, image=card_front)
initial_word = card.create_text(400, 150, text="text", font=("Arial", 40, "italic"))
translation = card.create_text(400, 283, text="word", font=("Arial", 60, "bold"))
card.grid(row=0, column=0, columnspan=2)

# Button
logo_right = tk.Button(image=right_logo, highlightthickness=0, bg=BACKGROUND_COLOR, padx=50,
                       highlightbackground=BACKGROUND_COLOR, command=word_change)
logo_right.grid(row=1, column=0)

logo_wrong = tk.Button(image=wrong_logo, highlightthickness=0, bg=BACKGROUND_COLOR, padx=50,
                       highlightbackground=BACKGROUND_COLOR, command=word_change)
logo_wrong.grid(row=1, column=1)

word_change()
window.mainloop()
