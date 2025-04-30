# 15. Using variables in a dictionary
# person={
#     "name":"riya",
#     "age":23,
#     "city":"delhi"
# }
# print(person["name"],person["age"],person["city"])


# 16. Dynamic variable values (from user input)

# name=input("enter your name")
# print("hiiii"+name)


# 17. Variable scope (global and local)\

# x = "global"


# def show():
#     x = "local"


# print("inside the  function", x)

# show()
# print("outside function", x)


# x = "global"


# def show():
#     x = "local"
#     print("Inside function:", x)


# show()
# print("Outside function:", x)


# 18. Global keyword

# count =0


# def increase():
#     global count
# if count < 6:
#     count += 1
#     increase()
#     print("count", count)

#     increase()

# count = 0

# def increase():
#     global count
#     if count < 5:       
#         count += 1
#         increase()
#     print("count", count)
# increase()

# count = 0  

# def increasee():
#     global count
#     if count < 6:
#         count += 1
#         increasee()
#     print("count", count)
# increasee()



# 19. Using type() and isinstance()

# num=100
# print(type(num))
# print(isinstance(num,int))


# 20. Complex number variable
comp=3+4j
print("complex",comp)
print("real part",comp.real)
print("imaginart part",comp.imag)
