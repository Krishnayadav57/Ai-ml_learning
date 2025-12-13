# args and kwarg
# *args


# def my_func(*args):
#     print(f"My first argument :- {args[0]}")
#     print(f"My second argument :- {args[1]}")
#     print(f"My third argument :- {args[2]}")

# my_func(45, 50, 5)



# def add_num(*take_all_argument):
#     sum = 0
#     for i in take_all_argument:
#         sum += i
#     print(sum)

# add_num(45, 55)
# add_num(5, 25)
# add_num(425, 44, 25, 75)




# kwarg

# def fun1(**kwarg):
#     print(kwarg)
#     for key, value in kwarg.items():
#         print(f"{key} : {value}")

# fun1(name = "krishna yadav", address = "siraha", grade = "XII", section = "Hinton")


# def fun2 (*args, **kwargs):
#     for i in args:
#         print(i)
    
#     for key, value in kwargs.items():
#         print(f"{key} : {value}")

# fun2(name = "krishna yadav", address = "siraha", grade = "XII", section = "Hinton")




# list4 = ["hello", 45.15, "good job"]

# try:
#     print(list4[3])

# except IndexError:
#     print("Index is out of range.")



list4 = ["hello", "45.15", "good job", "python", "500"]
converted_list = []

for element in list4:
    try:
        converted_list.append(int(element))
    except ValueError:
        converted_list.append("Invalid")

print(converted_list)