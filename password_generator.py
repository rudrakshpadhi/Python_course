import random
print(''' ____                                     _    
|  _ \ __ _ ___ _____      _____  _ __ __| |   
| |_) / _` / __/ __\ \ /\ / / _ \| '__/ _` |   
|  __/ (_| \__ \__ \\ V  V / (_) | | | (_| |   
|_|___\__,_|___/___/ \_/\_/ \___/|_|  \__,_|   
 / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
| |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
| |_| |  __/ | | |  __/ | | (_| | || (_) | |   
 \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   ''')
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password=""
length = nr_letters+nr_symbols+nr_numbers
for number in range(0,length):
    curr = []
    if(nr_letters>0):
        curr.extend(letters)
    if(nr_symbols>0):
        curr.extend(symbols)
    if(nr_numbers>0):
        curr.extend(numbers)
    curr_char = random.choice(curr)
    if(curr_char in letters):
        nr_letters-=1
    elif(curr_char in numbers):
        nr_numbers-=1
    else:
        nr_symbols-=1
    password+=curr_char
password_char=[]
for character in password:
    password_char.append(character)
random.shuffle(password_char)
password = ''.join(password_char)
print("Your password is: "+password)