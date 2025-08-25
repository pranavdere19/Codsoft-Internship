import random
import string

def generate_password(length):
    characters=string.ascii_letters+string.digits+string.punctuation

    password=''.join(random.choice(characters) for _ in range(length))
    return password

try:
    length = int(input("enter the desired password length:"))

    if length < 4:
        print("password length shouldbe at least 4 for better security")
    else:
        password= generate_password(length)
        print(f"Your Generated password: {password}")
except ValueError:
    print("Please enetr the valid number.")