#you are given a string sentence.Print the characters at even indices
sentence = "Python is amazing"
print(sentence[0:17:2])

#You are given a string s . Replace all spaces in the string with underscores (and print the modified string)
s = "Python is fun and powerful"
new_string=s.replace(" ","_")
print(new_string)

#You are given a string s . Check if the string contains only digits
s = "12345"
is_numeric=s.isdigit()
print(is_numeric)

#you are given a string . Print the string in reverse order.
s = "Python is amazing"
reverse_string=s[::-1]
print(reverse_string)

#You are given a string s . Capitalize the first letter of each word in the string and print the modified string
s = "python programming is fun"
capitalized_text= s.title()
print(capitalized_text)