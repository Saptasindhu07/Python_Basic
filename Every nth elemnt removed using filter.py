a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n=int(input("Enter n: "))
s=filter(lambda x: (a.index(x)+1)%n!=0,a)
print(list(s))