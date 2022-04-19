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
}

money = 0


def check_resources(a):
    for x in MENU[a]["ingredients"]:
        if MENU[a]["ingredients"][x] > resources[x]:
            print(f"Sorry. There is not enough {x}.")
            return False
        else:
            return True


def coffee(a):
    print(f"Here is your {a} ☕️. Enjoy!")
    for x in MENU[a]["ingredients"]:
        resources[x] -= MENU[a]["ingredients"][x]


def report():
    print(f"water: {resources['water']}ml")
    print(f"milk: {resources['milk']}ml")
    print(f"coffee: {resources['coffee']}g")
    print(f"money: ${money}")



on = True

while on:
    continuing = True

    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "report":
        report()
        continuing = False

    elif choice == "off":
        on = False
        continuing = False


    if continuing:
        continuing=check_resources(choice)

    if continuing:
        coins: float = 0
        print('Please insert coins')
        coins += 0.25 * int(input("how many quarters?: "))
        coins += 0.1 * int(input("how many dimes?: "))
        coins += 0.05 * int(input("how many nickles?: "))
        coins += 0.01 * int(input("how many pennies?: "))


        if coins >= MENU[choice]["cost"]:
            money += MENU[choice]["cost"]
            if coins > MENU[choice]["cost"]:
                refund = coins - MENU[choice]["cost"]
                print(f"Here is ${refund} in change.")
        else:
            print("Sorry. That's not enough money. Money refunded.")
            continuing = False

        if continuing:
            coffee(choice)

