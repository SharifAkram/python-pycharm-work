# triangle shape
print("   /|")
print("  / |")
print(" /  |")
print("/___|")

# variables
character_name = "Thomas"
character_age = "56"
print("There once was a man named " + character_name + ", ")
print("he was " + character_age + " years old.")

character_name = "Mike"
print("He really liked the name " + character_name + ",")
print("but didn't like being " + character_age + ".")

# strings
phrase = "Giraffe Academy"
print(phrase.replace("Giraffe", "Elephant"))

# working with numbers
print(2.0987)
print(-2.0987)
print(3 * 4.5)
print(3 * (4 + 5))
print(10 % 3)  # modulo operator

my_num = 5
print(str(my_num) + " = my favorite number")  # printing number next to string

# function = collection of code

my_num = -5
print(abs(my_num))  # absolute value

print(pow(4, 6))  # power
print(max(4, 6))  # maximum
print(min(4, 6))  # minimum
print(round(3.7))  # round up/round down

from math import *  # math module
print(floor(3.7))
print(ceil(3.7))
print(sqrt(36))
print(e)

# getting input from users
name = input("Enter Your Name: ")
age = input("Enter Your Age: ")
print("Hello " + name + "! You are " + age)

# building a basic calculator
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2) # integer (int) and float (decimals)

print(result)

# mad libs games
color = input("Enter a color: ")
plural_noun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity: ")

print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)

# lists - index begins at 0
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends[1] = "Mike"

print(friends[0])
print(friends[-1])  # index items from back of the list
print(friends[1:3])  # index items on list

# list functions
