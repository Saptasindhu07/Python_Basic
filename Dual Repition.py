num=input("Enter numbers: ").split()
z=True
k=[]
for i in range(len(num)-1):
    if num[i]==num[i+1]:
        if num[i] not in k:
            k.append(num[i])
        else:
            print("1st dual Repition occurs at ",[num[i],num[i]])
            z=False
            break
print(z)

