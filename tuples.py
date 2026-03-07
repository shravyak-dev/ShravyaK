#Write a program that creates a tuple containing three elements: your name, your age, and your favorite color. Then print the tuple
person_info=('shravya',23,'blue')
print(person_info)

#Write a program that creates a tuple containing the days of the week. Then, print the third element of the tuple.
week_days=('monday','tuesday','wednesday','thursday','friday','saturday','sunday')
print(week_days[2])

#Write a program that creates two tuples, one containing odd numbers from 1 to 5 and another containing even numbers from 2 to 6. Concatenate these two tuples and print the result.
odd_numbers=(1,3,5)
even_numbers=(2,4,6)
print(odd_numbers+even_numbers)

#Write a program that defines a tuple containing the dimensions of a rectangle (length and width). Then, unpack this tuple into two variables and calculate the area of the rectangle
length=5
width=9
Area_of_rectangle=length*width
print(Area_of_rectangle)

# Write a program that checks if a given element exists in a tuple
tuple=(1,2,3,4,5)
is_present= 3 in tuple
print(is_present)

# Write a Python program to generate a bill for a supermarket purchase. The program should store the items and their prices in a list of tuples. It should 
# then iterate over this list to print out each item along with its price. Finally, calculate and print the total cost of all the item
items = [("Apple", 99), ("Banana", 99), ("Milk", 49)]
print(f"items\tprice")
print("-"*20)
total=0
for i,j in items:
    print(f"{i}\t{j}")
    total+=j
print("-"*20)
print(f"total\t{total}")
