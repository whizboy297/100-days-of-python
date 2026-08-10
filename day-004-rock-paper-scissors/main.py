# Randomisation and Python List 
#Random Module
import random
import my_module



#  randint() function returns a random integer between the two integers passed as arguments.
 

randdom_integer= random.randint(1, 10)  # returns a random integer between 1 and 10
print(randdom_integer) 

print(my_module.my_favorite_number)  # Accessing the variable my_favorite_number from my_module

#  random() function returns a random float between 0.0 to 1.0 
random_0_to_1= random.random()  # returns a random float between 0.0 to 1.0
print(random_0_to_1)

random_float= random.uniform(1, 10)  # returns a random float between 1 and 10
print(random_float)

 # Create a program that ptints out Heads or Tails randomly
random_heads_or_tails= random.randint(0, 1)  # returns a random integer between 0 and 1
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails") 



#Python List
# A list is a collection which is ordered and changeable. In Python lists are written with square brackets.
fruits = ["Apple", "Banana", "Cherry"]
print(fruits)  # prints the entire list


states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut"]
print(states_of_america)  # prints the entire list



list_of_places = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
print(list_of_places[0])  # prints the first item in the list





states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut"]
print(states_of_america[1])  # prints the second item in the list
states_of_america[1] = "Pencilvania"  # modifies the second item to "Pencilvania"
print(states_of_america)  # prints the modified list

#add to the list
states_of_america.append("New State")  # adds "New State" to the end
print(states_of_america)  # prints the modified list

#remove from the list
states_of_america.remove("New State")  # removes "New State" from the list
print(states_of_america)  # prints the modified list

#extend the list
states_of_america.extend(["New State 3", "New State 4"])  # adds "New State 1" and "New State 2" to the end of the list
print(states_of_america)  # prints the modified list

 # Who will pay the bill program
friends = ["Alice", "Bob", "Charlie", "David"]
random_friend = random.choice(friends)  # randomly selects a friend from the list
print(f"{random_friend} will pay the bill!")  # prints the selected friend 

friends = ["Alice", "Bob", "Charlie", "David"]
random_index = random.randint(0, len(friends) - 1)  # generates a random index
random_friend = friends[random_index]  # selects a friend using the random index
print(f"{random_friend} will pay the bill!")  # prints the selected friend


#Inex Error
# If you try to access an index that is out of range, you will get an IndexError. For example, if you try to access the 5th item in a list that only has 4 items, you will get an IndexError. To avoid this, you can use the len() function to get the length of the list and use that to generate a random index. For example, if you have a list of 4 items, you can use random.randint(0, 3) to generate a valid index.

states_of_Nigeria = ["Lagos", "Abuja", "Kano", "Kaduna", "Rivers"]
print(states_of_Nigeria[random.randint(0, len(states_of_Nigeria) - 1)])  # prints a random item from the list

#nested list
# A nested list is a list that contains other lists as its elements. For example, a list of lists can be used to represent a matrix or a grid. You can access the elements of a nested list by using multiple indices. For example, if you have a list of lists called "


fruits = ["Apple", "Banana", "Cherry"]
vegetables = ["Carrot", "Broccoli", "Spinach"]
dirty_dozen = [fruits, vegetables]  # creates a nested list
print(dirty_dozen)  # prints the entire nested list
print(dirty_dozen[0])
print(dirty_dozen[1])

print(dirty_dozen[1][2])
print(dirty_dozen[1][1])

#Project Rock Paper Scissors

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer_choice = random.randint(0, 2)
choices = [rock, paper, scissors]

#if user_choice == 0:
#   print(choices[0])
#elif user_choice == 1:
#    print(choices[1])
#else:
#    print(choices[2])
print(choices[user_choice])

if user_choice == computer_choice:
    print(f"Computer chose {choices[computer_choice]}. It's a draw!")
elif (user_choice == 0 and computer_choice == 2):
    print(f"Computer chose {choices[computer_choice]}. You win!")
elif (user_choice == 1 and computer_choice == 0):
    print(f"Computer chose {choices[computer_choice]}. You win!")
elif (user_choice == 2 and computer_choice == 1):
    print(f"Computer chose {choices[computer_choice]}. You win!")
else:
    print(f"Computer chose {choices[computer_choice]}. You lose!")

