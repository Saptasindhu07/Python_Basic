a=input("Enter list 1: ").split()
b=input("Enter List 2: ").split()
s=[]
registered=[]
for i in a:
    if i not in registered:
        if i in b:
            s.append(i)
            registered.append(i)
print(s)