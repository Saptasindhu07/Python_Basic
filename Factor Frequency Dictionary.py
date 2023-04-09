a=eval(input("Enter the list: "))
result={}
for i in range(1,max(a)):
    count=0
    for j in a:
        if j%i==0:
            count+=1
    result[i]=count
for x,y in result.items():
    print("{} is divisible by {} values".format(x,y))
