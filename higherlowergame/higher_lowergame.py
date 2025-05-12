from logo import art,art2
from influencers import celebs
import random
a = ""
b = ""
winner = ""
correct = True
score = 0
def first_query(celebs):
    global a,b,winner,score
    print(art)
    random_keys = random.sample(list(celebs.keys()),2)
    a = random_keys[0]
    b = random_keys[1]
    if(celebs[a]>celebs[b]):
        winner = a
    else:
        winner = b  
    print(f"Compare A {a}")
    print(art2)
    print(f"Compare B {b}")
    option = input("Who has more followers? Type 'A' or 'B :").lower()
    if(winner==a and option=='a'):
        score+=1
        return True
    elif(winner==b and option=='b'):
        score+=1
        return True
    else:
        return False
def queries(celebs):
   global a,b,winner,score
   print(art)
   print(f"You're right! Current score: {score}")
   a = b
   while(b==a):
    b = random.choice(list(celebs.keys()))
   if(celebs[a]>celebs[b]):
    winner = a
   else:
    winner = b  
   print(f"Compare A {a}")
   print(art2)
   print(f"Compare B {b}")
   option = input("Who has more followers? Type 'A' or 'B :").lower()
   if(winner==a and option=='a'):
    score+=1
    return True
   elif(winner==b and option=='b'):
    score+=1
    return True
   else:
    return False
     
correct = first_query(celebs)
while correct:
    correct = queries(celebs)
if(not(correct)):
   print(art)
   print(f"Sorry that's wrong. Final score: {score}")


