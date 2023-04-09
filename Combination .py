def combination(l):
    s=[]
    for i in l:
        for j in l:
            b=[i,j]
            s.append(b)
    for k in s:
        if k[0] is k[1]:
            s.remove(k)
    print(s)
a=input("Enter List: ").split()
combination(a)