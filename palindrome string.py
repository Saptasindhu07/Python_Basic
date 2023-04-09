st=input("Enter String: ")
l=len(st)
a=l
b=l-1
c=""
for i in range(0,a):
    d=st[b:a]
    c=c+d
    a=a-1
    b=b-1
print(c)    
if(c==st):
    print("Palindrome")
else:
    print("Non Palindrome")
    