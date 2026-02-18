# a = 56
# b = 46
# # print(a==b)
# # print(a != b)


# name =  "krishna yadav"
# a = len(name)
# print(a)

# password = input("Enter your paasword")
# min_len  = 10
# a = len(password) > min_len
# print(a)


# if(min_len <= 10):
#     print("password is valid")

# else:
#     print("password not valid")

password = input("Enter your paaswor :- ")
default = "krishna"
min_len = 7
max_len = 20

is_longer = len(password) > min_len
is_smaller = len(password) < max_len
check = password != default

print(f"you entered password is longer :- {is_longer}")
print(f"you entered password is smaller :- {is_smaller}")
print(f"You entered password is not {check}")

