a=eval(input("Enter List: "))
new_list=[i[-1:-len(i)-1:-1] for i in a]
print(new_list)