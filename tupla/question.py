# Convert a tuple of strings to a single string.
# t=("Hello", "world", "from", "ChatGPT")
# result="  ".join(t)
# print(result)


# t = ("Age:", 25, "years")

# # Convert all elements to string first
# result = " ".join(str(item) for item in t)

# print(result)
# Unpack a tuple of 5 elements into separate variables.

# t = (10, 20, 30, 40, 50)

# # Unpack the tuple
# a, b, c, d, e = t

# print(a)  # 10
# print(b)  # 20
# print(c)  # 30
# print(d)  # 40
# print(e)  # 50
# Merge two tuples and sort.




# Two tuples
t1 = (5, 2, 9, 1)
t2 = (8, 3, 7)

# Step 1: Merge tuples using +
merged = t1 + t2

# Step 2: Sort the merged tuple
# First convert to list, sort, then convert back to tuple
sorted_tuple = tuple(sorted(merged))

print("Merged and sorted tuple:", sorted_tuple)
