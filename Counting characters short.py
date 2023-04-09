a=input("Enter your name ")
c=""
for i in range(0,len(a)):
    if a[i] not in c:
        print("{} appears {} times".format(a[i],a.count(a[i])))
        c=c+a[i]
    else:
        pass
    