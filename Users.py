from abc import ABC,abstractmethod
class User(ABC):
    def __init__(self,name,phone,email,address) -> None:
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address

class Customer(User):
    def __init__(self, name,phone,email,address,money) -> None:
        self.wallet=money
        self.__order=None
        self.due_amount=0
        super().__init__(name,phone,email,address)

    @property
    def order(self):
        return self.__order
    
    @order.setter
    def order(self,order):
        self.__order=order

    def place_order(self,order):
        self.order=order
        self.due_bill +=order.bill
        print(f'{self.name} placed an order with bill {order.bill}')
    
    def eat_food(self,order):
        print(f'{self.name} eat food {order.items}')

    def pay_for_order(self,amount):
        pass

    def give_tips(self,tips_amount):
        pass
    def write_review(self,stars):
        pass

class Employee(User):
    def __init__(self, name, phone, email, address,salary,starting_date,dept) -> None:
        super().__init__(name, phone, email, address)
        self.salary=salary
        self.due=salary
        self.starting_date=starting_date
        self.dept=dept

    def receive_salary(self):
        self.due=0

class Chef(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, dept,cooking_items) -> None:
        super().__init__(name, phone, email, address, salary, starting_date, dept)
        self.cooking_items=cooking_items

class Server(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, dept) -> None:
        self.tips_earning=0
        super().__init__(name, phone, email, address, salary, starting_date, dept)

    def take_order(self,order):
        pass
    def transfer_order(self,order):
        pass
    def serve_food(self,order):
        pass
    def receive_tips(self,amount):
        self.tips_earning +=amount

class Manager(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, dept) -> None:
        super().__init__(name, phone, email, address, salary, starting_date, dept)
