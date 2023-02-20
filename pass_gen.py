import string
import random

def generate_password(min_length, special_char=True, numbers=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    all_char = letters + digits
    if special_char:
        all_char += special
    pwd = ""
    criteria = False
    has_nmb = False
    has_special = False

    while not criteria or len(pwd) < min_length: 
# OR because you keep going after min length if you don't have nmb or special
        new_char = random.choice(all_char)
        pwd += new_char

        if new_char in digits:
            has_nmb = True
        elif new_char in special:
            has_special = True

        criteria = True
        if numbers:
            criteria = has_nmb
        if special_char:
            criteria = criteria and has_special
    
    return pwd

min_length = int(input("Enter the minimum length: "))
has_special = input("Do you want to have special characters (y/n): ").lower() == "y" 
pwd = generate_password(min_length, has_special)
print(f"Your password: {pwd}")