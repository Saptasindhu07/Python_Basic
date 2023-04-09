x=map(int,list(input("Enter list of integers: ").split()))
y=all(a%2==0 for a in x)
z=any(a%2!=0 for a in x)
print(y," ",z)
