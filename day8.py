# def add(a,b):
#     return a+b

# a = int(input("enter a number "))
# b = int(input("enter another number "))
# print(add(a,b))

def greet(name):
    print(f"hello {name}!")

greet(input("Enter your name: ").lower())

#keyword arguments:
def addthensubtract(a,b,c):
    return a+b-c

print(addthensubtract(b=2,c=3,a=5))
print(ord('a'))