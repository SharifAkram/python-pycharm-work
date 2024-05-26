import sys

my_age = 37
my_name = "Sharif"

print("Hello", my_name)

# Comment

'''
Multiline
Comment
'''

str_1 = "\"This is a quote\""

'''
Newline : \n
Backlash : \\
Single Quote : \'
Backspace : \b
Tab : \tcl
'''

print(sys.maxsize)

print(sys.float_info.max)

f1 = 1.1111111111111111
f2 = 1.1111111111111111
f3 = f1 + f2
print(f3)
# floats will be accurate to 15 digits

cn_1 = 5 + 6j
# complex number

can_vote = True
# boolean

my_age = 37
my_age = "dog"
# dynamically typed

print("Cast", type(int(5.4)))
print("Cast 2", type(str(5.4)))
print("Cast 3", type(chr(97)))
print("Cast 4", type(ord('a')))
print("Cast 5", type(float(2)))

age = 2
Age = 3
# variables are case sensitive

num_1 = "1"
num_2 = "2"
print("1 + 2 =", (int(num_1) + int(num_2)))
