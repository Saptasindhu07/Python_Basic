string=input("Enter String: ")
a=[i for i in string]
l=[]
result=[]
count=0
for i in range(len(a)-1):
    for j in range(i+1,len(a)+1):
        l.append(a[i:j])
    count+=1
    if(count==len(a)-1):
        break
final=[]
for i in l:
    final.append(("".join(i)))
final.sort()
print(final)

        