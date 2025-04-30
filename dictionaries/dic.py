# ✅ 1. Basic Dictionary + Compare Value

# student={ "name":"johra", "age":21}

# if student["age"]>28:
#     print("you are adult")
# else:print("your are not adult")


# ✅ 2. Compare Two Dictionary Keys

# product = {"price":1500,"discount_prince":1200}

# if product["discount_prince"]<product["price"]:
#     print("Discoubnt available")

# else:print("discount is not available")

# ✅ 3. Check If Key Exists Before Comparison''

# person={"name":"ankita","salary":24000}

# if "salary" in person and person["salary"]>20000:
#     print("Eligible for loan")


#     # ✅ 4. Use get() for Safe Comparison

#     if person.get("salary",0)>30000:
#         print("High salary")
#     else:print("Average salary")

# ✅ 5. Nested Dictionary Comparison

# student={
#     "stu1":{"name":"Ravi","marks": 75},
#     "stu2":{"name":"Ankita","marks":90}
#     }
# if student["stu2"]["marks"]>student["stu1"]["marks"]:
#         print("Ankita scored more")


# ✅ 6. Compare Length of Two Dictionaries

# dict1 = {"a": 1, "b": 2}
# dict2 = {"X": 10}

# if len(dict1) > len(dict2):
#     print("Dict1 is larger")

# # ✅ 7. Compare Values in Dictionary

# fruits = {"apple": 100, "banana": 40, "mango": 80}
# for fruit, price in fruits.items():
#     if price > 50:

#         print(f"{fruit} is expensive")




#  8. Compare Keys Between Two Dicts

# d1={"a":1,"b":2}
# d2={"b":3,"c":4}
# common_key = d1.keys()& d2.keys()
# print("Common keys",common_key)

# ✅ 9. Find Max Value in Dictionary

# maths={
#     "math":88,
#     "science":92,
#     "emglish":84,
#     "geogarphy":90,
     
    
# }
# max_subject=max(maths,key=maths.get)

# print("highest marks in :",max_subject)


# ✅ 10. Find Min Value in Dictionary

# marks={
#     "math":88,
#     "science":92,
#     "emglish":84,
#     "geogarphy":90,
     
    
# } 

# min_sub=min(marks,key=marks.get)
# print("Lowyer  marks in :", min_sub).


# ✅ 11. Sort Dictionary by Values (Descending)

# marks={
#     "math":88,
#     "science":92,
#     "emglish":84,
#     "geogarphy":90,
     
    
# }

# sorted_marks = dict(sorted(marks.items(), key=lambda x: x[1],reverse=True))
# print(sorted_marks)


# ✅ 12. Dictionary Value Comparison Using all()

# prices={"pen":10,"pencil":5,"eraser":8}

# if all(value<20 for value in prices.values()):
#     print("All items are cheap")
    
    
    # ✅ 13. Use any() in Dictionary
    
    
# prices={"pen":10,"pencil":5,"eraser":8}
# if any(value<10 for value in prices.values()):
#         print(" some items are cheap")
        
        
        # ✅ 14. Compare If Two Dictionaries Are Equal
        
        
# a={"X":1,"Y":2}
# b={"Y":2,"X":1}

# if a==b:
#     print("Both are dictionaries are equal")
    
#             # ✅ 15. Count Matching Values in Two Dictionaries


# dict1 = {"a": 1, "b": 2}
# dict2 = {"a": 1, "b": 3}

# matches = sum(1 for k in dict1 if k in dict2 and dict1[k] == dict2[k])
# print("Matching values:", matches)

# ✅ 16. Compare and Merge Two Dictionaries

a={"name":"johra","age":20}
b={"course":"BCa","AGE":21}

merged=a.copy()
merged.update(b)
print(merged)