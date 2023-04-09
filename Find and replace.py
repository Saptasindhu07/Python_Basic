d=input("Enter sentence ")
st=input("You want find or replace ")
if st=="find":
    b=input("Enter char ")
    c=int(input("Enter occurence count "))
    a=d
    for i in range(0,c):
        x=a.find(b)
        a=a[x+1:]
    print("Required index is ",x)
    print("New string is ",d[x:]) 
else:
    y=input("Enter character to replace ")
    m=input("Enter with what to replace ")
    print(d.replace(y,m))

    
