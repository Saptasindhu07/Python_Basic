#max,min,duplicates
d=eval(input("Enter the dictionary: "))
_maxmin=list(d.values())
for i in _maxmin:
    max1=_maxmin[0]
    if i > max1:
        max1=i
for i in _maxmin:
    min1=_maxmin[0]
    if i<min1:
        min1=i
non_duplicates=[]
duplicates=[]
for i in _maxmin:
    if i not in non_duplicates:
        non_duplicates.append(i)
    elif i not in duplicates:
        duplicates.append(i)
    else:
        pass
duplicated_keys=[]
for k in d:
    if d[k] in duplicates:
        duplicated_keys.append(k)
    else:
        pass
print("Maximum value present is {} and Minimum value present is {}".format(max1,min1))
print("Dupplicate values: ",duplicates)
print("Keys of dupplicate values: ",duplicated_keys)
        