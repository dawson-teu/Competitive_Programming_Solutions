def get_user_input(error_message, valid_responses):
    user_input = input()
    while user_input not in valid_responses:
        print(error_message)
        user_input = input()
    return user_input


def get_user_num():
    num = input()
    while not is_number(num):
        print("Please enter a valid number.")
        num = input()
    num = float(num)
    return num


def is_number(num):
    if len(num) == 0:
        return False
    if num[0] == "-":
        num = num[1:]
    if "." in num and len(num.split(".")) == 2:
        part1, part2 = num.split(".")
        return part1.isnumeric() and part2.isnumeric()
    return num.isnumeric()


print("Do you want to use the calculator?")
user_use = get_user_input("Please enter yes or no.", ["yes", "no"])
while user_use == "yes":
    print("Please enter the first number:")
    num1 = get_user_num()

    print("Please enter the second number:")
    num2 = get_user_num()

    print("Please enter the operation you want to use:")
    operation = get_user_input("Please enter a valid operation.", ["+", "-", "*", "/"])

    answer = None
    if operation == "+":
        answer = num1 + num2
    elif operation == "-":
        answer = num1 - num2
    elif operation == "*":
        answer = num1 * num2
    elif operation == "/":
        if num2 == 0:
            print("Division by zero results in an error. Please try again.")
        else:
            answer = num1 / num2
    if answer:
        print("The answer is: " + str(answer))

    print("Do you want to use the calculator again?")
    user_use = get_user_input("Please enter yes or no.", ["yes", "no"])
print("Thank you for using the calculator. Goodbye!")
