name , age= input("Enter your name and age in any format: ").split()
print("Your name is {} and your age is {}".format(name,age))
n=list(map(int,input("Enter numbers ").split()))
print(n)
l=len(n)
t=0
for i in range(0,l):
    t=t+n[i]
print("Average is",t/l)