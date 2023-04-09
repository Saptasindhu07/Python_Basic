def decorator_func(func):
    def modified_func(*args):
        print("Hello World")
        func(*args)
        print("Thanks")
    return modified_func
@decorator_func
def func(a,b):
    print(a+b)
func(2,3)
"""x=decorator_func(func)
x(2,3)"""