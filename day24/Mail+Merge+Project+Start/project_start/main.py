#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
with open("./Input/Letters/starting_letter.txt") as file:
    content = file.read()

with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()
cleaned_names = []    
for name in names:
    name = name.rstrip('\n')   
    cleaned_names.append(name) 
print(cleaned_names)   
for i in range(1,len(cleaned_names)+1):
    with open(f"./Output/file_{i}.txt","w") as file:
        file.write(content.replace("[name]",cleaned_names[i-1]))