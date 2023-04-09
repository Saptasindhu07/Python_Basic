"""Write a Python class Restaurant with attributes like menu_items, book_table, and customer_orders, and methods like 
add_item_to_menu,book_tables, and customer_order.

Perform the following tasks now:
Now add items to the menu.
Make table reservations.
Take customer orders.
Print the menu.
Print table reservations.
Print customer orders."""

class restaurant:
    @classmethod 
    def func(cls):
        print("Welcome to restaurant: ")
    def __init__(self,book_table,customer_orders):
        self.book_table=book_table
        self.customer_orders=customer_orders
    def check(self,book_table):
        a=input(f"Is Table number {book_table} available? ")
        if a=="Yes":
            return True
        else:
            return False

print("Restaurant has tables 1-50: ")
print("Menu Items: ",["Dal","Roti","Chicken","Mutton","Fish","Desert"])
book_table=int(input("Enter Table number of choice: "))
customer_orders=input("Eneter customer orders: ").split()
b=restaurant(book_table,customer_orders)
while True:
    if b.check(book_table)==True:
        print("Table Reserved: ")
        break
    else:
        book_table=int(input("Please Try Again: "))
        pass
print(customer_orders)











