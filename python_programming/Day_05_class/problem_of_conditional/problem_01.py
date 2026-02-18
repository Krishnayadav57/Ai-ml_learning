#     WAP to check if a number entered by the user is odd or even.

# num = int(input("Enter any number :- "))

# if (num % 2 == 0):
#     print(f'Number {num} is an even number.')

# else:
#     print(f'Number {num} is an odd number.')


    #  WAP to find the greatest of 3 numbers entered by the user.

# num1 = float(input("Enter a no. :- "))
# num2 = float(input("Enter a no. :- "))
# num3 = float(input("Enter a no. :- "))

# if num1 > num2 and num1 > num3 :
#     print(f"the greater no. is {num1}.")

# if num2 > num1 and num2 > num3 :
#     print(f"the greater no. is {num2}.")

# else:
#     print(f"the greater no. is {num3}.")


#     #   WAP to check if a number is a multiple of 7 or not.

# number = int(input("Enter any number :- "))
# if(number % 7 == 0):
#     print(f"Given number {number} is multiple of 7.")
# else:
#     print(f"Given number {number} is not multiple of 7.")



#         #  WAP to find the sum of first n numbers. (using while)
# nth = int(input("Enter how many numbers :-"))
# count = 0 
# sum = 0
# while (count < nth):
#     num = int(input("enter numbers :- "))
#     count += 1
#     sum += num
# print(f"The sum of all number is {sum}.")




    #   WAP to find the factorial of first n numbers. (using for)

# num = int(input("Enter any number :- "))
# if(num < 0):
#     print("no factorial for negative number.")
# elif(num == 0 or num == 1):
#     print(f'The factorial of {num} is 1.')
# else:
#     factorial = 1
#     for i in range(1, (num+1)):
#      factorial *= i

# print(f"The factorial of {num} is {factorial}")




#  Ask the user to enter a number and check whether it is positive, negative, or zero.

# num = int(input("Enter any number :- "))

# if (num == 0):
#     print(f'Number {num} is an Zero number.')

# elif (num < 0):
#     print(f'Number {num} is an negative number.')

# else:
#     print(f'Number {num} is an positive number.')


#  Take a number as input and print its multiplication table up to 10. (Assignment)
# number = int(input("enter any number :- "))
# for i in range (1, 11):
#     print(f"{number} * {i} = {number * i}")