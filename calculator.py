'''calculator'''

print("Welcome to python calculator\n")
print(''' _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|''')

keep_going = True
cnt = 0
def calc(a,b,op):
    if(op=='+'):
        return a+b
    elif(op=='-'):
        return a-b
    elif(op=='*'):
        return a*b
    else:
        return a/b
while(keep_going):
    if(cnt==0):
        first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))   
    print("+\n-\n*\n/")
    operation = True
    op = ""
    while(operation):
        op = input("Enter the operation that you want to perform: ")
        if(op=="+" or op=="-" or op=="*" or op=="/"):
            operation = False
    print("The result for your operation is: ",calc(first_number,second_number,op))
    condition = True
    while(condition):
        again = input(f"Do you want to continue calculating with, {calc(first_number,second_number,op)} (y/n) ")
        if(again=="y"):
            condition = False
            first_number = calc(first_number,second_number,op)
        elif(again=='n'):
            condition = False
            keep_going = False
    cnt+=1
