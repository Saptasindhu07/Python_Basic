def combination(l):
    s=[]
    for i in l:
        for j in l:                        #EXCEPTION
            b=[i,j]                        #HANDLING
            s.append(b)
    for k in s:
        if k[0] is k[1]:
            s.remove(k)
    print(s)

numbers=input("Enter numbers: ").split()
t=[]
for i in range(len(numbers)-1): #Initatiating Counter 1
    for j in range(i+1,len(numbers)):#Initaiating Counter 2
        n=[numbers[i]]
        n.append(numbers[j])
        for k in range(j+1,len(numbers)):#Variable Counters
            n.append(numbers[k])
            print(n)
combination(numbers)

            
            