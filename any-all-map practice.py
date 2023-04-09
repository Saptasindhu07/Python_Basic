a=[1,2,3,4,5,6,7,8,9,10]
b=[4,6,8,10]
c=[3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59]
def func(x):
    l=[i for i in range(2,x)]
    for j in l:
        if x%j==0:
            return(False)
        else:
            return(True)
if all(list(map(func,c))):
    print("All Prime")
else:
    print("Otherwise ")