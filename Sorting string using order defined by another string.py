def pattern(a,b):
    l=[]
    b=list(b)
    for i in a:
        if i in b:
            if b.count(i)>1:
                while b.count(i)>0:
                    l.append(b[b.index(i)])
                    b.remove(i)
            else:
                l.append(i)
    return("".join(l[-1::-1]))
a=input("Enter pattern string: ")
b=input("Enter string: ")
print("The word in reverse pattern is: ",pattern(a,b))
            
