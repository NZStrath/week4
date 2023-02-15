import functions
import math

user_name = input("Hello! Please enter your full name.\n")
user_input = int(input("Please enter amount: \n"))

bill = functions.calculate_tax(user_input)

print(f"Your total bill is: KES {bill}.")
print(f"This is the floored bill: KES {math.floor(bill)}.")

functions.read_file(user_name)
functions.write_file(bill, user_name)
