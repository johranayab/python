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

print(student_1.percentaze)
student_1.percentaze=100
print(student_1.percentaze)


# delete object property
print(student_1.__dict__)
del student_1.percentaze
print(student_1.__dict__)


# delete object

del student_1
print(student_1)


# class - blueprint or templat


class Student:
    def __init__(self, name, grade, percentaze, team):
        self.name = name
        self.grade = grade

        self.percentaze = percentaze
        self.team = team

    def student_details(self):  # Indented inside the class
        print(
            f"{self.name} is in class {self.grade} With {self.percentaze}%  and is in team  {self.team}"
        )


team1 = "A"
team2 = "B"
student_1 = Student("nayabb", 1, 99, team1)
student_2 = Student("lqaiba", 90, 76, team2)

student_1.student_details()
student_2.student_details()
print(student_1.team)
print(student_2.team)


# 4 features in OOPs
# Abstraction
# Encapsulation
# Inheritance
# Polymorphism


# Abstraction
# hiding unnecesary deatils from users through class, methods
class Student:
    def __init__(self, name, grade, percentaze):
        self.name = name
        self.grade = grade

        self.percentaze = percentaze

    def student_details(self):  # Indented inside the class
        print(f"{self.name} is in class {self.grade} With {self.percentaze+2}% ")


# object - instance of class

student_1 = Student("nayabb", 1, 99)
student_2 = Student("lqaiba", 90, 76)
print(student_1.percentaze)
student_1.student_details()
# # print(student_1.__percentaze)
# print(student_2.get_(percentaze())
