def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
a,b,c=map(int,input("Enter 3 numbers: ").split())
print("Greatest is ",greatest(a,b,c))
