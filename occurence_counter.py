def occurence_counter(a,b,c): #a is list b is argument
    for i in a:
        s=[]
        t=i.count(b)
        if t==c:
            for j in range(0,c):
                k=i.index(b)
                s.append(i[k])
                i.pop(k)
            print(s," from nested list ",a.index(i)+1)
        else:
            pass
a=eval(input("Enter a list: "))
b=int(input("Enter character to search: "))
c=int(input("Enter Observation count required: "))
occurence_counter(a,b,c)