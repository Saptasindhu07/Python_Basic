a=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
b=[1,2, 3, 4, 5, 6, 7, 8, 9, 10]
def func(x,b):
    return(x**b)
print(list(map(func,a,b)))