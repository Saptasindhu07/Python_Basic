def least(l):
    t=[]
    a=l[0]
    for i in l:
        if int(i)<int(a):
            a=i
        else:
            pass
    t.append(a)
    l.remove(a)
    return(t)
def greatest(l):
    if len(l)!=0:
        t=[]
        a=l[0]
        for i in l:
            if int(i)>int(a):
                a=i
            else:
                pass
        t.append(a)
        l.remove(a)
        return(t)
    else:
        return("")
b=input("Enter the lsit of numbers: ").split()
c=map(int,list(b))
a=list(c)
h=[]
while len(a)>0:
    h.append(least(a))
    h.append(greatest(a))
h.remove("")
print(h)

    

    
