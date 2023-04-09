def to_power(a):
    def base(b):
        def experiment(c):
            return a**b**c
        return experiment()
    return base
a=int(input("Enter base: "))
b=int(input("Enter Exponenet: "))
e=int(input("Enter exp: "))
c=to_power(b)
d=c(a)
print(d(e))