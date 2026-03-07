#Write Python code to add a new key-value pair to the following dictionary:
my_dict = {'name': 'python', 'age': 25}
dict_1={'city':'west godavari'}
my_dict.update(dict_1)
print(my_dict)

#write Python code to access and print the value associated with the key 'price' in the following dictionary:
product_info = {'name': 'Laptop', 'brand': 'Dell', 'price': 1200}
print(product_info.get('price'))

#Write Python code to remove the key-value pair with the key 'city' from the following dictionary:
my_dict = {'name': 'python', 'age': 30, 'city': 'Bhimavaram'}
dict_1=my_dict.pop('city')
print(my_dict)

#Write Python code to print all the keys present in the following dictionary
my_dict = {'name': 'python', 'age': 25, 'city': 'Rajahmundry'}
print(my_dict.keys())

#Write Python code to print all the values present in the following dictionary
my_dict = {'name': 'python', 'age': 25, 'city': 'tanuku'}
print(my_dict.values())