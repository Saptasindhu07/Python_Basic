"""Write a Python class Inventory with attributes like item_id, item_name, stock_count, and price, and methods like add_item, update_item, and check_item_details.
Use a dictionary to store the item details, where the key is the item_id and the value is a dictionary containing the item_name, stock_count, and price"""
global d
d={}
class items:
    @classmethod 
    def greeting(cls):
        print("Hello There Welcome to Sapta Shop: ")
    def __init__(self,item_id,item_name,stock_count,price,d):
        self.item_id=item_id
        self.item_name=item_name
        self.stock_count=stock_count
        self.price=price
        self.d[self.item_id]={"Item Name":self.item_name,
                               "Item Count":self.stock_count,
                               "Price":self.price
                               }
    def check(self,char):
        return d[char]
    def add(self,key,value):
        x={key:value}
        d.update(x)
        return d
count=int(input("Enter number of values: "))
for i in range(0,count):
    a=int(input("Enter Product serial number: "))
    b=input("Enter product name: ")
    c=int(input("Enter stock count: "))
    k=int(input("input Price: "))
    e=items(a,b,c,k)
    print(e.d)
check_=input("Enter serial to check:" )
print(e.check(check_))





    