# Defining the function 
# def first_function():
#     print("hello python programmer.")

# first_function()
# Parameters
# input of the function 


# num1 = int(input("enter first number :- "))
# num2 = int(input("enter second number :- "))
# def sum(num1, num2):
#     print(f"The sum of two number is :- {num1 + num2}")
#     print(f"The difference of two number is :- {num1 - num2}")
#     print(f"The division of two number is :- {num1 / num2}")
#     print(f"The multiplication of two number is :- {num1 * num2}")
# sum(num1, num2)


# return of values
# num1 = int(input("enter first number :- "))
# num2 = int(input("enter second number :- "))
# def sum(num1, num2):
#     return num2 + num1
    

# print(sum(num1, num2))
# sum = sum(num1, num2)
# print(f"The sum the given number is :- {sum}")


# default parameters
# def sum(num1=50, num2=45):
#     return num1 + num2
# print(sum(50, 10))


num1 = int(input("enter first number :- "))
num2 = int(input("enter second number :- "))
def check(num1, num2):
    return num1 + num2, num1 - num2, num1 * num2, num1 / num2

# # print(f"sum = {check(num1, num2 )}")
# result = check(num1,num2)
# sum, diff, mul, div = result
# print(f"The sum of two number is :- {sum}")
# print(f"The difference of two number is :- {diff}")
# print(f"The division of two number is :- {mul}")
# print(f"The multiplication of two number is :- {div}")




l1 = [1, "krishna", 3.23 ,True, "Hello"]
def list(l1):
    print(len(l1))
    for i in l1:
        print(i)
list(l1)


# def sum(num1, num2):
#     return num1 + num2

# def mul(num1, num2):
#     return num1 * num2

# def diff(num1, num2):
#     return num1 - num2

# def div(num1, num2):
#     return num1 / num2

# Write a program using multiple function to 
# calculate the grade of the student, first function to ask the user about the score of the student 
# 2nd to check 