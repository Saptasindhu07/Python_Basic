a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
d=b
if(a>b):
    for i in range(0,b):
        if(b%d==0):
            if(a%d==0):
                print("HCF is ",d)
                break
            else:
                d=d-1
                continue
        else:
            d=d-1
            continue
            
    
    
    
