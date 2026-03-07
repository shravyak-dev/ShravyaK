
#Write Python code to reverse the order of elements in the given list Print the reversed list
list = [10, 20, 30, 40, 50, 11]
list.reverse()
print(list)

#Given two lists them.list1 and list2 , find and print the common elements between 
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = []
for i in list1:
    if i in list2:
        common.append(i)
print(f"common elements: {common}")

#Create a new list unique_list containing only the unique elements from the given list original_list . Print the unique list.
original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = []

for i in original_list:
    if i not in unique_list:
        unique_list.append(i)

print(f"Unique_list: {unique_list}")

#Remove duplicate elements from the given list without duplicates while preserving the order.duplicated_list and print the list 
duplicated_list = [1, 2, 2, 3, 4, 4, 5]
list =[]
for i in duplicated_list:
    if i not in list:
        list.append(i)
print(f"list:{list}")

#Write a Python script that concatenates two lists and prints the result
my_list1=[1,2,3,4]
my_list2=[5,6,7,8]
my_list1.append(my_list2)
print(f"concatenated list :{my_list1}")

#Write a Python script that repeats a list three times and prints the result
list=[1,2,3]
Result=3*list
print(Result)

#Write a Python script that removes the elements at even indices from a list
my_list = [10, 20, 30, 40, 50, 60]
result = my_list[1::2]
print(f"After removing even indices:{result}")

#Write a Python script that inserts the numbers 10, 11, and 12 at the beginning of a list
numbers=[2,3,4,5,6]
numbers.insert(0,10)
numbers.insert(1,11)
numbers.insert(2,12)
print(numbers)

#Create a list of squares of numbers from 1 to 10
squares = [x**2 for x in range(11)]
print(squares)

#Generate a list of even numbers from 1 to 20.
Even_numbers = [x for x in range(21) if x%2==0]
print(Even_numbers)

# Given a list of words, create a list containing the lengths of each word
words = ["apple", "banana", "cherry", "date"]
list=[len("apple"),len( "banana"),len("cherry"),len("date")]
print(list)