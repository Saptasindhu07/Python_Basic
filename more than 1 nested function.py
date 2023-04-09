list1=list(map(int,input("Enter the numbers: ").split()))
a,b,c,d=list1
def main_func(a,b,c,d):
    def func1(a,b):
        print(a+b)
        return a+b
    func1(a,b)
    def func2(func):
        def modified(c,d):
            print("Hello....")
            return func(c,d)
        return modified
    func2(func1)(c,d)
main_func(a,b,c,d)
        