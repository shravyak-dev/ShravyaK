# Write a Python function named add that takes two arguments a and b and returns their sum.
def add(a,b):
    return(a+b)
print(add(4,5))

#Write a Python function named square that takes a number x as input and returns its square.
def square(x):
    return x * x
print(square(5))

#Write a Python function named factorial that takes a positive integer n as input and returns its factorial.
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(factorial(5))

#Write a Python function named maximum that takes a list of numbers as input and returns the maximum value in the list
def maximum(nums):
    return max(nums)
print(maximum ([23,13,67,45,84]) )

#write a Python function named reverse that takes a string s as input returns its reverse.
def reverse(s):
    return s[::-1]

print(reverse("reverse string"))

#Write a Python function named is_prime that takes a positive integer n as input and returns True if n is prime, otherwise False .
def is_prime(n):
    if n%2!=0:
        return True
    else:
        return False
print(is_prime(4))

#Write a Python function named fibonacci that takes a positive integer n as input and returns n th Fibonacci number.
def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(7))


#Write a Python function named is_palindrome that takes a string returns True if s is a palindrome, otherwise False 
def is_palindrome(s):
    if s ==s[::-1]:
        return(True)
    else:
        return(False)
print(is_palindrome("racecar"))

#write a Python function named .sum_of_squares that takes a list of numbers as input and returns the sum of the squares of those numbers.
def sum_of_squares(numbers):
    return sum(num**2 for num in numbers)
print(sum_of_squares([3,4,9,5]))

#Write a Python function named average that takes a list of numbers as input and returns the average value.
def average(nums):
    total=sum(nums)
    return total/len(nums)
print(average([42,45,76,48]))
