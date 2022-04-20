from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()

coffee = CoffeeMaker()
money = MoneyMachine()

on = True

while on:

    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "report":
        coffee.report()
        money.report()

    elif choice == "off":
        on = False

    else:
        drink = menu.find_drink(choice)

        if coffee.is_resource_sufficient(drink):

            if money.make_payment(drink.cost):
                coffee.make_coffee(drink)

