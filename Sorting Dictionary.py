d=[
    {"name":"Sapta Sindhu", "marks":80},
    {"name":"Sagnik Hodu","marks":100},
    {"name":"Ujan Lodu","marks":101}
]
def func(item):
    return item['marks']
sorted_= sorted(d,key=func)
print(sorted_)