import random
print('''
                      __                                                      .__                                  
_______  ____   ____ |  | __ ___________  ______   ___________    ______ ____ |__| ______ _________________  ______
\_  __ \/  _ \_/ ___\|  |/ / \____ \__  \ \____ \_/ __ \_  __ \  /  ___// ___\|  |/  ___//  ___/  _ \_  __ \/  ___/
 |  | \(  <_> )  \___|    <  |  |_> > __ \|  |_> >  ___/|  | \/  \___ \\  \___|  |\___ \ \___ (  <_> )  | \/\___ \ 
 |__|   \____/ \___  >__|_ \ |   __(____  /   __/ \___  >__|    /____  >\___  >__/____  >____  >____/|__|  /____  >
                   \/     \/ |__|       \/|__|        \/             \/     \/        \/     \/                 \/ 
                                                                                                                   
                                                                                                                   
                                                                                                                   
                                                                                                                   
                                                                                                                   
                                                                                                                   
''')
rock = '''_______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''
paper = '''_______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)'''
scissors = '''_______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

images = [rock,paper,scissors]
user_input=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))
computer_input = random.randint(0,2)
if(user_input<0 or user_input>2):
    print("Invalid number. Try again")
else:
    print("You chose:\n"+images[user_input])


print("Computer chose:\n"+images[computer_input])  



if(computer_input==user_input):
    print("It is a draw")
elif(computer_input==0 and user_input==1):
    print("You lose")
elif(computer_input==0 and user_input==2):
    print("You win")
elif(computer_input==1 and user_input==0):
    print("You lose")
elif(computer_input==1 and user_input==2):
    print("You win")
elif(computer_input==2 and user_input==0):
    print("You lose")
elif(computer_input==2 and user_input==1):
    print("You win")

