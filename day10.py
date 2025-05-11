#functions with outputs
def format_name(first_name,last_name):
    first_name = first_name.title()
    last_name = last_name.title()
    print(first_name+" "+last_name)

first = input()
second = input()
format_name(first,second)
