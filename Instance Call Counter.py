global a
global b
a=input("Enter Laptop Name: ")
b=int(input("Enter Price: "))
class laptop:
    count1=0
    def __init__(self,laptop_name,laptop_price):
        laptop.count1+=1
        self.laptop_name=laptop_name
        self.laptop_price=laptop_price
    def discount(self):
        if self.laptop_price>10000:
            return "Discount is 10%"
        else:
            return "Discount is 5%"
s=laptop(a,b)
print(s.discount())
print(f"Instance is called {laptop.count1} times.")
while True:
    a=input("Again?: ")
    if a=="Yes":
        a=input("Enter Laptop Name: ")
        b=int(input("Enter Price: "))
        s=laptop(a,b)
        print(s.discount())
        print(f"Instance is called {laptop.count1} times.")
    else:
        break
        