from data import MENU, resources


# TODO: 1. function that prompts user and stores input
def is_client(profit):
    """Function decides if user is client eliminating wrong entries, maintenance and shutdown"""
    reply = input(f"What would you like ? (espresso/latte/cappuccino): ").lower()
    if reply in MENU or reply == "off":
        return reply  # keyword
    # TODO: 3. print report when input is report
    elif reply == "report":  # report case (no return index , case activated)
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
        return is_client(profit)
    else:  # recursion fail-safe (no return index , case activated)
        print("invalid answer")
        return is_client(profit)


# TODO: 4. check resources sufficient
def enough(drink):
    lactose = ["water", "milk", "coffee"]
    caffeine = ["water", "coffee"]
    if drink == "espresso":
        components = caffeine
    else:
        components = lactose
    for component in components:
        if resources[component] < MENU[drink]["ingredients"][component]:
            print(f"Sorry there is not enough {component}")
            return False
        else:
            return True


# TODO: 5.process coins function
def coins():
    """Prompts user to insert coins then calculate their monetary value"""
    print("please insert coins.")
    quarters = int(input("How many quarters ?: "))
    dimes = int(input("How many dimes ?: "))
    nickles = int(input("How many nickles ?: "))
    pennies = int(input("How many pennies ?: "))
    value = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    return value


# TODO: 6.check transaction
def transaction(choice, paid, profit):
    """compares paid value to selected drink"""  # paid value from coins() and selected drink from order()
    price = MENU[choice]['cost']
    if paid > price:
        change = round(paid - price, 2)
        print(f"Here is ${change} in change.")
        profit += price
        coffee(choice)
        return profit
    elif paid == price:
        profit += price
        coffee(choice)
        return profit
    else:
        print("Sorry that's not enough money. Money refunded.")


# TODO: 7.Make coffee
def coffee(choice):
    """This Function deducts drink ingredients from resources and prints drink message"""
    items = ["water", "milk", "coffee"]
    things = ["water", "coffee"]
    if choice == "espresso":
        for thing in things:
            if resources[thing] >= MENU[choice]["ingredients"][thing]:
                resources[thing] -= MENU[choice]["ingredients"][thing]
    else:
        for item in items:
            if resources[item] >= MENU[choice]["ingredients"][item]:
                resources[item] -= MENU[choice]["ingredients"][item]
    print(f"Here is your {choice} ☕. Enjoy!")


def machine():
    profit = 0
    running = True
    while running:
        choice = is_client(profit)
        # TODO: 2. Turn off input shuts down machine
        if choice == "off":
            running = False
        elif enough(choice):
            running = enough(choice)
            profit = transaction(choice, coins(), profit)


machine()

# print(order(profit))
# print(coins())
