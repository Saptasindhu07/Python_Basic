a=eval(input("Enter a list of tuples: "))
t=[]
for i in a:
    k=[]
    for j in i:
        k.append(j)
    t.append(k)
print(t)