# -*- coding: utf-8 -*-
string=input("Enter a string")
a=len(string)
for i in range(a-1,-1,-1):
    print(string[i])
string2=input("Enter 2nd string")
a=len(string2)
s=""
for i in range(a-1,-1,-1):
    s=s+string2[i]
print(s)
name=input("Enter name ")
print(len(name))
print("Name in reverse order is {}".format(name[-1:-len(name)-1:-1]))
