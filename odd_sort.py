def odd_sort(l):
    m=[]
    s=[]
    h=[]
    for i in l:
        if int(i)%2==0:
            m.append(l.index(i))
            s.append(i)
        else:
            h.append(i)
            h.sort()
    print(s)
    print(h)
    output=[]
    tt=0
    mm=0
    nn=0
    while tt<len(l):
        if tt in m:
            output.append(s[mm])
            mm+=1
        else:
            output.append(h[nn])
            nn+=1
        tt+=1
    print(output)
a=input("Enter List: ").split()
odd_sort(a)
    
    
        
        
            
    