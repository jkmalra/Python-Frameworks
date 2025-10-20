#
# # -----QUESTIONS SOLVED FOR PRACTICE-------
#
# # ------------------------------------------------------------
# # 1. Basic Function Syntax
# # Problem: Write a function to calculate and return the square of a number.
#
# # def square(int):
# #     return int ** 2
#
# # result = square(4)
# # print(result)
# # ------------------------------------------------------------
#
# # 2. Function with Multiple Parameters
# # Problem: Create a function that takes two numbers as parameters and returns their sum.
#
# # def sum_of_two_numbers(num1,num2):
# #     return num1 + num2
#
# # result = sum_of_two_numbers(21,12)
# # print(result)
# # ------------------------------------------------------------
#
# # 3. Polymorphism in Functions
# # Problem: Write a function multiply that multiplies two numbers, but can also accept and multiply strings.
#
# # def multiply(p1,p2):
# #     return p1*p2
#
# # print(multiply(12,2))
# # print(multiply('hello ',4))
# # ------------------------------------------------------------
#
# # 4. Function Returning Multiple Values
# # Problem: Create a function that returns both (the area and circumference of a circle) given its radius.
#
# # import math
#
# # def circle(radius):
# #     area = math.pi * radius ** 2
# #     circumference = 2 * math.pi * radius
# #     return round(area, 2),round(circumference, 2)
#
# # print('Area and Circumference of circle is: ',circle(10))
# # ------------------------------------------------------------
#
# # 5. Default Parameter Value
# # Problem: Write a function that greets a user. If no name is provided, it should greet with a default name.
#
# # def greet(name='User'):
# #     return f"Good Morning {name} !"
#
# # Greet = greet('Jaskaran')
# # print(Greet)
# # print(greet())
# # ------------------------------------------------------------
#
# # 6. Lambda Function
# # Problem: Create a lambda function to compute the cube of a number.
#
# # cube = lambda num: num ** 3
# # print(cube(2))
# # ------------------------------------------------------------
#
# # 7. Function with *args
# # Problem: Write a function that takes variable number of arguments and returns their sum.
#
# # def sum_all(*args):
# #     for i in args:
# #         print(i * 2)
# #     return sum(args)
#
# # print(sum_all(1,2))
# # print(sum_all(1,2,3,4,5))
# # ------------------------------------------------------------
#
# # 8. Function with **kwargs
# # Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.
#
#
# # ------------------------------------------------------------
#
# # 9. Generator Function with yield
# # Problem: Write a generator function that yields even numbers up to a specified limit.
#
# # def generator():
#
#
# # ------------------------------------------------------------
#
# # 10. Recursive Function
# # Problem: Create a recursive function to calculate the factorial of a number.
#
#
# # ------------------------------------------------------------
#
# # DOC String
# """testing DOC String on functions"""
# def add(a,b):
#     """adding a and b"""
#     def sub(c,d):
#         """subtracting c and d"""
#         pass
#     return a + b
#
# print(add(21,1))
# help(add)


class person:
    """docstring for person"""
    def __init__(self, name, age):
        """docstring for person's function"""
        self.name = name
        self.age = age

help(person)

