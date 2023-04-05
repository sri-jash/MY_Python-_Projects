# TODO:2:Take user input

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
profit =0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def is_resource_sufficient(order_ingredients):
    """ Returns True when order can be made,False if ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item]>=resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coins():
    """ Returns the total calculated from coins entered"""
    print("please insert coins")
    total = int(input("how many quarters"))*0.25
    total += int(input("how many dimes"))*0.1
    total += int(input("how many nickles?:"))*0.05
    total += int(input("how many pennies?:"))*0.01
    return total



def is_transaction_Successfull(money_recieved,drink_cost):
    """ Return True when the payment is accepted, or False if money is insufficient"""
    if money_recieved>=drink_cost:
        change = round(money_recieved-drink_cost,2)
        print(f"Here is ${change} in change")
        global profit
        profit+=drink_cost
        return True
    else:
        print("Sorry That's not enough money.Money is refunded.")
        return False

def make_coffee(drink_name,order_ingredients):
    """ Deduct the required ingredients from the resources """
    for item in order_ingredients:
        resources[item] -=order_ingredients[item]
    print(f"here is yur {drink_name}☕☕")


#  TODO : 1.Print report of all coffee resources
turn_on = True
while True:
    choice=input("What would You Like to have?(espresso/latte/cappucino):")
    if  choice=="off":
        turn_on=False
    elif choice=="report":
        print(f"Water : {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"Coffee :{resources['coffee']}g")
        print(f"Money : ${profit}")
    else:
        drink=MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
        if is_transaction_Successfull(payment,drink['cost']):
            make_coffee(choice,drink['ingredients'])







