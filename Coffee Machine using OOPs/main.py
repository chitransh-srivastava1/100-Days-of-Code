from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

items=Menu()
calculation=MoneyMachine()
coffee=CoffeeMaker()

turn_off=False

while not turn_off:
    choice= input(f"What do you like ({items.get_items()}) ").lower()

    if choice=="report":
        coffee.report()
        calculation.report()
    elif choice=="off":
        turn_off=True

    else:
        item_properties=items.find_drink(choice)
        if coffee.is_resource_sufficient(item_properties):
            if(item_properties!=None):
                has_sufficient_money=calculation.make_payment(item_properties.cost)
                if has_sufficient_money:
                    coffee.make_coffee(item_properties)