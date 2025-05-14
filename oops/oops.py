# OOPs in Python
# OOP- Object Oriented Programming

# using list - creating student records
# student details


# student_1=['madhav',10]
# student_2=['vishaka',12]

# student_3='Keshav'

# student_1.append('A')
# print(student_1)

# print(f'{student_1[0]} is in class {student_1[1]}')

# print(f'{student_2} is in class {student_2[1]}')

# neww

# class Student:

#     name='johra'
#     grade=10


# student_1=Student()
# print(student_1.name,student_1.grade)


# student_2=Student()
# print(student_2.name,student_2.grade)


# neww


# class Student:


#     def __init__(self ,name,grade):
#         self.name=name
#         self.grade=grade


# student_1=Student("nayabb",1)
# print(student_1.name,student_1.grade)


# student_2=Student("lqaiba",90)
# print(student_2.name,student_2.grade)


# #new


# class Student:
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade

#     def student_details(self):  # Indented inside the class
#         print(f"{self.name} is in class {self.grade}")

# student_1 = Student("nayabb", 1)
# student_2 = Student("lqaiba", 90)

# student_1.student_details()
# student_2.student_details()

# new


# class Student:
#     def __init__(self, name, grade, percentaze):
#         self.name = name
#         self.grade = grade

#         self.percentaze = percentaze

#     def student_details(self):  # Indented inside the class
#         print(f"{self.name} is in class {self.grade} With {self.percentaze}%")


# student_1 = Student("nayabb", 1,99)
# student_2 = Student("lqaiba", 90,76)

# # student_1.student_details()
# # student_2.student_details()
# # print(student_1.name)

# print(student_1.__dict__)


# modify object property

# print(student_1.percentaze)
# student_1.percentaze = 100
# print(student_1.percentaze)


# # delete object property
# print(student_1.__dict__)
# del student_1.percentaze
# print(student_1.__dict__)


# # delete object

# del student_1
# print(student_1)


# class - blueprint or templat


# class Student:
#     def __init__(self, name, grade, percentaze, team):
#         self.name = name
#         self.grade = grade

#         self.percentaze = percentaze
#         self.team = team

#     def student_details(self):  # Indented inside the class
#         print(
#             f"{self.name} is in class {self.grade} With {self.percentaze}%  and is in team  {self.team}"
#         )


# team1 = "A"
# team2 = "B"
# student_1 = Student("nayabb", 1, 99, team1)
# student_2 = Student("lqaiba", 90, 76, team2)

# student_1.student_details()
# student_2.student_details()
# print(student_1.team)
# print(student_2.team)


# 4 features in OOPs
# Abstraction
# Encapsulation
# Inheritance
# Polymorphism


# Abstraction
# hiding unnecesary deatils from users through class, methods
# class Student:
#     def __init__(self, name, grade, percentaze):
#         self.name = name
#         self.grade = grade

#         self.percentaze = percentaze

#     def student_details(self):  # Indented inside the class
#         print(f"{self.name} is in class {self.grade} With {self.percentaze+2}% ")# Abstraction


# # object - instance of class

# student_1 = Student("nayabb", 1, 99)
# student_2 = Student("lqaiba", 90, 76)
# print(student_1.percentaze)
# student_1.student_details()
# # print(student_1.__percentaze)
# print(student_2.get_(percentaze())

# encapsulation

# Restrict access to certain attributes or methods to protect data and enforce controlled access

# class Student:
#     def __init__(self, name, grade, percentaze):
#         self.name = name
#         self.grade = grade

#         self.__percentaze = percentaze  # double underscore limit access
#     def get_percentaze(self):
#         return self.__percentaze


#     def student_details(self):  # Indented inside the class
#         print(
#             f"{self.name} is in class {self.grade} With {self.percentaze}% "
#         )  # encapsulation


# # object - instance of class

# student_1 = Student("nayabb", 1, 99)
# student_2 = Student("lqaiba", 90, 76)

# # student_1.student_details()#error

# # print(student_1.__percentaze)#error
# # print(student_1.__percentaze)#error
# print(student_1.get_percentaze())


# Inheritance
# allows one class (child) to reuse the prop and methods of another class (parent).


# parent class - baap
# class Student:  # student class
#     def __init__(self, name, grade, percentage):
#         self.name = name  # attribute
#         self.grade = grade
#         self.percentage = percentage

#     def student_details(self):  # method
#         print(f"{self.name} is in class {self.grade}, with {self.percentage}%")


# # object - instance of class
# student1 = Student("Madhav", 11, 96)
# student2 = Student("Vishakha", 12, 99)


# # clild  class beta
# class graduateStudent(
#     Student
# ):  # grauate calss is child class inherit prop an methons from parents class

#     def __init__(self, name, grade, percentage, stream):  # old
#         # parameters from parent class an new parameter in child class
#         super().__init__(name, grade, percentage)  # claa parent class init
#         self.stream = stream  # new attribute in child class

#     def student_details(self):
#         super().student_details()


# grad_student1 = graduateStudent("johra", 12, 89, "commerce")

# grad_student2 = graduateStudent("nayab", 12, 99, "science")

# print(grad_student1.stream)
# grad_student1.student_details()


# Polymorphism


class Student:  # student class
    def __init__(self, name, grade, percentage):
        self.name = name  # attribute
        self.grade = grade
        self.percentage = percentage

    def student_details(self):  # method
        print(f"{self.name} is in class {self.grade}, with {self.percentage}%")


# object - instance of class
student1 = Student("Madhav", 11, 96)
student2 = Student("Vishakha", 12, 99)


# child class
class GraduateStudent(Student):
    def __init__(self, name, grade, percentage, stream):
        super().__init__(name, grade, percentage)
        self.stream = stream

    def student_details(self):# method
        # super().student_details()
        # print(f"stream is {self.stream}")
       pass


# object - Student class
student1 = Student('Madhav', 11, 96)


# object - GraduateStudent class

Grad_Student1 = GraduateStudent("Keshav", 12, 96, "PCM")
student1.student_details()
Grad_Student1.student_details()
