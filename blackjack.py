'''Game of Black jack'''
print('''.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      '------'                           |__/  ''')
import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
def deal_cards(deck,number):
    for i in range(number):
        deck.append(random.choice(cards))
def score(deck):
    total = 0
    for card in deck:
        total += card
    return total
running = True 
while(running):
    player_cards = []
    comp_cards = []
    deal_cards(player_cards,2)
    deal_cards(comp_cards,2)
    print(f"Your cards are: {player_cards}")
    print(f"Computer's first card is : {comp_cards[0]}")
    game = True
    while(game):
        draw_card = True
        if(input("Do you want to draw another card? (y/n) ")=="y"):
            draw_card = True
            deal_cards(player_cards,1)
            print(f"Your cards are: {player_cards})")
            if(score(player_cards)>21):
                print("You Lose")
                break
        else:
            draw_card = False
        print(f"Computer's cards are: {comp_cards}")
        if(score(comp_cards)<17):
            deal_cards(comp_cards,1)
            print(f"Computer's cards are: {comp_cards}")
        if(score(comp_cards)>21):
            print("You win")
            break
        if(draw_card==False):
            if(score(player_cards)>score(comp_cards)):
                print("You win")
            elif(score(player_cards)<score(comp_cards)):
                print("You lose")
            else:
                print("Draw")
            game = False 
    if(input("Do you want to play again? (y/n) ")=='y'):
        running = True    
    else:
        running = False
        print("Thanks for playing")
        




