#local and global variables

a = 10

def print_a():
    a = 20
    print(a)

print(a)
#python has no block scope which means operators like while for etc. cannot create a local scope only functions can
#modifying global variables with a scope

enemies = 2
print(enemies)
def increase_enemies():
    global enemies
    enemies+=1
    print(enemies)
increase_enemies()