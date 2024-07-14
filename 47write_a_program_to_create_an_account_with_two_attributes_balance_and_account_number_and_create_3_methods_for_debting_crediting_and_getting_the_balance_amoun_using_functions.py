class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc
    def debit(self,amount):
        self.balance -= amount
        print("rs",amount,"is debited")
        print("the balance amount is",self.get_balance())
    def credit(self,amount):
        self.balance += amount
        print("rs",amount,"is credited")
        print("the balance amount is",self.get_balance())
    def get_balance(self):
        return self.balance
acc1=Account(10000,12345)
acc1.debit(1000)
acc1.credit(500)
60)write_a_program_to_find_the_sum_of_elements_in_the_list_using_function.py
def sum_numbers(list1):
    sum=0
    for i in list1:
        sum=sum+i
    return(sum)
print(sum([5,6,7,9,10]))
