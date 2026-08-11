#Loops in Python are used to execute a block of code repeatedly until a certain condition is met. 
# There are two main types of loops in Python: the "for" loop and the "while" loop.
#For Loop: A "for" loop is used to iterate over a sequence (such as a list, tuple, or string) and execute a block of code for each item in the sequence. 
# The syntax for a "for" loop is as follows:
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    print(fruit + "Pie")

places = ["New York", "Paris", "Tokyo", "Sydney", "London"]
for place in places:
    print(place)
    print("I would love to visit " + place + " someday!")



#Highest Score
student_scores = [70, 85, 90, 78, 92, 88, 95, 80, 89, 91, 87, 93, 84, 76, 82]
total_score = sum(student_scores)
print("The total score of all students is:", total_score)

#or 
sum = 0
for score in student_scores:
    sum += score
print("The total score of all students is:", sum)

#Maximum Score
max_score = max(student_scores)
print("The highest score among the students is:", max_score)

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print("The highest score among the students is:", highest_score)

# For Loop with Range: The "range()" function is often used in conjunction with a "for" loop to generate a sequence of numbers.
# The syntax for a "for" loop with "range()" is as follows:
for i in range(5):
    print(i)  # This will print numbers from 0 to 4
sum = 0
for number in range(1, 101):
    print(number)  # This will print numbers from 1 to 100
    sum += number
print("The sum of numbers from 1 to 100 is:", sum) 

#Password Generator

import random
print("Welcome to the Password Generator!")
input_letters = int(input("How many letters would you like in your password?\n"))
input_symbols = int(input("How many symbols would you like?\n"))
input_numbers = int(input("How many numbers would you like?\n"))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

letter_list = []
for letter in range(input_letters):
    letter_list.append(random.choice(letters))

symbol_list = []
for symbol in range(input_symbols):
    symbol_list.append(random.choice(symbols))


number_list = []
for number in range(input_numbers):
    number_list.append(random.choice(numbers))  


generated_password = letter_list + symbol_list + number_list
random.shuffle(generated_password)
print("Your generated password is: " + "".join(generated_password)) 


#Easy Level
password = ""
for char in range(1, input_letters + 1):
    password += random.choice(letters)
for char in range(1, input_symbols + 1):
    password += random.choice(symbols)
for char in range(1, input_numbers + 1):
    password += random.choice(numbers)
print("Your generated password is: " + password)

