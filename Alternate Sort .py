def alternate_sort(l):
    k=[]
    if(len(l)%2!=0):
        j=1
        while(j<=len(l)-1):
            k.append(l[j])
            j=j+2
    else:
        j=1
        while(j<len(l)):
            k.append(l[j])
            j=j+2
    
    b=[]
    if(len(l)%2!=0):
        j=0
        while(j<=len(l)-1):
            b.append(l[j])
            j=j+2
    else:
        j=0
        while(j<len(l)-1):
            b.append(l[j])
            j=j+2
    b.sort()
    s=0
    n=[]
    if len(b)==len(k):
        h=0
        while s<int((len(b)+len(k))/2):
            n.append(b[h])
            n.append(k[h])
            s=s+1
            h=h+1
    else:
        h=0
        t=min(len(b),len(k))
        z=0
        for i in range(0,t):
            n.append(b[z])
            n.append(k[z])
            z+=1
        n.append(b[len(b)-1])
    print("The original List is ",n)
a=input("Enter the list: ").split()
t=map(int,list(a))
m=list(t)
alternate_sort(m)
            
    