# fruits={"apple","banana","cherry"}
# print(fruits)

# # ✅ 2. Add Item to Set

# fruits.add("mango")
# print(fruits)

# # ✅ 3. Update Set with Multiple Values


# fruits.update(["grape","papaya"])
# print(fruits)



# collection={1,2,2,2,3,4,4,"hello","world","world",4}
# print(collection)

# print(type(collection))

# sets methods




# collection=set()
# collection.add(1)
# collection.add(2)
# collection.add(3)


# collection.add(2)
# collection.add(4)
# collection.add(5)
# collection.add("johra")
# collection.remove(2)
# collection.add((1,2,3))
# # collection.add([1,2,3])
# # collection.remove(9)
# # print(collection)
# # print(len(collection))
# # collection.clear()
# # print(collection)
# # print(len(collection))



# print(collection)



# collection ={"Hello","apnacollege","johra","nayab","simmi","python"}
# collection.pop()
# print(collection)



# #union
# set1={1,2,3}
# set2={2,3,4}
# # print(set1.union(set2))
# print(set1.intersection(set2))




# fruits = {"apple", "banana", "cherry"}
# print(fruits)
# fruits.add("mango")
# print(fruits)

# fruits.update(["grapes","papaya"])
# print(fruits)
# fruits.remove("banana")
# print(fruits)

# fruits.clear()
# print(fruits)

# colors={"red","blue","green"}

# for color in colors:
#   print(color)
  
# #   ✅ 8. Check if Element Exists
#   print("red" not in   colors)
  
#   print("red" in colors)
#   print(len(colors))



# ✅ 10. Set Comparison: Equality


# a={1,2,3}
# b={3,1,2}
# # # print(a==b)



# # # ✅ 11. Set Comparison: Subset

# # print({1,2}.issuperset(a))


# # ✅ 12. Set Comparison: Superset

# print(a.issuperset({2}))

# ✅ 14. Set Union

# a = {1, 2}
# b = {3, 4}
# print(a.union(b))  # {1, 2, 3, 4}






# a = {1, 2, 3}
# b = {2, 3, 4}
# print(a.intersection(b))  # {2, 3}

# print(a.difference(b))  # {1}
# print(b.difference(a))  # {4}

# a = {1, 2, 3}
# b = {3, 4, 5}
# for item in a:
#     if item in b:
#         print(f"Common: {item}")
# ✅ 19. Convert List to Set (Remove Duplicates)



nums = [1, 2, 2, 3, 3, 3]
unique = set(nums)
print(unique)
