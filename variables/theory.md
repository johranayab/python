🔸 1. What is a variable in Python?
Answer:
A variable in Python is a name that refers to a memory location where data is stored. Variables are dynamically typed in Python.



 
🔸 2. How is Python different in terms of variable declaration compared to languages like Java or C++?
Answer:
In Python, you don’t need to declare the type of variable. Python is dynamically typed, so the type is inferred automatically.

x = 10    # int
x = "Hi"  # now string, no error
 
 

🔸 3. What are local and global variables?
Answer:
A local variable is declared inside a function and is only accessible within it.
A global variable is declared outside all functions and is accessible throughout the file.
 
 

 
🔸 5. Can variable names start with a number in Python?
Answer:
No. Variable names must start with a letter or underscore.
❌ 2name = "John" → Invalid


 
  6. Is Python strongly typed or loosely typed?
Answer:
Python is strongly typed — even though it's dynamically typed.

You cannot do:
 x = 10 + "20"  # ❌ TypeError



  7. What is the difference between = and == in Python?
Answer:

= is the assignment operator (assigns value to a variable)

== is the comparison operator (checks if values are equal)


 8. How can you find the type of a variable?
Answer:
Using type() or isinstance():
 



  10. What is the scope of a variable?
Answer:
Scope defines where the variable is accessible:

Local scope (inside a function)

Global scope (entire file/module)

Enclosing scope (nested functions)

Built-in scope (Python keywords)





 
 
person = {
"name": "Riya",
"age": 24,
"city": "Delhi"
}
 
 
 
"name" is a key, and "Riya" is its value
"age" is a key, and 24 is the value
"city" is a key, and "Delhi" is the value
🧩 What is person["name"]?..
 
This is called dictionary key access or key lookup.
✅ It's not calling an object or function, but rather accessing a value from the dictionary using its key.
 
 
 
 
 
11. String formatting with variables
first = "Coding" second = "is fun" sentence = f"{first} {second}!" print(sentence) why we use f here ??
 
✅ Reason: To Use f-string (formatted string)
In Python, the f before a string tells Python to use f-string formatting, which allows you to insert variables directly inside the string using {}.
 
 
💡 Without f:
python
 
first = "Coding"
second = "is fun"
sentence = "{first} {second}!"
print(sentence)
 
sentence = f"{first} {second}!"
 
f"..." is called an f-string.
It lets you easily insert variables into strings.
The expressions inside {} are evaluated and inserted
 
 
 
a = 10
b = 5
print(f"The sum is {a + b}")  # Output: The sum is 15
 