print(''',adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88 ''')
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(word,shift):
    encrypted = ""
    for ch in word:
        if ch in alphabet:
            num = alphabet.index(ch)
            encrypted += alphabet[(num+shift)%26]
        else:
            encrypted += ch
    return encrypted

def decrypt(word,shift):
    decrypted = ""
    for ch in word:
        if ch in alphabet:
            num = alphabet.index(ch)
            decrypted += alphabet[(num-shift)%26]
        else:
            decrypted += ch
    return decrypted

game_on = True
while(game_on):
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    while(choice.lower()!="encode" and choice.lower()!="decode"):
        choice = input("Input either encode or decode:\n")
    word = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if(choice=="encode"):
        result = encrypt(word,shift)
    else:
        result = decrypt(word,shift)
    print(f"Here's the {choice}d result: {result}")
    keep_going = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    while(keep_going!="yes"and keep_going!="no"):
        keep_going = input("Type either yes or no\n").lower()
    if(keep_going!="yes"):
        game_on = False
print("Goodbye")