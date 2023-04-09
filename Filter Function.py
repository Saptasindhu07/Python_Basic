a=list(map(int,list(input("Enter list").split())))
result=list(filter(lambda a: a%2==0, a))
print(result)