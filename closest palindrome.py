def closest_palindrome(string):
    l=[]
    for k in string:
        l.append(k)
    a=0
    m=0
    t=1
    while a<1:
        l[len(l)-t]=l[m]
        if l[-1::-1]==l:
            break
        else:
            pass
        m+=1
        t+=1
    print("closest palindrome is ","".join(l))
a=input("Enter String: ")
closest_palindrome(a)
        
        
        
        