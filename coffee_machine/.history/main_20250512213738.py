MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk":20
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money":0
}
def sufficient(prompt,resources):
    if(resources["water"]-MENU[prompt]["ingredients"]["water"]<0):
        print("Sorry there is not enough water")
        return False
    elif(resources["milk"]-MENU[prompt]["ingredients"]["milk"]<0):
        print("Sorry there is not enough milk")
        return False
    elif(resources["coffee"]-MENU[prompt]["ingredients"]["coffee"]<0):
        print("Sorry there is not enough coffee")
        return False
    else:
        return True
def dispense(prompt,resources):
    resources["water"]-=MENU[prompt]["ingredients"]["water"]
    resources["milk"]-=MENU[prompt]["ingredients"]["milk"]
    resources["coffee"]-=MENU[prompt]["ingredients"]["coffee"]
def processTransaction(prompt,quarters,dimes,nickels,pennies):
    total_amt = quarters*0.25+dimes*0.1+nickels*0.05+pennies*0.01
    change = 0
    if(total_amt>MENU[prompt]["cost"]):
        change = total_amt-MENU[prompt]["cost"]
        resources["money"]+=total_amt-change
        print(f"Here is ${change} in change.")
        dispense(prompt,resources)
        print(f"Here is your {prompt}.Enjoy!")
    elif(total_amt==MENU[prompt]["cost"]):
        resources["money"]+=total_amt
        dispense(prompt,resources)
        print(f"Here is your {prompt}.Enjoy!")
    else:
        print(f"Sorry that's not enough money. Money refunded.")

drinks = ["cappuccino","latte","espresso"]
running = True
while(running):
    #prompting user about what they like 
    prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if(prompt=="off"):
        break
    elif(prompt in drinks):
        if(sufficient(prompt,resources)):
            print("Enter coins: ")
            quarters = int(input("Number of quarters : "))
            dimes = int(input("Number of dimes : "))
            nickels = int(input("Number of nickels : "))
            pennies = int(input("Number of pennies : "))
            processTransaction(prompt,quarters,dimes,nickels,pennies)
    elif(prompt=="report"):
        print(f'Water: {resources["water"]} ml\nMilk: {resources["milk"]} ml\nCoffee: {resources["coffee"]}\nMoney: {resources["money"]}')

