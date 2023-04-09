def list_identifier(l):
    count=0
    for i in l:
        if type(i) is list:
            count+=1
    print("No.of list inside ur list is ",count)
count=0
while count<=0:
    a=eval(input("Enter list: "))
    list_identifier(a)
    d=input("Want to repeat?: ")
    if d=="yes":
        pass
    else:
        count+=1

