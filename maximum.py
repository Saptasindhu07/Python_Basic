def maximum(l):
    s=l[0]
    for i in l:
        if int(i)>int(s):
            s=i
    print("The maximum value is {} and its index is {}".format(s,l.index(s))) 
a=input("Enter list: ").split()
maximum(a)