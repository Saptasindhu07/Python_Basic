a=input("Enter the word ")
l=[]
for i in a:
    l.append(i)
for i in l:
    if i in ["a","e","i","o","u","A","E","I","O","U"]:
        l[l.index(i)]=chr(ord(i)+2)
print("".join(l))