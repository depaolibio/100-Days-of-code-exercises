from platform import machine

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_on = True
coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

while machine_on == True:
    order_name = input(f"What would you like? {menu.get_items()}: ")
    if order_name == "report":
        coffee_maker.report()
        money_machine.report()
    elif order_name == "off":
        print("Machine is being turned off. Goodbye")
        machine_on = False
    else:
        drink = menu.find_drink(order_name)
        her2d = coffee_maker.is_resource_sufficient(drink) #her2d = have enough resources to make the drink
        if her2d == True:
            rich_enough = money_machine.make_payment(drink.cost)
            if rich_enough == True:
                coffee_maker.make_coffee(drink)
                coffee_maker.report()
                money_machine.report()
