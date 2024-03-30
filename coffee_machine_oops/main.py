from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = CoffeeMaker()
money = MoneyMachine()
coffee_menu = Menu()
is_on = True

while is_on:
    options = coffee_menu.get_items()
    user_choice = input(f"What is your drink? {options} ")
    if user_choice == 'off':
        is_on = False
    elif user_choice == 'report':
        coffee.report()
        money.report()
    else:
        drink = coffee_menu.find_drink(user_choice) #user's choice of drink
        cost = drink.cost
        if coffee.is_resource_sufficient(drink) and money.make_payment(cost): 
            coffee.make_coffee(drink)
        coffee.report()
        money.report()