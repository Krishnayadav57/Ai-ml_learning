      # Data structure in python.

# list1 = ["hello", 44, "krishna", 47.60, True, "good"] # mutable
# print(type(list1))

# list1[5] = "Bad" 
# print(list1)

# empty_list = []
# # empty_list1 = list()
# # print(type(empty_list))
# # empty_list.append = input("Enter the items :- ")
# empty_list.insert(0, "kriss")
# empty_list.insert(1, 56)
# empty_list.remove(56)
# for i in empty_list:
#     print(i)
# print(empty_list)


# list2 = []
# for i in range(5):
#     n = int(input("Enter :- "))
#     list2.append(n)
# print(list2)

# list3 = []
# for i in list2:
#     i ** 2
#     list3.append(i)

# print(list3)




# list1 = []
# tuple1 = ('krishna', 567, 45.6) # immutable   
# my_tuple = 1,2,3  # packing
# a, b, c = my_tuple  # Unpacking
# print(a)
# print(b)
# print(c)
# print(my_tuple + list1)
# print(list1.sort)






# dict1 = {
#     "name" : "krishna yadav",
#     "address" : "Siraha",
#     "roll no" : "813012",
#     "class" : "XII",
#     "marks" : [98, 99, 95, 100]
# } # Hashtables

# print(type(dict1))
# print(dict1.keys())
# print(dict1.values())
# print(list(dict1.items()))
# print(list(dict1.keys()))
# dict1["address"] = ["Biratnagar"]


# for i in dict1.keys():
#     print(i)


# for i in dict1.values():
#     print(i)


# for i, j in dict1.items():
#     print(f"{i} : {j}")

parent_dict = {
    1 : {
         "name" : "krishna yadav",
    "address" : "biratnagar",
    "roll no" : "813013",
    "class" : "XII",
    },

    2 : {
         "name" : "krishna",
    "address" : "Siraha",
    "roll no" : "813012",
    "class" : "XII",
    }
}

print(parent_dict)





#   Note: Set items are unchangeable, but you can remove items and add new items.   
# # 
# set5 = {1, 2, 3,(5,7,8),58}
# set6 = {1, 2, 3,[5,7,8],58}
# print(type(set5))
# print(type(set6))