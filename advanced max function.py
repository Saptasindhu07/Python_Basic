d=[
    {"name":"Sapta Sindhu", "marks":80},
    {"name":"Sagnik Hodu","marks":100},
    {"name":"Ujan Lodu","marks":101}
]
l=[]
h=[]
for i in d:
    l.append(i["marks"])
    h.append(i["name"])
def func2(a):
    return(len(a))
maximum_marks= max(h, key=func2)
print(maximum_marks)