a=eval(input("Enter List of Tuples: "))
a.sort(key= lambda x: x[0][1], reverse=True)
print(a)