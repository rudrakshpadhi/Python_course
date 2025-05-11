print("Welcome to Python Pizza")
bill = 0
size = input("What size of pizza do you want? S,M or L:")
pepperoni = input("Do you want pepperoni in your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
if(size=='S'):
    bill+=15
elif(size=='M'):
    bill+=20
else:
    bill+=35

if(pepperoni=='Y'):
    bill+=3
        
        
if(extra_cheese=='Y'):
    bill+=1
print(f"{bill}")