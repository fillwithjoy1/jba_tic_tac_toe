# put your python code here
first_number = float(input())
second_number = float(input())
operation = input()

if operation == "+":
    print(first_number + second_number)
elif operation == "-":
    print(first_number - second_number)
elif operation == "*":
    print(first_number * second_number)
elif operation == "/" and second_number:
    print(first_number / second_number)
elif operation == "mod" and second_number:
    print(first_number % second_number)
elif operation == "pow":
    print(first_number ** second_number)
elif operation == "div" and second_number:
    print(first_number // second_number)
else:
    print('Division by 0!')
