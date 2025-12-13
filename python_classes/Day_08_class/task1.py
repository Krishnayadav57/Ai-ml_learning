def sum(num1, num2):
    return num1 + num2

def mul(num1, num2):
    return num1 * num2

def diff(num1, num2):
    return num1 - num2

def div(num1, num2):
    return num1 / num2


def main():
    num1 = float(input("Enter first number :- "))
    num2 = float(input("Enter second number :- "))
    choose = int(input('''1. sum 
2. subtraction
3. multiplication
4. division
What expression do you want to do :- '''))
    if (choose == 1):
        sum = sum(num1, num2)
        print(f"The sum of the given number is :- {sum}")
    elif (choose == 2):
        difference = diff(num1, num2)
        print(f"The difference of the given number is :- {difference}")

    elif (choose == 3):
        multiplication = mul(num1, num2)
        print(f"The multiplication of the given number is :- {multiplication}")

    elif (choose == 4):
        division = div(num1, num2)
        print(f"The division of the given number is :- {division:.3f}")

    else:
        print("invali operation")

main()