num=int(input("Enter a number: "))
reverse_numbers=[]
while num>0:
    reverse_numbers.append(num%10) #Storing values in reverse
    num=num//10
numbers=reverse_numbers[-1::-1] #Creating correct order
t=[]
for i in range(len(numbers)-1):
    k=[numbers[i]]
    for j in range(i+1,len(numbers)):
        k.append(numbers[j])
        t.append(list(k)) #List Of all possible Permutations
h=[]
for m in t:
    z=True
    n=0
    p=1
    while z==True and p<len(m):
        if m[n]==m[p]+1 or m[n]==m[p]-1:
            z=True
            n+=1
            p+=1
        else:
            z=False
    if z==True:
        h.append(list(m))
print("The List of all Possible Consecutive numbers is ")
print(h)
print(len(h)," Consective numbers")
print("Number of possible combinations are ",len(t))
