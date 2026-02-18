
# # creating a file 
# file_path = "newfile.txt"
# f = open(file_path, "x")
# print(f.name)
# print(f.mode)


# Writing something in the file




# f = open("newfile.txt", "r")
# data = f.read()
# print(data)
# line1 = f.readline()
# line2 = f.readline()
# print(line1)
# print(line2)
# lines = f.readlines()
# print(lines)


# with open("newfile.txt", "r") as f:
#     content = f.read()
#     print(content)

# # to append something in the file 
# with open("newfile.txt", "a") as f:
#     f.write("This isnan new line")


# to copy the content from one file to another file 
# creating new file 
# with open("newfile.txt", "r") as f1:
#     content = f1.read()

# with open("newfile.txt", "w") as f2:
#     f2.write(content)


# Prepar
# def calculate_score():
#     phy = float(input("Enter thr mark of physics :- "))
#     ches = float(input("Enter thr mark of chemistry :- "))
#     math = float(input("Enter thr mark of math :- "))

#     percentages = (phy + ches + math )/3
#     return phy, ches, math, percentages


# def calculate_score():
#     if (percentages >= 90):
#         return "A"
    
#     elif (percentages >= 80):
#         return "B"
    
#     elif (percentages >= 70):
#         return "C"
    
#     elif (percentages >= 60):
#         return "D"
    
#     elif (percentages >= 50):
#         return "E"
    
#     else:
#         print("fail")


# def main ():
#     name = input("Enter the name of student :- ")
#     roll = input("Enter the roll no. of student :- ")
#     phy, ches, math, score = calculate_score()

#     with open("student.txt", "a") as f:
#         f.write(f"--------------RESULT----------")
#         f.write(f"Name :- {name}")
#         f.write(f"roll :- {name}")
#         f.write(f"Name :- {name}")
        





