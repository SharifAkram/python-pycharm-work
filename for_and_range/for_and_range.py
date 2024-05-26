"""
for i in [2, 4, 6, 8, 10]:
    print("1 =", i)

for i in range(2, 5):
    print("1 =", i)

i = 6
print("Is 6 Even :", ((i % 2) == 0))

for i in range(1, 21):
    if (i % 2) != 0:
        print("i =", i)

your_float = input("Enter a float : ")
your_float = float(your_float)
print("Rounded to 2 Decimals : {:.2f}".format(your_float))

"""

money = input("How much to invest : ")
interest_rate = input("Interest Rate : ")

money = float(money)
interest_rate = float(interest_rate) * .01

for i in range(10):
    money = money + (money * interest_rate)

print("Investment after 10 years : ${:.2f}".format(money))

