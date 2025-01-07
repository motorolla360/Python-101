print("Hello, World!")

a_string = "HELLO YERS which integer here is a positive number?"
print(a_string)

# Request integers from the user
variable1 = int(input("Please enter the first integer: "))
variable2 = int(input("Please enter the second integer & note that next request will be with No prompt string included: "))
variable3 = int(input()) # No prompt string included

a_list = [1, 2, 3, variable1, variable2, variable3]
print(a_list)

for listvar in a_list:
    if listvar > 0:
        print(f"{listvar} is positive")
    elif listvar < 0:
        print(f"{listvar} is negative")
    else:
        print(f"{listvar} is zero")
