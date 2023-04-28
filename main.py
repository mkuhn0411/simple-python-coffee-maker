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

coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01
}

profit = 0

def print_resources():
    for item in resources:
        unit = "g" if item.lower() == "coffee" else "ml"
        print(f"{item}: {resources[item]}{unit}")
    print(f"Profit: ${'{:.2f}'.format(round(profit))}")


def get_money(item, item_cost):
    paid = 0

    while paid < item_cost:
        if paid > 0:
            rounded_paid = '{:.2f}'.format(round(paid, 2))
            rounded_remainder = '{:.2f}'.format(round(item_cost - paid, 2))
            print(f"You did not pay enough. You paid ${rounded_paid} but it costs ${'{:.2f}'.format(round(item_cost))}. Please pay ${rounded_remainder} more.")
        for coin in coins:
            amount_coin = int(input(f"How many {coin}?: "))
            paid += amount_coin * coins[coin]

    if paid > item_cost:
        change = '{:.2f}'.format(round(paid - item_cost, 2))
        print(f"Your change is ${change}")
        return
    elif paid == item_cost:
        print("No change here! Thanks for paying.")
        return


def use_resources(item):
    item_resources = MENU[item]["ingredients"]

    for resource in item_resources:
        resources[resource] -= item_resources[resource]


def check_can_make(item):
    ingredients_needed = MENU[item]["ingredients"]

    for ingredient in ingredients_needed:
        if ingredients_needed[ingredient] > resources[ingredient]:
            return False
    return True


def make_coffee(item, cost):
    global profit
    profit += cost
    use_resources(item)
    return

def handle_initial_ask():
    user_input = input("What would you like? (expresso/latte/cappuccino): ").lower()

    if user_input == "report":
        print_resources()
        return
    elif user_input == "off":
        return "shut off"
    elif user_input in MENU:
        can_make = check_can_make(user_input)
        if can_make:
            cost = MENU[user_input]["cost"]
            print(f"Great! The cost of a {user_input} is ${'{:.2f}'.format(round(cost))}. Please pay me.")
            get_money(user_input, cost)
            make_coffee(user_input, cost)
            return user_input
        else:
            print("Sorry, we do not have enough ingredients to make this. Please try again later")
            return


def run():
    machine_on = True

    while machine_on:
        item = handle_initial_ask()
        if item == "shut off":
            machine_on = False

        item and print(f"{item} ☕️ is ready! Please enjoy")

    print("Machine has been shut off for maintenance")


run()