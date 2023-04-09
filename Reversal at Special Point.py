def reversal(l,m):
    s=l[:m]
    t=l[m:]
    n=t[-1:-len(t)-1:-1]
    z=s+n
    print(z)
a=input("Enter list: ").split()
b=int(input("Enter index of reversal point: "))
reversal(a,b)
