a=input("Enter the string to center ")
b=input("Enter character to place on both sides" )
c=int(input("how many times each side"))
print(a.center(len(a)+c*2,b))