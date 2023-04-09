def decorator1(func):
    def innerfunc(a,b):
        print("Hi")
        return func(a,b)
    return innerfunc 
def decorator2(func):
    def innerfunc(a,b):
        print("Bye")
        return func(a,b)
    print(innerfunc(1,2))
    return innerfunc
     #Expected 3
@decorator2 
@decorator1
def func(a,b):
    print( a+b)
func(2,3)