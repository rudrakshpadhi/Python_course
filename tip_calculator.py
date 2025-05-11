print("Welcome to the tip calculator!")
total = float(input("What was the total bill $"))
tip = float(input("How much tip would you like to give "))
people = int(input("How many people to split the bill "))

print("$"+str(round(((total + tip*total/100)/people),2)))