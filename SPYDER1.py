tet=2
while(tet>1):
    ch=input("Enter character: ")
    if((ch>="a"and ch<="z")or(ch>="A"and ch<="Z")or(ch>="0"and ch<="9")):
       print("Normal char")
    else:
       print("Special character")
    zx=input("Any other character?")
    if zx=="yes" :
        continue
    else:
        break
print("Thank You")