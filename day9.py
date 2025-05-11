prog_dict = {"apple":"red","banana":"yellow","mango":"orange"}
# ///retrieve a value from the dictionary based on its key value//
print(prog_dict["apple"])
#adding a new pair to the dictionary
prog_dict["peach"]="white"
print(prog_dict["peach"])
#creating an empty dictionary
empty_dict = {}
#wiping an existing dictionary
# prog_dict = {}
print(prog_dict)
#modifying a value of a key in dictionary
prog_dict["apple"]="yellow"
print(prog_dict["apple"])
#creating a dict with a nested list
travel_log = {"France":["Lille","Dijon"],"India":["Delhi","Mumbai"]}
#how to print out individual cities
for pair in travel_log:
    for city in travel_log[pair]:
        print(city)

