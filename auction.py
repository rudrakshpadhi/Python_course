print("Welcome to Blind Auction")


print(''''   ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                   /_______________\'''')


run = True
dict = {}
while(run):
    name = input("What is your name?\n")
    price = int(input("What price are you bidding at?\n"))
    dict[name] = price
    if(input("Are there other users who want to bid\n").lower()!="yes"):
        run = False
    print("\n"*100)
max_bid = 0
winner = ""
for key in dict:
    if(dict[key]>max_bid):
        winner = key

print(f"The winner of the bid is {winner}")