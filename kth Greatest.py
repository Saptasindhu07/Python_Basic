def greatest(l,k):
    for i in range(0,k):
        t=l[0]
        for i in l:
            if int(i)>int(t):
                t=i
            else:
                pass
        l.remove(t)
    print(t)
a=input("Enter List: ").split()
b=int(input("Enter rank of greatness: "))
greatest(a,b)