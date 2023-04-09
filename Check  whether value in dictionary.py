sample_dict = {'a': 100, 'b': 200, 'c': 300}
a=int(input("Enter value to check: "))
if any([i==a for i in sample_dict.values()]):
    print("Present ")
else:
    print("Absent ")