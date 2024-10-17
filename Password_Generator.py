import random
import string

def generate_password(length,numbers=True,special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers :
         characters += digits
    if special_characters:
         characters += special

    password = ""
    satisfies_criteria = False
    has_number = False
    has_special = False

    while not satisfies_criteria or len(password) < length :
         new_char = random.choice(characters)
         password += new_char

         if new_char in digits:
              has_number = True
         elif new_char in special:
              has_special = True

         satisfies_criteria = True
         if numbers:
              satisfies_criteria = has_number
         if special_characters:
              satisfies_criteria = satisfies_criteria and has_special

    return password

length = int(input("Enter the length of password : "))
has_number = input("Do you want to have numbers (y/n)? = ").lower() == "y"
has_special = input("Do you want to have special characters(y/n)? = ").lower() == "y"



password = generate_password(10)
print("The Generated Password is: ",password)
            
         

