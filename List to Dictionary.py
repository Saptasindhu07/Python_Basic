a=eval(input("Enter list 1: "))
b=eval(input("Enter list 2: "))
def func(a,b):
    d={}
    p=0
    for i in a:
        d[i]=b[p]
        p+=1
    return(d)
print(func(a,b))
