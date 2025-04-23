from foodItem import FoodItem
from menu import Menu
from orders import Order
from restaurant import Restaurant
from users import Customer,Employee,Admin

kfc = Restaurant('KFC')

def customer_menu():
    name = input('Enter your Name: ')
    email = input('Enter your Email: ')
    phone = input('Enter your Phone: ')
    address = input('Enter your Address: ')

    customer = Customer(name=name,email=email,phone=phone,address=address)

    while True:
        print(f'Welcome {customer.name}!!!')
        print('1. View Menu')
        print('2. Add item to cart')
        print('3. View cart')
        print('4. Pay Bill')
        print('5. Exit')

        choice = int(input('Enter your choice: '))

        if choice == 1:
            customer.view_menu(kfc)

        elif choice == 2:
            item_name = input('Enter item name: ')
            quantity = int(input('Enter item quantity: '))

            customer.add_to_cart(kfc,item_name,quantity)
        elif choice == 3:
            customer.view_cart()
        
        elif choice == 4:
            customer.pay_bill()

        elif choice == 5:
            break

        else:
            print('Invalid choice!')


def admin_menu():
    name = input('Enter your Name: ')
    email = input('Enter your Email: ')
    phone = input('Enter your Phone: ')
    address = input('Enter your Address: ')

    admin = Admin(name=name,email=email,phone=phone,address=address)

    print(f'Welcome {admin.name}!!!')
    while True:
        print('1. Add New Item')
        print('2. Add New Employee')
        print('3. View Employees')
        print('4. View Items')
        print('5. Delete Item')
        print('6. Exit')

        choice = int(input('Enter your choice: '))

        if choice == 1:
            name = input('Enter Item Name: ')
            price = int(input('Enter Item Price: '))
            quantity = int(input('Enter Item Quantity: '))

            item = FoodItem(name=name,price=price,quantity=quantity)
            admin.add_menu_item(kfc,item)

        elif choice == 2:
            name = input('Enter Employee name: ')
            email = input('Enter Employee email: ')
            phone = input('Enter Employee phone: ')
            address = input('Enter Employee address: ')
            age = input('Enter Employee age: ')
            salary = input('Enter Employee salary: ')
            designation = input('Enter Employee designation: ')

            employee = Employee(name=name,email=email,address=address,phone=phone,age=age,designation=designation,salary=salary)            
            admin.add_employee(kfc,employee)

        elif choice == 3:
            admin.view_employee(kfc)
        
        elif choice == 4:
            admin.view_item(kfc)
            
        elif choice == 5:
            item_name = input('Enter Item name you want to delete: ')
            admin.remove_item(kfc,item_name)

        elif choice == 6:
            break

        else:
            print('Invalid choice!')


while True:
    print('---Welcome---')
    print('1. Customer')
    print('2. Admin')
    print('3. Exit')

    choice = int(input('Enter your choice: '))

    if choice == 1:
        customer_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break
    else:
        print('Invalid input!')

