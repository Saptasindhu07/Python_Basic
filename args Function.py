def func(*add):
    sum=0
    for i in add:
        sum+=i
    return(sum)
a=map(int,input("Enter numbers: ").split())
a=list(a)
print(a)
print(func(*a))
