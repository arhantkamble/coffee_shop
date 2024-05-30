# coffee_shop
#A ROBOT BARISTA

    print("hello, welcome to dazai exist coffee!!!!!!!!!!!!!!!!!")
    name = input("what is your good name?\n")
    blocked = ("rock")
    if name == blocked:
    evil_status=input("are you evil?")
    
        if input == "yes":
            print("evil people are not welcome here!!!")
            exit()        
    else:
        print("hello!! " + name + " thankyou so much for coming in today!:)\n\n\n")
    menu = "black coffee, latte, cappucino, cold coffee, espresso "
    order = input(name +",what would you like from our menu today, we are serving\n"+ menu +"\n\n")
    if order != menu:
        print("sorry!! "+order+" is not served here")
    else:
        price = 8
    quantity = input(name +" how many coffee would you like?\n")
    total = price * int(quantity)
    print ("thankyou, your total will be: $" + str(total))
    print("\n\nsounds good " + name + " we will have that " +str(quantity)+" "+ order + " ready for you in a moment.")
