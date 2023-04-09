def intersection(a,b):
    for i in a:
        for j in b:
            if i==j:
                b.remove(j)
            else:
                pass
    print(a+b)
a=input("Enter 1st list: ").split()
b=input("Enter 2nd list: ").split()
intersection(a,b)

        