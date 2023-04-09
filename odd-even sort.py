def oddeven(l):
    x=[]
    y=[]
    for i in l:
        if int(i)%2==0:
            x.append(i)
        else:
            y.append(i)
    x.append(y)
    print(x)
a=input("Enter list ").split()
oddeven(a)