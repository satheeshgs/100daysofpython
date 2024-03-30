from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = CoffeeMaker()
money = MoneyMachine()
coffee_menu = Menu()

user_choice = input(f"What is your drink? {coffee_menu.get_items()} ")
if user_choice == 'report':
    coffee.report()
else:
    drink = coffee_menu.find_drink(user_choice) #user's choice of drink

    resource_check = coffee.is_resource_sufficient(drink)
    if not resource_check:
        print(resource_check)
    else:
        cost = drink.cost
        if money.make_payment(cost): 
            coffee.make_coffee(drink)
        coffee.report()