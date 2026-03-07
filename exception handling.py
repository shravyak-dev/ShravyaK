#1.try and except example:
try:
    num_1=int(input("Enter first number:"))
    num_2=int(input("Enter second number:"))
    result=num_1/num_2
    print("Result:",result)
except ZeroDivisionError:
    print("Error:cannot divide by zero")

#2.else block:else runs only if no exception occurs.
try:
    num = int(input("Enter a number: "))
    result = 5 / num
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("Result is:", result)

#3.finally block :finally always executes whether error occurs or not.
try:
    num_1=int(input("Enter first number:"))
    num_2=int(input("Enter second number:"))
    result=num_1/num_2
    print("Result:",result)
except ZeroDivisionError:
    print("Error:cannot divide by zero")
finally:
    print("Executed successfully!")

# 4.Value error:Occurs when correct type but wrong value is given.
try:
    num = int("abc")   
except ValueError:
    print("ValueError occurred, Cannot convert string to integer.")

# 5.Type error:Occurs when wrong data type is used.
try:
    result = "10" + 5   # Cannot add string and integer
except TypeError:
    print("TypeError occurred ,wrong data types.")

# 6.filenotfounderror:Occurs when file does not exist.
try:
    file = open("sample.txt", "r")
except FileNotFoundError:
    print("FileNotFoundError, File not found.")

#7.zerodivisionerror:Occurs when dividing by zero.
try:
    a = 5
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("ZeroDivisionError, Cannot divide by zero.")

#8.Indexerror:Occurs when accessing invalid index.
try:
    list1 = [1, 2, 3]
    print(list1[5])
except IndexError:
    print("IndexError! List index out of range.")

#9.keyerror:Occurs when key not found in dictionary.
try:
    dict = {"name": "Shravya"}
    print(dict["age"])
except KeyError:
    print("KeyError! Key not found in dictionary.")

#10.object error:Occurs when object has no such attribute.
try:
    x = 10
    x.append(5)   # int has no append method
except AttributeError:
    print("AttributeError! Attribute not found.")

#11.overflow:Occurs when result is too large
import math
try:
    print(math.exp(1000))
except OverflowError:
    print("OverflowError, Number too large.")

#12.IOerror:Occurs during input/output operation failure.
try:
    file = open("demo.txt", "r")
    file.write("Hello")   # Writing in read mode
except IOError:
    print("IOError! Cannot perform I/O operation.")

#13.RunTimeerror:Occurs during program execution.
try:
    raise RuntimeError("Something went wrong!")
except RuntimeError:
    print("RuntimeError occurred!")

#14.Exception (Base class of all exceptions):Exception is the base class for all built-in exceptions.
try:
    num = int("abc")
except Exception as e:
    print("Exception found")
    print("Error message:", e)


