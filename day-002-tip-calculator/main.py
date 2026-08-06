# Data Types
#Learn about the different data types in Python. The most common data types are:
# Integers: Whole numbers, e.g., 1, 2, 3
# Floats: Decimal numbers, e.g., 1.5, 2.75
# Strings: Text, e.g., "Hello", "Python"    

# Subsriping: A string is a sequence of characters. You can access individual characters in a string using indexing. For example, if you have a string `s = "Hello"`, you can access the first character with `s[0]`, which will return 'H'.            

print("Hello"[4]) # This will print 'o' because indexing starts at 0    

#String Concatenation: You can combine strings using the `+` operator. For example, `"Hello" + " " + "World"` will result in `"Hello World"`
print("123" + "456") # This will print '123456'

#Integers = Whole numbers without a decimal point. You can perform arithmetic operations with integers, such as addition, subtraction, multiplication, and division.
print(123 + 456) # This will print 579

#Large Integers: Python can handle very large integers without any special syntax. For example, `12345678901234567890` is a valid integer in Python.    
print(12345678901234567890 + 1) # This will print 12345678901234567891

#Float = Numbers with a decimal point. You can perform arithmetic operations with floats as well. For example, `1.5 + 2.5` will result in `4.0`.
print(1.5 + 2.5) # This will print 4.0

#Boolean = A data type that can have one of two values: `True` or `False`. Booleans are often used in conditional statements and logical operations. For example, `5 > 3` will evaluate to `True`, while `2 == 3` will evaluate to `False`.
print(5 > 3) # This will print True

#len(12345) # This will raise an error because `len()` function is used to get the length of a sequence (like a string or list), and integers are not sequences.
print(len("Hello")) # This will print 5
#How to Print an integer with the `len()` function: You can convert the integer to a string first, and then use the `len()` function. For example, `len(str(12345))` will return 5.
print(len(str(12345))) # This will print 5

#How to know a data type of a variable: You can use the `type()` function to determine the data type of a variable. For example, `type(123)` will return `<class 'int'>`, while `type("Hello")` will return `<class 'str'>`.
print(type(123)) # This will print <class 'int'>
print(type("Hello")) # This will print <class 'str'>    

 #Print all the datatypes in Python in one single print statement: You can use the `type()` function along with a list of different data types to print them all in one statement. For example:
print(type(123), type(1.5), type("Hello"), type(True)) # This will print <class 'int'> <class 'float'> <class 'str'> <class 'bool'>

#Type Conversion: You can convert between different data types using built-in functions. For example, you can convert an integer to a float using `float()`, or a string to an integer using `int()`.
#Example of type conversion:
num_str = "123"
num_int = int(num_str) # Convert string to integer
print(num_int) # This will print 123    

#List of errors that can occur when working with data types in Python:
# TypeError: This error occurs when you try to perform an operation on incompatible data types.
# ValueError: This error occurs when you try to convert a value to a different data type    

print("Number of letters in our name is: " + str(len(input("What is your name? "))))        # This will print "Number of letters in our name is: 8"

#Mathematical Operations: You can perform various mathematical operations in Python, such as addition, subtraction, multiplication, division, and more. For example:
print(10 + 5) # This will print 15
print(10 - 5) # This will print 5
print(10 * 5) # This will print 50
print(10 / 5) # This will print 2.0
print(10 // 5) # This will print 2 (floor division)
print(10 % 5) # This will print 0 (modulo operation)
print(10 ** 2) # This will print 100 (exponentiation)

#PEMDASLR: Python follows the order of operations, also known as PEMDAS (Parentheses, Exponents, Multiplication and Division, Addition and Subtraction). For example, `2 + 3 * 4` will evaluate to `14`, not `20`, because multiplication is performed before addition.
print(2 + 3 * 4) # This will print 14   
print(3 * 3 + 3 / 3 - 3) # This will print 7.0 #why? This is because the expression inside the parentheses is evaluated first, resulting in `3 * 6 / 3 - 3`, which simplifies to `18 / 3 - 3`, and finally to `6 - 3`, which equals `3.0`.    

#Number Manipulation: You can manipulate numbers in Python using various built-in functions and methods. For example, you can round a float to a specific number of decimal places using the `round()` function, or you can use the `abs()` function to get the absolute value of a number.
#Example of number manipulation:
num = 3.14159
rounded_num = round(num, 2) # Round to 2 decimal places
print(rounded_num) # This will print 3.14   

# Assignment Operators: You can use assignment operators to assign values to variables. The most common assignment operator is `=`, which assigns the value on the right to the variable on the left. For example, `x = 5` assigns the value `5` to the variable `x`. You can also use compound assignment operators, such as `+=`, `-=`, `*=`, and `/=`, to perform an operation and assign the result to the same variable. For example, `x += 2` is equivalent to `x = x + 2`.
x = 5
x += 2 # This is equivalent to x = x + 2
print(x) # This will print 7

#F-Strings: F-strings are a way to format strings in Python. You can include variables and expressions inside an f-string by using curly braces `{}`. For example, `name = "Alice"; f"Hello, {name}!"` will result in `"Hello, Alice!"`.
name = "Alice"
age = 30
print(f"Hello, {name}! You are {age} years old.") # This will print "Hello, Alice! You are 30 years old."   

#Project : Tip Calculator
#In this project, you will create a simple tip calculator that takes the total bill amount and the tip percentage as input, and calculates the tip amount and the total amount to be paid.
#Example of a tip calculator:
# Get the total bill amount from the user
#total_bill = float(input("Enter the total bill amount: $"))
# Get the tip percentage from the user
#tip_percentage = float(input("Enter the tip percentage (e.g., 15 for 15%): "))
# Calculate the tip amount
#tip_amount = total_bill * (tip_percentage / 100)
# Calculate the total amount to be paid
#total_amount = total_bill + tip_amount
# Print the tip amount and the total amount to be paid
#print(f"Tip amount: ${tip_amount:.2f}")
#print(f"Total amount to be paid: ${total_amount:.2f}")  

print("Welcome to the Tip Calculator!")
# Get the total bill amount from the user
total_bill = float(input("What was the total bill?: $"))
# Get the tip percentage from the user
tip_percentage = int(input("How much Percentage tip would you like to give? 10, 12, or 15?: "))
# Calculate the tip amount
tip_amount = total_bill * (float(tip_percentage) / 100)
# Calculate the total amount to be paid
total_amount = total_bill + tip_amount
#How many people to split the bill with?
num_people = int(input("How many people to split the bill?: "))
#Calculate the amount each person should pay
amount_per_person = total_amount / float(num_people)
#Each person should pay
print(f"Each person should pay: ${amount_per_person:.2f}")





