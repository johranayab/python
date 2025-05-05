# f=open("demo.txt","r")

# data=f.read()
# print(data)
# print(type(data))



# with open(r"C:\Users\91844\Desktop\NEW JS\python\fileHandling\demo.txt", "r") as f:
#     data = f.read()
#     print(data)
#     print(type(data))



# with open(r"C:\Users\91844\Desktop\NEW JS\python\fileHandling\demo.txt", "r") as f:
#     data = f.read(20)
#     print(data)
#     print(type(data))




# with open(r"C:\Users\91844\Desktop\NEW JS\python\fileHandling\demo.txt", "w") as f:
#     data = f.write("i want to learn javaScript tommorow !!!")
#     print(data)
#     print(type(data))





with open(r"C:\Users\91844\Desktop\NEW JS\python\fileHandling\demo.txt", "a") as f:
    data = f.write("then i will move to java  !!!")
    print(data)
    print(type(data))



# f=open("sample.txt")




with open(r"C:\Users\91844\Desktop\NEW JS\python\fileHandling\demo.txt", "r+") as f:
    data = f.write(" i will move to cpp  !!!")
    print(data)
    # print(type(data))
