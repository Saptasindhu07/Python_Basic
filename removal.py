def removal(l,j):
    a=l.count(j)
    for i in range(0,a):
        l.remove(j)
    print(l)
a=input("Enter list: ").split()
b=input("Enter character to remove: ")
removal(a,b)