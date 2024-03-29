MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def turn_off():
    global state 
    state = 'off'
    return state

state = 'on'

def report():
    """
    prints list of resources in coffee machine
    """
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} ml")
    print(f"Money: ${resources['money']}")


def check_water(coffee_type):
    global resources
    global MENU
    return (resources['water'] > MENU[coffee_type]["ingredients"]['water']) 

def check_milk(coffee_type):
    global resources
    global MENU
    return (resources['milk'] > MENU[coffee_type]["ingredients"]['milk']) 

def check_coffee(coffee_type):
    global resources
    global MENU
    return (resources['coffee'] > MENU[coffee_type]["ingredients"]['coffee']) 

def calculate_money(quarters, dimes, nickles, pennies):
    return 0.25*quarters + 0.1*dimes + 0.05*nickles + 0.01*pennies

def calculate_change(money_inserted, coffee_type):
    return money_inserted - MENU[coffee_type]['cost']

report()


def make_coffee():
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ")
    
    #secret turn off machine
    if coffee_type == "off":
        turn_off()
        print("Shutting down coffee machine.")
        return
    
    #checking all resources and giving the user messages
    if coffee_type != "espresso":
        milk_available = check_milk(coffee_type)
    else:
        milk_available = True
    
    if not milk_available: 
        print("Sorry there is not enough milk. Exiting")
    
    water_available = check_water(coffee_type)
    if not water_available:
        print("Sorry there is not enough water. Exiting")

    coffee_available = check_coffee(coffee_type)
    if not coffee_available:
        print("Sorry there is not enough coffee. Exiting")

    if state == 'on':
        quarters = int(input("Please input number of quarters: "))
        dimes = int(input("Please input number of dimes: "))
        nickles = int(input("Please input number of nickles: "))
        pennies = int(input("Please input number of pennies: "))

        money_inserted = calculate_money(quarters, dimes, nickles, pennies)
        cost = MENU[coffee_type]['cost']

        if money_inserted < cost:
            print("Insufficient Money. Returning money inserted and exiting")
            return
        else:
            change = calculate_change(money_inserted, coffee_type)
            if coffee_type != "espresso":
                resources['milk'] -= MENU[coffee_type]["ingredients"]['milk']
            resources['coffee'] -= MENU[coffee_type]["ingredients"]['coffee']
            resources['water'] -= MENU[coffee_type]["ingredients"]['water']
            resources['money'] += cost
            print(f"Here is your {coffee_type}.")
            print(f"Here is ${change} dollars in change")

make_coffee()
report()