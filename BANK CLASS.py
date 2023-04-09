""""Write a Python class BankAccount with attributes like account_number,
 balance, date_of_opening and customer_name, and methods like deposit,
 withdraw, and check_balance."""

class bank:
    def __init__(self,account_number,account_balance,date_of_opening):
        self.account_number=account_number
        self.account_balance=account_balance
        self.date_of_opening=date_of_opening
    @classmethod 
    def clas(cls,arg1):
        print(f"Hello {arg1} Welcome To Hapta National Bank: ")
    def deposit(self,deposit):
        new_deposit=self.account_balance+deposit
        print(f"New balance is {new_deposit}")
    def withdraw(self,withdraw):
        new_remaining=self.account_balance-withdraw
        print(f"New balance is {new_remaining}")
database={2345:
{"Name": "Toninho Takeo",
"Account Number": 2345,
"Date of opening":"01-01-2011",
"Balance":1000},
1234:{
"Name": "Astrid Rugile",
"Account Number": 1234,
"Date of opening":" 11-03-2011",
"Balance": 2000},
2312:{
"Name": "Orli Kerenza",
"Account Number": 2312,
"Date of opening": "12-01-2009",
"Balance": 3000},
1395:{
"Name": "Luciana Chika",
"Account Number": 1395,
"Date of opening": "01-01-2011",
"Balance": 3000},
6345:{
"Name": "Toninho Takeo",
"Account Number": 6345,
"Date of opening":" 01-05-2011",
"Balance": 4000},
1351:{
"Name":"Sukla Palit",
"Account Number":1351,
"Date of opening":"01-06-2010",
"Balance":50000
}
}
while True:
    acc_num=int(input("Enter Account Number: "))
    print(database[acc_num])
    k=bank(acc_num,database[acc_num]["Balance"],database[acc_num]["Date of opening"])
    add_=int(input("Enter balance deposited: "))
    k.deposit(add_)
    minus_=int(input("Enter balance withdrawn: : "))
    k.withdraw(minus_)
    
    
    
    
    
    
    