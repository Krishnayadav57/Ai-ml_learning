# s = int("Hello")
# print(s)

# a = 45
# b = '123'
# print(a + b)

# a = 45
# b = 0
# print(a / b)

# try:
#     s = int ("12")
#     print(s)
# except:
#     print("error")
# finally:
#     print("code ended")

try:
    num1 = int(input('enter first number :- '))
    num2 = int(input('enter second number :- '))
    division = num1 / num2

except ValueError:
    print("Value error occured")

except TypeError:
    print("Value error occured")

except ZeroDivisionError:
    print("Value ZeroDivisionError occured")

else:
    print(division)

finally:
    print("program ended")











# try:
#     a = int(input("Hey, Enter a number: "))
#     print(a)

# except ValueError as v:
#     print("please enter an number ")
#     print(v)
    
# except Exception as e:
#     print(e) 

# finally:
#     print("code ended")

# print("Thank You")