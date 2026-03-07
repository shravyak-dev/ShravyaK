# Write a Python function square_all(numbers) that takes a list of numbers as input and returns a new list containing the square of each number in the input list. Use the 
# map() function with a lambda function to implement this
list_1=[3,45,6,87,24,5,6,]

result=map(lambda a:a**2,list_1)
print(list(result))

# write a Python function filter_positive(numbers) that takes a list of numbers as input and returns a new list containing only the positive numbers from the input list. Use the 
# filter() function with a lambda function to implement this.
list_2=[2,-5,8,5,-45,86,45,-87,-34]
result=filter(lambda a:a>0,list_2)
print(list(result))

#Write a Python function calculate_factorial(n) that calculates the factorial of a given number n. Use the reduce() function with an appropriate lambda 
# function to implement this
from functools import reduce
n=5
result= reduce(lambda x, y: x * y, range(1, n + 1))
print(result)

# Write a Python function count_vowels(string) that takes a string as input and returns the count of vowels (a, e, i, o, u) in the input string. Use the 
# reduce() function with an appropriate lambda function to implement this.
from functools import reduce
def countvowels(string):
    vowels="aeiouAEIOU"
    return reduce(lambda count,char:count + (1 if char in vowels else 0),string,0)
print(countvowels("shravya"))