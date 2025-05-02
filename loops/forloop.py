# ✅ 1. Loop Over a List

# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)


# #    ✅ 2. Compare Items in List


# nums = [10, 20, 30]
# for num in nums:
#     if num > 15:
#         print(num, "is greater than 15 ")

#         # ✅ 3. Loop Over a String


# name="Python"
# for char in name :
#     print(char)


# ✅ 4. Check for Vowels in a String


# text = "hello"
# vowels = "aeiou"
# for char in text:
#     if char in vowels:
#         print(char, "Is a vowel")


# ✅ 5. Loop Over a Tuple


# colors =("red","green","blue")

# for color in colors:
#     print(color)



# ✅ 6. Loop Over a Set

# id={1,2,3}
# for ids in id:
#     print(ids)



# ✅ 7. Loop Over a Dictionary (keys only)
 
# person ={"name":"Alice","age":22}
# for key in person:
#     print(key , "=",person[key])
    
    
    
    
#     # ✅ 8. Loop Over Dictionary Items (key + value)
    
    
# for key, value in person.items():
#     print(f"{key} => {value}")





# ✅ 9. Using if, else inside Loop

# names=["Ali","Zara","john"]
# for name in names:
#     if name=="Zara":
#         print("found Zara:")
#     else:
#         print("Not Zara :", name)
        
        
        
        
        # ✅ 10. Check Common Items Between Lists
        
        
# a=[1,2,3]
# b=[3,4,5]
# for items in a:
#     if items in b:
#         print(items , "is common")





# ✅ 11. Loop Over Dictionary and Compare Values

# marks= { "math":80,"science":70 , "english":90}
# for subject , score in marks.items():
#     if score >=75:
#         print(subject,"passed")
#     else:
#         print(subject,"failed")
        
        
        # ✅ 12. Loop Through List of Tuples
        
        
        
# data=[("Alice",25),("bob",20)]      

# for name,age in  data :
#     if age >21:
#         print(name,"is adult") 



# ✅ 13. Use break in Loop


# words = ["hii","stop","byee"]

# for word in words:
#         if word=="stop":
                
#                 print(word)
                
                
                
                
                # ✅ 14. Use continue in Loop
                
# words =["yes","skip","okay"]

# for word in words:
#         if word == "skip":
#                 continue
#         print(word)
 
 
 
#  ✅ 15. List Comprehension with Condition

# nums=[1,2,3,4,5]
# squares=[x*x for x in nums if  x % 2==0]
# print(squares)


# # ✅ 16. Nested Loop on 2 Lists

# colors=["red","green"]

# shapes =["circle","square"]
# for color in colors:
#         for shape in shapes:
#                 print(color,shape)
                
                
                # ✅ 17. Loop With enumerate()
                
                
