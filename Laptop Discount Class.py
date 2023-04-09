global a
global b
a=input("Enter Laptop Name: ")
b=int(input("Enter Price: "))
class laptop:
    def __init__(self,laptop_name,laptop_price):
        self.laptop_name=laptop_name
        self.laptop_price=laptop_price
    def discount(self):
        if self.laptop_price>10000:
            return "Discount is 10%"
        else:
            return "Discount is 5%"
s=laptop(a,b)
print(s.discount())
        