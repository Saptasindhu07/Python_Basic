def is_palindrome(a):
    s=""
    for i in range(-1,-len(a)-1,-1):
        s=s+a[i]
    if a==s:
        return True
    else:
        return False
a=input("Enter Word: ")
print("Number is palindrome: ",is_palindrome(a))
        