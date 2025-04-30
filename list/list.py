# Mixed data types
# data = [10, 3.14, "hello", True]


# fruits=["apple","banana","mango"]
# print(fruits[0])
# print(fruits[1:3])
# print(len(fruits))
# fruits[0]="graps"
# print(fruits)

#  2. Adding & Removing Elements

# fruits = ["apple", "banana", "mango"]
# fruits.append("orange")
# print("append  ,,",fruits)
# # Insert at index
# fruits.insert(1, "KIWI")
# print("insert  ,,",fruits)
# # Extend with another list
# fruits.extend(["papaya", "guava"])
# print("extend  ,,",fruits)
# # Remove by value
# fruits.remove("banana")
# print("removed  ,,",fruits)
# # Remove by index
# del fruits[0]
# removed = fruits.pop()
# print(fruits)
# print("removed", removed)

# numbers = [5, 3, 8, 1, 3]

# # count(): how many times value appears
# # print(numbers.count(3))  # 2

# # index(): first index of value
# # print(numbers.index(8))  # 2

# # # reverse(): reverse the list in-place
# # print (numbers.reverse())

# # # sort(): ascending
# print(numbers.sort())

# # # sort descending
# # numbers.sort(reverse=True)

# # # copy(): make a shallow copy

# # new_list = numbers.copy()




# nums = [10, 20, 30]

# print(sum(nums))    # 60
# print(max(nums))    # 30
# print(min(nums))    # 10
# print(sorted(nums)) # [10, 20, 30] (returns new list)
# print(any(nums))    # True
# print(all(nums))    # True


# Nested Lists (2D list)
matrix = [[1, 2], [3, 4], [5, 6]]

# Accessing elements
print(matrix[0][1])  # 2

# Flattening a 2D list
flat = [num for row in matrix for num in row]
print(flat)  # [1, 2, 3, 4, 5, 6]
