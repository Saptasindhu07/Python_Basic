def odd_even(num):
    if(num%2==0):
        return "even"
    else:
        return "odd"
a=int(input("Enter a number "))
print("Your number is {}".format(odd_even(a)))