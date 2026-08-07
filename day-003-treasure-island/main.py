#Conditional Statements: if, else, elif 
 # if condition:
#     do something
# else:
#     do something else

# elif condition:
#     do something else

# For example:
water_level = 5
if water_level > 80:
    print("Drain water!")
else:
    print("Continue monitoring water level.")


height = 120
if height >= 120:
    print("You can ride the roller coaster!")
else:
    print("You are not tall enough to ride the roller coaster.")


print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the roller coaster!")
else:
    print("You are not tall enough to ride the roller coaster.")

# Comparison Operators: >, <, >=, <=, ==, !=

#Modulo Operator: % (returns the remainder of a division)
print(10 % 3)  # Output: 1

print("This is to check if a number is even or odd.")
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")

#Nested if statements
print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("What is your age? "))
    if age <= 18:
        print("You need to pay $7 for the ride.")
    else:
        print("You need to pay $12 for the ride.") 
else:
        print("Enjoy the ride!")



#elif statements
print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age >= 12 and age <= 18:
        bill = 7
        print("Youth tickets are $7.")

    elif age >= 45 and age <= 55:
        bill = 0
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12    
        print("Adult tickets are $12.")
    wants_photo = input("Do you want a photo taken? Type Y for Yes or N for No. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}.")
    

else:
    print("You are not tall enough to ride the roller coaster.")


#Python Pizza Delivery Program
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
else:
    bill = 25  
if pepperoni == "Y":
    if size == "S":
        bill += 2
    if size == "M":
        bill += 4
    else:
        bill += 8
if extra_cheese == "Y":
    if size == "S":
        bill += 2
    if size == "M":
        bill += 4
    else:
        bill += 8
print(f"Your final bill is ${bill}.")

#Logical Operators: and, or, not
# and operator: True if both conditions are true
# or operator: True if at least one condition is true
# not operator: True if the condition is false

#Treasure Island Game
print("Welcome to Treasure Island.\nYour Mission Is to find the Treasure.")
Direction = input("You are at a cross road. Where do you want to go? Type 'left' or 'right': ")
if Direction == "left":
    Action = input("You have come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across: ")
    if Action == "wait":
        Door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ")
        if Door == "red":
            print("It's a room full of fire. Game Over.")
        elif Door == "yellow":
            print("You found the treasure! You Win!")
        elif Door == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
