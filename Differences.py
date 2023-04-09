global diff
def greatest_least(l):
    l.sort()
    diff=l[1]-l[0]
    a=0
    b=1
    while(b<len(l)):
        n=l[b]-l[a]
        if n<diff:
            diff=n
        else:
            pass
        a=a+1
        b=b+1
    print("Smallest diff is ",diff)
    k=int(sorted(l)[len(l)-1])-int(sorted(l)[0])
    print("Required difference is ",k- int(diff))
a=map(int,input("Enter list: ").split())
b=list(a)
greatest_least(b)

        
        