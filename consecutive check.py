def consecutive(l):
    s=[]
    for i in range(0,len(l)-2):
        if l[i] not in s:
            if(l[i]==l[i+1] and l[i+1]==l[i+2]):
                print(l[i]," is Consecutive")
                s.append(l[i])
            else:
                print(l[i]," is non Consecutive")
        else:
            pass
a=input("Enter list ").split()
consecutive(a)
            