"""
WalmartDelivery

Description:
"""

import random
import tsapp
window = tsapp
answer = ("y/n ")


## storing a list of ingredients/emails and ids ##
random_ingredients = ["milk","hot pockets", "cheese","cookies","ice tea","pickels"] #
emails = ["ilovetacos@gmail.com","kwya12127@gmail.com","pst12@gmail.com","loco2012@gmail.com","kidsplay@gmail.com"]
order_ids = [451932,318746,506472,864527,294813]

prices = [5, 4, 7, 8, 2, 6]

# adding up all the prices
cart = list(random_ingredients)
cart_prices = [5, 4, 7, 8, 2, 6]


for i in range (6):
    print(random_ingredients[i], "$", prices[i])


## where the user put there id/email##
print("Welcome to walmart delivey, what can i help you with?")
email = input("Please enter your email address ")
order_id = int(input("Please enter your order number "))


## checking to see if their email is in the list ##
if email  in emails:
    ## get the postion of the users email ## 
    email_index = emails.index(email)
    
    ## checking to see if their order id is in the list ##
    if order_id in order_ids:
        ## get the postion of the order id ##
        order_id_index = order_ids.index(order_id)
        ## check to see if the postion of the email and id are the same ##
        if order_id_index == email_index:

            ##if they are the same the user will see their tracking number ##
            ## where the user will see there tracking order ##
            print("----------------------------")
            print("Here's your tracking order")
            print("order number " + str(order_id))
            ## if the user order id doesn't match with email ##
        else:
            print("Sorry your order id doesn't match with your email")
    else:
        print("Invaild order id")
else:
    answer = input("Would you like to create an account y/n ")
    
    ## if the user doesn't have a email they can make one ##
    if answer.lower() == 'y':
           email = input("enter your new email ")
           emails.append(email)
        ## The user will be given a random order id ##
           order_id = random.randint(100000, 999999)
           print("Thank you for making an account here's your order id " + str(order_id))
           order_ids.append(order_id)
            ## if the user types n then the program ends ##
    elif answer.lower() == 'n':
        print("Have a good day, see ya")