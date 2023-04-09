a=int(input("Enter How many Tuples you wish to enter: "))
t=[]
for i in range(a):
    a=eval(input("Enter Tuple "))
    t.append(a)
f=[]
for i in t:
    k=[]
    for s in range(0,len(i)):
        k.append(i[s])
    f.append(k)
h=len(f[0])
for i in f:
    if len(i)>h:
        h=len(i)
for i in f:
    if len(i)!=h:
        for j in range(h-len(i)):
            i.append(0)
    else:
        pass
print(f)
final_list=[]
for i in range(h):
    s=0
    for j in range(len(f)):
        s=s+f[j][i]
    final_list.append(s)
print(final_list)
        
    

    