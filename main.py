from Menu import Pizza,Burger,Drinks,Menu
from Users import Chef,Manager,Server,Customer
from Restaurant import Restaurant
from Order import Order
def main():
    menu=Menu()
    pizza1=Pizza('Shutki pizza',500,['Fish','onion'],'large')
    menu.add_menu_item('pizza',pizza1)
    pizza2=Pizza('Chicken pizza',500,['Chicken','onion'],'large')
    menu.add_menu_item('pizza',pizza2)
    pizza3=Pizza('Mutton pizza',500,['Mutton','onion'],'large')
    menu.add_menu_item('pizza',pizza3)

    burger1=Burger('naga burger',200,'chicken',['bread','chicken','onion'])
    menu.add_menu_item('burger',burger1)
    burger2=Burger('mutton burger',300,'Mutton',['bread','Mutton','onion'])
    menu.add_menu_item('burger',burger2)
    
    coke=Drinks('Cocacola',50,True)
    menu.add_menu_item('drinks',coke)
    pepsi=Drinks('Pepsi',50,True)
    menu.add_menu_item('drinks',pepsi)
    coffee=Drinks('coffee',100,False)
    menu.add_menu_item('drinks',coffee)

    menu.show_menu()
    
    restaurant=Restaurant('Cui jhal',2000,menu)
    manager=Manager('Tushar',123,'tus@.com','Narsingdi',800,'2nd january','Food')
    restaurant.add_employee('manager',manager)
    chef=Chef('Rustom',1,'rus@','Dha',400,'1april','chef','Mutton')
    restaurant.add_employee('chef',chef)
    server=Server('A',2,'b@','N',200,'2 nd Feb','serve')
    restaurant.add_employee('server',server)

    restaurant.show_employees()
    #order for customer 1
    customer_1=Customer('T',123,'T@','Dha',2000)
    order_1=Order(customer_1,[pizza3,coffee])
    customer_1.pay_for_order(order_1)
    restaurant.add_order(order_1)
    restaurant.receive_payment(order_1,2000,customer_1)
    print('revenue and balance after 1st customer :',restaurant.revenue,restaurant.balance)

    #Order for customer 2
    customer_2=Customer('S',123,'S@','Dha',3000)
    order_2=Order(customer_2,[pizza3,coffee,burger2])
    customer_2.pay_for_order(order_2)
    restaurant.add_order(order_2)
    restaurant.receive_payment(order_2,2000,customer_2)
    print('revenue and balance after 2nd customer :',restaurant.revenue,restaurant.balance)

    #Order for customer 3
    customer_3=Customer('K',123,'K@','Dha',5000)
    order_3=Order(customer_3,[pizza3,coffee,burger2,coke,burger1,pizza2,pepsi])
    customer_3.pay_for_order(order_3)
    restaurant.add_order(order_3)
    restaurant.receive_payment(order_3,5000,customer_3)
    print('revenue and balance after 3nd customer :',restaurant.revenue,restaurant.balance)

    restaurant.pay_expense(restaurant.rent,'Rent')
    print('revenue and balance after rent :',restaurant.revenue,restaurant.balance,restaurant.expense)
    
    restaurant.pay_salary(chef)
    print('revenue and balance after giving salary :',restaurant.revenue,restaurant.balance,restaurant.expense)


if __name__ =='__main__':
    main()