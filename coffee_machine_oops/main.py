from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = CoffeeMaker()
money = MoneyMachine()
coffee_menu = Menu()

user_choice = input("What is your drink? espresso/cappuccino/latte? ")
print(coffee_menu.find_drink(user_choice))
print(coffee.is_resource_sufficient(user_choice))