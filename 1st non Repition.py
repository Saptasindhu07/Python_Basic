def non_repeated(l):
    for i in l:
        if l.count(i)==1:
            print(i)
            break
        else:
            pass
list1=input("Enter list ").split()
non_repeated(list1)