#####
def money_deposit(sum):
    print("Please insert coins.")
    quarters = int(input("how many quarters?: ")) * 0.25
    dimes = int(input("how many dimes?: ")) * 0.1
    nickles = int(input("how many nickles?: ")) * 0.05
    pennies = int(input("how many pennies?: ")) * 0.01
    sum = quarters + dimes + nickles + pennies
    
    return sum
####
#Initial Ingredient Quantity Placed in the Machine
default_water = 300
default_milk = 200
default_coffee = 100
default_money = 0

main_loop = True
while main_loop == True:
    customer = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # to check the report of the current state of the machine
    if customer == "report":
        print(f"Water: {default_water}ml")
        print(f"Milk: {default_milk}ml")
        print(f"Coffee: {default_coffee}g")
        print(f"Money: ${default_money}")
    # to switch of the machine  
    elif customer == "off":
        main_loop = False 
    
    elif customer == "espresso" or customer == "latte" or customer == "cappuccino":
        var = money_deposit(sum)
        # the total_deposit should remain in 1 d.p in order to meet
        # cappuccino's if condition, after which we need to type-cast
        # to convert it from str to float
        total_deposit = "%.1f" % (var)
        total_deposit = float(total_deposit)
        # the change should be rounded up to 2 d.p
        esp_change = round(total_deposit - 1.5, 2)
        lat_change = round(total_deposit - 2.5, 2)
        cap_change = round(total_deposit - 3.0, 2)

        #MONEY REFUNDED
        if customer=="espresso" and total_deposit < 1.5:
                print("Sorry that's not enough money. Money refunded")
        if customer=="latte" and total_deposit < 2.5:
                print("Sorry that's not enough money. Money refunded")
        if customer=="cappuccino" and total_deposit < 3.0:
                print("Sorry that's not enough money. Money refunded")
        ##
        
        if customer=="espresso" and total_deposit == 1.5:
            if default_water < 50 or default_coffee < 18:
                print("Sorry there is not enough ingredient needed to make espresso.")
            else:
                print(f"Here is ${0.00} in change.\nHere is your espresso. Enjoy!☕")
                default_water -= 50
                default_coffee -= 18
                default_money += total_deposit
        if customer=="espresso" and total_deposit > 1.5:
            if default_water < 50 or default_coffee < 18:
                print("Sorry there is not enough ingredient needed to make espresso.")
            else:
                print(f"Here is ${esp_change} in change.\nHere is your espresso. Enjoy!☕")
                default_water -= 50
                default_coffee -= 18
                default_money += (total_deposit - esp_change)
            
        if customer == "latte" and total_deposit == 2.5:
            if default_water < 200 or default_coffee < 24 or default_milk < 150:
                print("Sorry there is not enough ingredient needed to make latte.")
            else:
                print(f"Here is ${0.00} in change.\nHere is your latte. Enjoy!☕")
                default_water -= 200
                default_coffee -= 24
                default_milk -= 150
                default_money += total_deposit
        if customer=="latte" and total_deposit > 2.5: 
            if default_water < 200 or default_coffee < 24 or default_milk < 150:
                print("Sorry there is not enough ingredient needed to make latte.")
            else: 
                print(f"Here is ${lat_change} in change.\nHere is your latte. Enjoy!☕")
                default_water -= 200
                default_coffee -= 24
                default_milk -= 150
                default_money += (total_deposit - lat_change)
            
        if customer == "cappuccino" and total_deposit == 3.0:
            if default_water < 250 or default_coffee < 24 or default_milk < 100:
                print("Sorry there is not enough ingredient needed to make cappuccino.")
            else:
                print(f"Here is ${0.00} in change.\nHere is your cappuccino. Enjoy!☕")
                default_water -= 250
                default_coffee -= 24
                default_milk -= 100
                default_money += total_deposit
        if customer == "cappuccino" and total_deposit > 3.0: 
            if default_water < 250 or default_coffee < 24 or default_milk < 100:
                print("Sorry there is not enough ingredient needed to make cappuccino.")
            else:
                print(f"Here is ${cap_change} in change.\nHere is your cappuccino. Enjoy!☕")
                default_water -= 250
                default_coffee -= 24
                default_milk -= 100
                default_money += (total_deposit - cap_change)