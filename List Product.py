def prod(l):
    t=1
    s=[]
    for i in l:
        if i not in s:
            t=t*int(i)
            s.append(i)
        else:
            pass
    print("Product is ",t)
a=input("Enter a number ").split()
prod(a)