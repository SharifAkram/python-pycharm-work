# and, or, not

age = int(input("Enter Age: "))
if(age >= 1) and (age <= 18):
    print("Important Birthday")
elif(age == 21) or (age == 50):
    print("Important Birthday")
elif not age < 65:
    print("Important Birthday")
else:
    print("Sorry, Not Important Birthday")

# what grade someone should go to based on age

age = int(input("Enter Age: "))
if age < 5:
    print("Too Young For School")
elif age == 5:
    print("Go To Kindergarten")
elif (age > 5) and (age <= 17):
    grade = age - 5
    print("Go To Grade {}".format(grade))
else:
    print("Go To College")

