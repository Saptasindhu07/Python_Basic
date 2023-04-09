a=input("Enter string ")
b=input("Enter character wanted: ") 
x=lambda a,b: True if a[0]==b else False
print(x(a,b))