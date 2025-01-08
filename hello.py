print("Hello, World!")

import time

a_string = "HELLO YERS which integer here is a positive number?"
print(a_string)

# Request integers from the user
variable1 = int(input("Please enter the first integer: "))
variable2 = int(input("Please enter the second integer & note that next request will be with No prompt string included: "))
# Delay before requesting variable3
time.sleep(2)
print("in Mickey's voice: Well, I am waiting for yor f*cking response...")
variable3 = int(input()) # No prompt string included

a_list = [1, 2, 3, variable1, variable2, variable3]
print(a_list)

for item in a_list:
    if item == 45:
        print(f"{item} is for MARIIOO")
    elif item > 0:
        print(f"{item} is positive")
    elif item < 0:
        print(f"{item} is negative")
    else:
        print(f"{item} is zero")
print("Вот как-то так...)")