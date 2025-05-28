from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
try:
    DATA = pd.read_csv("data/to_learn.csv")
except FileNotFoundError:
    DATA = pd.read_csv("data/french_words.csv")    
flip_timer = None
dictionary = {}
for index,row in DATA.iterrows():
    dictionary[row["French"]] = row["English"]


def gen_random_word():
    global flip_timer
    if flip_timer is not None:
        window.after_cancel(flip_timer)
    random_word = random.choice(list(dictionary.keys()))
    canvas.itemconfig(card_bg,image = card_front)
    canvas.itemconfig(language,text = "French",fill="black")
    canvas.itemconfig(word,text = random_word,fill="black")
    flip_timer = window.after(3000,flip_card,random_word)
def delete_word():
    try:
        del dictionary[canvas.itemcget(word,"text")]
    except KeyError:
        for key in list(dictionary.keys()):
            if(dictionary[key]==canvas.itemcget(word,"text")):
                del dictionary[key]
                break    
    #convert dictionary to csv file
    df = pd.DataFrame(list(dictionary.items()),columns = ["French","English"])
    df.to_csv("data/to_learn.csv",index = False)
    gen_random_word()

def flip_card(random_word):
    global flip_timer 
    flip_timer = None
    canvas.itemconfig(card_bg,image = card_back)
    canvas.itemconfig(language,text="English",fill = "white")
    canvas.itemconfig(word,text=dictionary[random_word],fill = "white")   
#creating window
window = Tk()
window.config(bg=BACKGROUND_COLOR)
window.title("Flashy")
window.config(padx=50,pady=50)

#images
card_front = PhotoImage(file = "images/card_front.png")
card_back = PhotoImage(file = "images/card_back.png")
tick = PhotoImage(file = "images/right.png")
wrong = PhotoImage(file = "images/wrong.png")
#canvas creation
canvas = Canvas(window,width = 800,height = 526,highlightthickness=0,bg = BACKGROUND_COLOR)
card_bg = canvas.create_image(400,263,image = card_front)
language = canvas.create_text(400,150,text="Title",font=("Ariel",40,"italic"))
word = canvas.create_text(400,263,text="Word",font=("Ariel",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)
#tick label 
tick_button = Button(window,image = tick,highlightthickness=0,command = delete_word)
tick_button.grid(row = 1,column =0)
#wrong label
wrong_button = Button(window,image = wrong,command = gen_random_word)
wrong_button.grid(row=1,column=1)
gen_random_word()
window.mainloop()
