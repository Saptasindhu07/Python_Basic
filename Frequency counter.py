def freq(l,h):
    s=[]
    for i in range(0,len(l)):
        a=l[i]
        b=l.count(a)
        if a not in s:
            if b>=h:
                print("{} is Passed".format(a))
            else:
                print("{} is Failed".format(a))
            s.append(a)
        else:
            pass
a=input("Enter list ").split()
b=int(input("Enter frequency required: "))
freq(a,b)
        