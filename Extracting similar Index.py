def extraction(l,a,x): 
    for i in range(0,len(l)):
        if a[i]==x:
            print(l[i])
        else:
            pass
l=input("Enter 1st list: ").split()
a=input("Input 2nd list: ").split()
x=input("Enter search argument: ")
extraction(l,a,x)
            