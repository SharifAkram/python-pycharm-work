# A - Z = 65 - 90
# a - z = 97 - 122

norm_string = input("Enter a string to hide in uppercase : ")
secret_string = ""
for char in norm_string:
    secret_string += str(ord(char))
print("Secret Message :", secret_string)
norm_string = ""
for i in range(0, len(secret_string)-1, 2):
    char_code = secret_string[i] + secret_string[i+1]
    norm_string += chr(int(char_code))
print("Original Message :", norm_string)
