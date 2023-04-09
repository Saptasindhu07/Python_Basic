def min_subsequence(l):
    t=[]
    for i in range(0,len(l)-1):
        s=l[i]
        k=0
        p=int(l[i])
        for j in range(i+1,len(l)):
            k=int(l[j])
            p=p+k
            if p<float(s):
                s=p
            else:
                pass
        t.append(int(s))
    t[len(t)-1]=int(l[len(l)-1])
    v=t[0]
    for j in t:
        if j<v:
            v=j
        else: 
            pass
    print(v)
a=input("Enter list: ").split(",")
min_subsequence(a)