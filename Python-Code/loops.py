# ------LOOPS PRACTICE Q/A's--------

# solution 1 Counting positive numbers

# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

# for num in numbers:
#     if num < 0:
#         continue
#     print(num, end=", ")
# ------------------------------------------------


# solution 2: Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n.

# even_sum = 0
# Input = 10 # int(input("Enter a number: "))

# for i in range(1, Input+1):
#     if i%2 == 0:
#         even_sum += 1
# print('Sum of even numbers:',even_sum)
# ------------------------------------------------


# solution 3: Multiplication Table Printer
# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

# Input = 2

# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(Input," X ",i, " = ", Input*i)
# ------------------------------------------------


# 4. Reverse a String
# Problem: Reverse a string using a loop.

# string = 'jaskaran'
# rev_string = ''
# for i in string:
#     rev_string = i + rev_string
# print(rev_string)
# ------------------------------------------------


# 5. Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.

# string = 'jaskaran singh'
# for char in string:
#     if string.count(char) == 1:
#         print("charactor is ", char)
#         break
# ------------------------------------------------


# 6. Factorial Calculator
# Problem: Compute the factorial of a number using a while loop.

# num = 5
# factorial = 1

# while num > 0:
#     factorial *= num
#     num -= 1
# print(factorial)
# ------------------------------------------------


# 7. Validate Input
# Problem: Keep asking the user for input until they enter a number between 1 and 10.


# while True:
#     Input= 12 # int(input('Enter your number: '))
#     if 1 <= Input <= 10:
#         print("now you are between 1 and 10")
#         break
#     else:
#         print('Invalid Input')
# ------------------------------------------------


# 8. Prime Number Checker
# Problem: Check if a number is prime.

# num = 2

# if num%2 == 0:
#     print(num, 'is not a prime number')
# else:
#     print(num,'is prime number')
# ------------------------------------------------


# 9. List Uniqueness Checker
# Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.

# items = ["apple", "banana", "orange", "apple", "mango"]
# item_set = set()

# for item in items:
#     if item in item_set:
#         print('Duplicate: ', item)
#         break
#     item_set.add(item)
# ------------------------------------------------

# 10. Exponential Backoff
# Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.

import time


# ------------------------------------------------