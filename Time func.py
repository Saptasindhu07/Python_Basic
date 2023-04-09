import time
a=input("Enter your name\n")
b=input("Enter character to count ")
s=a.count(b)
t=a.count(b.capitalize())
print("Processing...",end="\r")
time.sleep(3)
print("Total case insensitive characters are {}".format(s+t))


