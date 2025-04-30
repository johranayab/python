import math
print(math.sqrt(25))

# 13. Floor and Cei 
print(math.floor(3.7)) #3
print(math.ceil(4.5))#5


# 14. Logarithm

print(math.log(100,10))  # 2.0.


# 15. Factorial
print(math.factorial(5))#120

# 16. Trigonometry
print(math.sin(math.pi/2))

# 17. Constants
print(math.pi)
print(math.e) 


from decimal import Decimal, getcontext

# 18. Decimal for more precision
getcontext().prec = 6
x = Decimal('1.123456789')
y = Decimal('2.987654321')
print(x + y)  # 4.11111...

from fractions import Fraction

# 19. Fraction
f1 = Fraction(1, 3)
f2 = Fraction(2, 5)
print(f1 + f2)  # 11/15
