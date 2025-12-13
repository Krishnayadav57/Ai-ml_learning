# a = 56
# b = 25

# add = a +b
# subtract = a - b
# multiply = a * b



# creating class 
# class Student :
#     name = "krishna yadav"
#     roll_no = "001"
#     section = "hinton"

# s1 = Student()
# print(s1.name)
# s2 = Student()
# print(s2.name)



# class Student :
#     def __init__(self, name, roll, address):
#         print("I am called")
#         self.name = name
#         self.roll = roll
#         self.address = address

#     def student_info(self):
#         print(f"Name :- {self.name}\nRoll No :- {self.roll}\nAddress :- {self.address}")

# s1 = Student("krishna yadav", "0012", "siraha")
# # print(s1.name, s1.roll, s1.address)
# s1.student_info()
# # s2 = Student()
# # s3 = Student()
# # s4 = Student()



# # car class 
# class car :
#     def __init__(self):
#         self.brand = brand
#         self.model_no = model_no
#         self.



# in haritence
# class parent:
#     hair_color = "golden brown"

# class child (parent):
#     pass

# child1 = child()
# print(child1.hair_color)



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"I am {self.name} and I am {self.age} years old")

class Student(Person):
        def __init__(self, name, age, roll):
            super().__init__(name,age)
            self.roll = roll

        def Student_info(self):
            print(f"I am {self.name}, I am student , My age is {self.age}, my roll no is {self.roll}")


class Teacher (Person):
        def __init__(self, name, age, subject):
            super().__init__(name, age)
            self.subject = subject

        def teach(self):
            print(f"I teach {self.subject}")

# creating object
s1 = Student("krishna", 60, "001")
t1 = Teacher("sujan", 40, "math")
s1.Student_info()
s1.introduce()
t1.teach()