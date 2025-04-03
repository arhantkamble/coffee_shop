import time

print("Hello, welcome to Dazai Exist Coffee! ☕")
name = input("What is your good name?
")

evil_customers = ["ujwal", "arhant", "om"]
if name.lower() in evil_customers:
    evil_status = input("Are you evil? (yes/no)
").strip().lower()
    good_deeds = input("How many good deeds did you do today?
").strip()
    
    while not good_deeds.isdigit():
        print("Please enter a valid number!")
        good_deeds = input("How many good deeds did you do today?
").strip()
    
    if evil_status == "yes" and int(good_deeds) < 4:
        print(f"Evil people are not welcome here, {name}!!!\nGet lost!")
        exit()
    else:
        print(f"Oh! So you are one of those non-evil {name}s. Get in!")

print(f"\nHello, {name}! Thank you so much for coming in today! :)")

menu = {
    "black coffee": 3,
    "latte": 5,
    "cappuccino": 5,
    "cold coffee": 6,
    "espresso": 7,
    "frappuccino": 10
}

print("We are serving:")
for item in menu:
    print(f"- {item.title()} - ${menu[item]}")

order = input(f"\n{name}, what would you like from our menu today?
").strip().lower()

if order not in menu:
    print("\nSorry, we don't serve that here!")
    exit()

while True:
    quantity = input(f"{name}, how many {order}s would you like?
").strip()
    if quantity.isdigit():
        quantity = int(quantity)
        break
    print("Please enter a valid number!")

total = menu[order] * quantity
print(f"\nThank you, your total will be: ${total}")

time.sleep(2) 
print(f"\nSounds good, {name}! We will have your {quantity} {order}(s) ready for you in a moment. ☕")
