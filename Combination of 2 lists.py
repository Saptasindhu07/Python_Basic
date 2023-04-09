def unique_combination(l,m):
    s=[]
    t=[]
    for i in l:
        for j in m:
            if [i,j] not in t:
                s.append([i,j])
                t.append([i,j])
            else:
                pass
    print(s)
a= input("Enter List 1 ").split()
b=input("Enter list 2 ").split()
unique_combination(a,b)
            
            
            