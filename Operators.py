'''Create a program that takes user input for their name and age. 
Use formatted strings (f-strings) to print a message welcoming the user and
stating their age.'''

name = input("Enter your name:")
Age = input("Enter your age:")
print(f"Welcome {name} and you are {Age} years old")

#Create a list called numbers that contains integers from 1 to 10
numbers = [1,2,3,4,5,6,7,8,9,10]
print(type(numbers))
print(5 in numbers)
print(15 not in numbers)

'''write a Python program to calculate the area of a rectangle using the given 
formula: area = length * width . Take the values of length and width as inputs from 
the user.'''
length = float(input("Enter the lenght value:"))
width = float(input("Enter the width value:"))
Area=length*width
print(f"Area of rectangle is{Area}")

'''Write a Python program to demonstrate incrementing and decrementing a variable'''
x = 10

# Incrementing
x += 1
print("After incrementing by 1:", x)

# Decrementing
x -= 1
print("After decrementing by 1:", x)

'''Write a Python program to convert temperature from Celsius to Fahrenheit. The 
formula for conversion is: 
F = (C * 9/5) + 32 . Take the temperature in Celsius as input'''

celsius = float(input("Enter the celsius value:"))
Total_Celsius=celsius*9/5
Temperature=Total_Celsius+32
print(f"Temperature from celsius to Fahrenheit is {Temperature}")

'''Write a Python program to calculate the simple interest given the principal 
amount, rate, and time (in years)'''
principal_amount=float(input("Enter the principle value:"))
Rate=float(input("Enter the Rate value:"))
time=int(input("Enter the time (years):"))
simple_interest=principal_amount*Rate*time/100
print(simple_interest)

'''Write a Python program to concatenate two strings and display the result. The 
strings should be taken as input from the user'''
str_1=str(input("Enter your first name:"))
str_2=str(input("Enter your last name:"))
Full_Name=str_1+str_2
print(f"Your Full Name is {Full_Name}")

'''Write a Python program to convert a distance from kilometers to miles'''
Distance=float(input("Enter the distance travelled(km):"))
Total_Distance=Distance*0.621
print(f"Distance travelled in miles is {Total_Distance}")

