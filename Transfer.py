'''Write a Python program that takes a list of numbers as input 
numbers = [25, 30, 20, 40, 15, 25] and prints the sum of the numbers. However, if the sum exceeds 
100, stop adding numbers and print "Sum exceeded 100".'''
numbers = [25, 30, 20, 40, 15, 25]
sum = 0
for i in numbers:
    sum+=i
    if sum>100:
        break
print("sum exceeds 100")
print(sum)
print(f"{i}")
   
'''write a Python script that uses a for loop to iterate through numbers from 1 to 
600. Print only the odd numbers, skipping the even ones using the 
statement.'''

for i in range(1,601):
    if i%2==0:
        continue
    print(f"{i}")

'''Write a Python script that checks if a number is even or odd. If the number is 
even, print "Even"; if odd, do nothing (use the 
pass statement).'''
i=int(input("Enter a number:"))
if i%2==0:
    print("number is even")
else:
    pass

'''Write a Python script that iterates through a list of words. If the word is "break," 
exit the loop using the break statement. If the word is "skip," skip the rest of the code for the current iteration using the 
continue statement. For any other word, print the word'''
words = ["hello", "python", "skip", "world", "break", "coding"]

for word in words:
    if word == "break":
        break          # Exit the loop completely
    elif word == "skip":
        continue       # Skip this iteration
    else:
        print(word)




