'''write a Python program that takes a character as input and checks whether 
it is a vowel or not. Use the 
if-else statement.'''
char = input("enter a char:")
vowels = "aeiouAEIOU"
if char in vowels:
    print("Given char is vowel")
else:
    print("Given char is not vowel")


'''write a program that takes an age as input and classifies the person into 
one of the following age groups:
Child: 0-12 years
Teenager: 13-17 years
Adult: 18-64 years
Senior: 65 years and older'''

Age = int(input("Enter your age:"))
if Age >0 and Age<=12:
    print(f"You are a child as you are {Age} years old")
elif Age >=13 and Age<=17:
    print(f"you are Teenager as you are {Age} years old")
elif Age >=18 and Age<=64:
    print(f"You are Adult as you are {Age} years old")
elif Age >=65:
    print(f"You are Senior as you are {Age} years old")
else:
    print("invalid value")

'''Write a program that takes an integer as input and classifies it as positive, 
negative, or zero. Use the 
if-elif-else statement'''
Num = int(input("Enter a number:"))
if Num >0:
    print("Given number is positive")
elif Num <0:
    print("Given number is negative")
elif Num ==0:
    print("Given number is 0")
else:
    print("invalid value")

'''Create a program that checks whether a given year is a leap year or not. A 
leap year is divisible by 4, but not by 100 unless it is divisible by 400'''
Year=int(input("Enter year:"))
if Year%4==0:
    print("Given year is a leap year")
elif Year%400==0:
    print("Given year is a leap year")
elif Year%100==0:
    print("Given year is not leap year")
else:
    print("Given year is not leap year")

'''Build a simple calculator program that takes two numbers and an operator 
(+, -, *, /) as input and performs the corresponding operation.'''
num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
operator=input("Enter operator(+,-,*,/):")
if operator == '+':
   print(num1+num2)
elif operator =='-':
    print(num1-num2)
elif operator =='*':
    print(num1*num2)
elif operator =='/':
    print(num1/num2)
else:
    print("invalid value")

'''x = 8
if x % 2 == 0: result = "Even"
else: result = "Odd"'''
#short-hand-if
x=2
Result=print("x is even") if x%2==0 else print("x is odd")


'''Create a program that calculates the final price after applying a discount. 
The program should take the original price and the discount percentage as 
input'''
Original_price=float(input("Enter the price:"))
Discount_percent=float(input("Enter the discount:"))
Discount_amount = (Original_price*Discount_percent)/100
final_price = Original_price - Discount_amount
print(final_price)

'''Write a program that calculates the Body Mass Index BMI using the 
formula: BMI  weight (kg) / (height (m))^2. The program should take 
weight and height as input'''
Weight = float(input("Enter weight of your body:"))
Height = float(input("Enter height :"))
Total_Height = (Height)**2
BMI = Weight/Total_Height
print(BMI)



