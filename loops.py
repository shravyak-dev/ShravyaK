'''Write a Python program that calculates and prints the sum of the squares of 
numbers from 1 to 5 using a for loop.'''
sum =0
for i in range(1,6):
    result=i**2
    sum += result
print(f"sum of squares are {sum}")

'''Write a Python program that uses a 
while loop to print a countdown from 5 to 1'''
count = 5
while count >=1:
    print(count)
    count -=1

'''Write a Python program to print the multiplication table for a user-specified 
number using a nested for loop'''
table =int(input("Enter Number to print table:"))
for i in range(1,2):
        for j in range(1,11):
            print(f"{table}*{j}={table*j}")

'''Write a Python program that uses a "for" loop to find the sum of all even 
numbers between 0 and 10 (inclusive)'''
sum = 0
for i in range(1,11):
    if i%2==0:
        sum+=i
print(f"Sum of even numbers is {sum}")

#Calculate the sum of all numbers from 1 to a given number
num=int(input("Enter any number:"))
sum = 0
for i in range(1,num+1):
     sum+=i
print(f"sum of all numbers from 1 to given number is {sum}")

#Display numbers from a list using loop
numbers = [1,2,3,4,5,6,7,8]
for num in numbers:
     print(num)

#Display numbers from -10 to -1 using for loop
for i in range(-10,0):
     print(i)

'''Write a Python program to print the cube of all numbers from 1 to a given number'''
num = int(input("Enter a Number:"))
total = 1
for i in range(1,num+1):
     total=i**3
     num+=total
print(f"cube of all numbers from 1 to a given number{num}")

