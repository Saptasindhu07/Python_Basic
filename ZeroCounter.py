def zero_separation(l):
    k=1
    for i in range(1,len(l)-1):
        if l[i]=="0":
            continue
        elif l[i-1]=="0" or l[i+1]=="0":
            k=k+1
        else:
            pass
    print(k)
a=input("Enter list: ").split()
zero_separation((a))
        