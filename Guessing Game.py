import random
print("Welcome to Guessing Game")
a=random.randint(0,100)
b=random.randint(a,a+10)

m=0
while m<1:
    x=int(input("Guess any number between {} and {} \n".format(a,a+10)))
    if x<b:
        print("Little more pls")
        continue
    elif x>b:
        print("Little less pls")
        continue
    elif x==b:
        print("Correct")
        break
print("Thanks")