# def cal_sum(a,b):
#     sum=a+b
#     print(sum)
#     return sum

# cal_sum(2,3)


# cal_sum(2,3)
# cal_sum(3,3)
# cal_sum(8,3)
# cal_sum(5,3)
# cal_sum(6,3)

# 2

# def cal_sum(a,b):
#     return a+b

# sum = cal_sum(1,2)
# print(sum)

# def print_hello():
#     print("hello")

#     print_hello()
#     print_hello()
#     print(print_hello())


# 3


# def cal_avg(a, b, c):
#     sum = a + b + c
#     avg = sum / 3

#     print(avg)
#     return avg
# cal_avg(22,44,55)

# 4

# def cal_prod( b , a=2):
#     print(a*b)
#     return a*b
# cal_prod(4 )


# 5

# cities = ["delhi", "gurgoan", "noida", "pune", "mumbai", "channel"]
# heros = ["thor", "IronMan", "Captain Amrica", "shaktiman"]


# def print_len(list):
#     print(len(list))
#     print(list)


# print_len(cities)
# print_len(heros)


# ✅ 2. Function With Arguments


# def greed(name):
#     print("hello", name)


# greed("johra")


# ✅ 3. Function With Return Value

# def add(a,b): 

#     return a+b
# result =add(2,4)
# print(result)


# ✅ 6. Function With Arbitrary Arguments (*args)

# def total(*nums):
#     print("Sum:", sum(nums))
# total(1, 2, 3, 4)


# ✅ 8. Function Calling Another Function


def square(n):
    return n * n

 
def show():
    print("square of  s is |", square(6))
    
     
    
show()


