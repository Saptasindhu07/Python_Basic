def combination(d):
    keys=list(d.keys())
    result=[]
    for i in range(0,len(keys)-1):
        value_list=d[keys[i]]
        for j in value_list:
            for k in d:
                if k==keys[i]:
                    pass
                else:
                    for l in d[k]:
                        result.append([j,l])
    return(list(result))
d1=eval(input("Enter dictionary1: "))
d2=eval(input("Enter dictionary 2: "))
print("1st combination: ")
print(combination(d1))
print("2nd combination: ")
print(combination(d2))
list1_win=0
list2_win=0
t=len(combination(d1))
for i in range(t):
    sum1=combination(d1)[i][0]+combination(d1)[i][1]
    sum2=combination(d2)[i][0]+combination(d2)[i][1]
    if(sum1>sum2):
        list1_win+=1
        print(sum1)
    else:
        list2_win+=1
        print(sum2)
if list1_win>list2_win:
    h=list(d1.keys())
    print("{} is the winner".format(h))
else:
    h=list(d2.keys())
    print("{} is the winner".format(h))
            
        