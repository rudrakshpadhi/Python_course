import random
guesses = 6
lives  = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
word_bank = [
    "apple", "dog", "table", "ocean", "happy", "chair", "house", "smile", "yellow", "bread",
    "banana", "puzzle", "garden", "thunder", "blanket", "sunset", "danger", "candle", "forest", "pillow",
    "elephant", "whirlpool", "pyramid", "paradox", "sphinx", "galaxy", "chandelier", "symphony", "vineyard", "eclipse",
    "tiger", "giraffe", "dolphin", "penguin", "koala",
    "cerulean", "crimson", "lavender", "sapphire", "chartreuse",
    "gravity", "atom", "molecule", "quantum", "neutron",
    "mountain", "volcano", "glacier", "archipelago", "desert",
    "protagonist", "villain", "epilogue", "manuscript", "trilogy"
]
def check(ch,word,curr_state,guesses):
    guessed = False
    for num in range(0,len(word)):
        if(ch==word[num]):
            string_list = list(curr_state)
            string_list[num]=ch
            curr_state = "".join(string_list)
            guessed = True
    if(not guessed):
        guesses-=1
        print(f"You guessed {ch}, that's not in the word. You lose a life.")
    else:
        print(curr_state)
    print(f"****************************{guesses}/6 LIVES LEFT****************************")
    print(lives[6-guesses])
    return curr_state,guesses
print(''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/''')
word = random.choice(word_bank)
curr_state = len(word)*"_"
win = False
while guesses>0 and not win :
    print("Word to guess: "+curr_state)
    ch = input("Guess a letter ").lower()
    curr_state,guesses = check(ch,word,curr_state,guesses)
    if(word==curr_state):
        win = True
if(not win):
    print(f"***********************IT WAS {word}! YOU LOSE**********************")
else:
    print(f"Congrats! You have won the word was {word}")
