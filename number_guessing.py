#number guessing game
print(''' _______               ___.                    ________                            .__                 
 \      \  __ __  _____\_ |__   ___________   /  _____/ __ __   ____   ______ _____|__| ____    ____   
 /   |   \|  |  \/     \| __ \_/ __ \_  __ \ /   \  ___|  |  \_/ __ \ /  ___//  ___/  |/    \  / ___\  
/    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ \    \_\  \  |  /\  ___/ \___ \ \___ \|  |   |  \/ /_/  > 
\____|__  /____/|__|_|  /___  /\___  >__|     \______  /____/  \___  >____  >____  >__|___|  /\___  /  
        \/            \/    \/     \/                \/            \/     \/     \/        \//_____/   ''')

import random
def game(number,attempts):
    for i in range(0,attempts):
        guess = int(input("Guess a number: "))
        if(number==guess):
            print(f"Congrats, you guessed the number. It was {number}")
            break
        elif(number>guess):
            print(f"Too low, guess again.\nYou have {attempts-i-1} attempts remaining.")
        else:
            print(f"Too high, guess again\nYou have {attempts-i-1} attempts remaining.")
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.(inclusive)")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard: ").lower()
attempts = 0
if(difficulty=="easy"):
    attempts = 10
else:
    attempts = 5
running = True
while(running):
    number = random.randint(1,100)
    print(number)
    game(number,attempts)
    print(f"You lost the game. The number was {number}.")
    if(input("Do you want to play again (y/n): ").lower()=='n'):
        running = False
