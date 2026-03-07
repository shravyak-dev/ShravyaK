# Write a Python program that prints your name.
print("My name is Shravya K")

# Create a Python script with both single-line and multi-line comments 
# explaining the purpose of the script.
print("integer is denoted as int") #this line explains integer is denoted by int
print("there are different types of datatypes")
'''The above statement says
we have different types of data types'''


#define a list containing three different data types.
Data = ["Mangoes",19.0,["python","java"],{1,9}]
print(type(Data))

#Define a set containing employee idʼs
employee_ids = {51852,4689,36729}
print(type(employee_ids))

#Concatenate two strings and print the result.
first_name = "Shravya"
last_name = "K"
print(first_name + ' ' +last_name)

#Repeat a string three times and display the output.
first_name = "Shravya"
last_name = "K"
repeated_str = first_name*3
print(repeated_str)

#Declare two variables, one storing an integer and the other a string. 
#Print their values.
str_var = "String"
num_var = 25
print(str_var)
print(num_var)

#Convert a float to an integer and print the result
pi = 3.14
num = int(pi)
print(num)
print(type(num))

#Convert an integer to a string and display the output
num = 30
str_num = str(num)
print(str_num)
print(type(str_num))

#Take the user's age as input and print a message using that input.
Age = input("Enter your age:")
print(f"you are {Age} years old")