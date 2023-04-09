def rev(l):
    c=len(l)
    for i in range(0,c):
        d=l[i]
        l[i]=d[-1:-len(d)-1:-1]
    return l
a=input("Enter list: ").split()
print(rev(a))