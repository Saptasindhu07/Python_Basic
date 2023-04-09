a=eval(input("Enter the list: "))
b=eval(input("Enter the 2nd list: "))
d={}
temp=0
for i in b: 
    if b.index(i)<=len(a)-1:
        d[a[b.index(i)]]=i
    else:
        break
print(d)
    
        
