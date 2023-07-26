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
company_money = 0

def check_resources(coffee):
    water_needed = MENU[coffee]["ingredients"]["water"]
    if coffee=="espresso":
        milk_needed=0
    else:
        milk_needed = MENU[coffee]["ingredients"]["milk"]
    coffee_needed = MENU[coffee]["ingredients"]["coffee"]
    if water_needed > resources["water"] or milk_needed > resources["milk"] or coffee_needed > resources["coffee"]:
        return False
    else:
        return True

def check_money(coffee,pay):
   amount_needed = MENU[coffee]["cost"]
   if amount_needed > pay:
       return False
   else:
       return True

def make_coffee(coffee):
    water_needed = MENU[coffee]["ingredients"]["water"]
    if coffee=="espresso":
        milk_needed=0
    else:
        milk_needed = MENU[coffee]["ingredients"]["milk"]
    coffee_needed = MENU[coffee]["ingredients"]["coffee"]
    amount_needed = MENU[coffee]["cost"]
    if check_resources(coffee):
        print("Please insert coins. ")
        while True:
            try:
                quarters = float(input("How many quarters? "))
                dimes = float(input("How many dimes? "))
                nickles = float(input("How many nickels? "))
                penny = float(input("How many pennies? "))
                break
            except:
                print("Wrong input! Please enter a digit. ")
        total_money=(quarters*0.25)+(dimes*0.1)+(nickles*0.05)+(penny*0.01)
        if check_money(coffee,total_money):
            if total_money>amount_needed:
                bal = total_money-amount_needed
                bal = round(bal, 2)
                print(f"Here's your change ${bal}")
                print(f"Here's your {coffee} ☕️, enjoy!")
            else:
                print("You don't have a change.")
                print(f"Here's your {coffee} ☕️, enjoy!")
            global company_money
            company_money += amount_needed
            resources["water"]-= water_needed
            resources["milk"]-=milk_needed
            resources["coffee"]-=coffee_needed
        else:
            print("Insufficient funds for the coffee choice!")
            print("Your money has been refunded.")
    else:
        print("There's not enough Water or Milk or Coffee for the choice you made.")
    return resources

while True:
    choice_list =["espresso", "cappuccino", "latte", "report", "q"]
    choose=0
    while choose not in choice_list:
        choose = input("What would you like? Coffee >> 'espresso' / 'cappuccino' / 'latte' OR 'report': Press 'q' to quit: ").lower()

    if choose=="report":
        print(f""" \twater: {resources["water"]}ml
        \tmilk: {resources["milk"]}ml
        \tcoffee: {resources["coffee"]}mg
        \tmoney: ${company_money}
        """)
    elif choose=="q":
        break
    else:
        make_coffee(choose)