#lets build a robot barista
print("hello, welcome to dazai exist coffee!!!!!!!!!!!!!!!!!")
name = input("what is your good name?\n")
if name == "sujata" or name == "rock" or name == "loki":
    evil_status=input("are you evil?(yes/no)\n")
    good_deeds=int(input("how many good deeds did you do today\n"))
    if evil_status == "yes" and good_deeds < 4:
        print("evil people are not welcome here " + name + "!!!\nget lost!")
        exit()       
    else:
        print("ohh! so you are one of those non evil " + name + (" get in!"))
print("\nhello!! " + name + " thankyou so much for coming in today!:)\n\n")
menu = "black coffee, latte, cappucino, cold coffee, espresso, frappuccino "
order = input(name +",what would you like from our menu today, we are serving\n"+ menu +"\n\n")
if order == "black coffee":
    price = 3
elif order.lower() == "latte":
    price = 5
elif order.lower() == "cappucino":
    price = 5
elif order.lower() == "cold coffee":
    price = 6
elif order.lower() == "espresso":
    price = 7
elif order.lower() == "frappuccino":
    price = 10
else:
    print("\nSorry we don't serve that here!!!")
    exit()
    
quantity = input(name +" how many coffee would you like?\n")
total = price * int(quantity)
print ("\nthankyou, your total will be: $" + str(total))
print("\n\nsounds good " + name + " we will have that " +str(quantity)+" "+ order + " ready for you in a moment.")
