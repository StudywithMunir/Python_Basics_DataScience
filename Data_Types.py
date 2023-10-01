# checking which type of data is stored in a variable
color = "Green"
grade = 'A'
num = 12
fnum = 12.90
is_saturday = False

print(type(color))
print(type(grade))
print(type(fnum))

# Data Types

# 1: Primitive 

# Integer
current_year = 2023
print(type(current_year))

# Float
pi = 3.1415
print(type(pi))

avogadro_number = 6.0221407e23 #6.0221407e23 means 6.0221407 x 10^23
print(type(avogadro_number)) 

# Boolean
is_today_rain = True
print(type(is_today_rain))

cost_iceBag = 1.25
is_ice_bag_expensive = cost_iceBag >=10
print(type(is_ice_bag_expensive))

# None
nothing = None
print(type(nothing))

# String
today = "Saturday"
print(type(today))

# we can use single quote or double for strings
my_movie = "One flew over the Cukoo's Nest"
print(my_movie)

# MultiLine String
ye_another_pun = """Son: "Dad, can you tell me what a solar eclipse is?"
Dad: "No sun"
"""
print(ye_another_pun)

# Checking Length of the String
print(len(my_movie))

# string can be converted into characters
multi_string = """a
b"""
# multiline string holds charcters like \n and \ thats why length
# of multi_string is 3

print(list(multi_string))

# Accessing individual charcters of a string
day = "Monday"
print(day[0])
# 0 included and 2 excluded
print(day[0:2])

# checking whether day occurs in string
print('day' in today)

# More Strings
# Joining Strings
full_name = "Munir"
greetings ='Hello'

print(greetings+full_name)
print(greetings + " " + full_name)

# String Functions
print(full_name.capitalize())
print(full_name.upper())
print(full_name.lower())
print(full_name.replace("Munir","Hamza"))
print("Sun,Mon,Tue".split(","))
# Removes before and after spaces
print(" Hello this is me  ".strip())

# String Format Function (replace placeholders with th variable values same as C lang)
# Input variables
cost_of_ice_bag = 1.25
profit_margin = .2
number_of_bags = 500

# Template for output message
output_template = """If a grocery store sells ice bags at $ {} per bag, with a profit margin of {} %, 
then the total profit it makes by selling {} ice bags is $ {}."""

print(output_template)

# Inserting values into the string
total_profit = cost_of_ice_bag * profit_margin * number_of_bags
output_message = output_template.format(cost_of_ice_bag, profit_margin*100, number_of_bags, total_profit)

print(output_message)

# Converting any data type var into string
print(type(str(num)))
print(str(20))

# Strings also supports Comparison Operators
first_name = "Munir"
print(first_name == "John")
print(first_name!="John")

# 2. Non-primitive Data Types

# List (can hold dif data types)
fruits = ['apple','mango','cherry']
print(type(fruits))

a_list = [23,'hello',None,3.14,fruits,3<=6]
empty_list = []

# Determine values in a list
print("Number of Fruits: ",len(fruits))

# Accessing values of a List
print(fruits[1])
print(fruits[-1])
print(a_list[2:4]) #4 index excluded
print(a_list[2:]) #display all
print(a_list[:4]) #display from start upto 4th

# Updating index of list
fruits[1] = 'Watermelon'
print(fruits)

# Adding elemet at the end of List
fruits.append('dates')

# adding value at specific index
fruits.insert(1,'banana')
print(fruits)

# remove a value from list
fruits.remove('banana')
print(fruits)

# pop method to remove specific index value
fruits.pop(0)
print(fruits)

# Combining Lists
more_fruits = ['apple','mango']
print(more_fruits+fruits)

# Checking if value occurs in list
print("apple" in fruits)

# Creating a copy of list
more_fruits_copy = more_fruits.copy()
print(more_fruits_copy)

# Modifying the copy doesn't affect original copy
more_fruits_copy.append('pineapple')
more_fruits_copy.pop(1)
print(more_fruits_copy)

# Reverse order of a list
original_list = [1, 2, 3, 4, 5]
original_list.reverse()
print(original_list)

# Add the elements of one list at the end of another list
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print("Combined list:", combined_list)

# Sort a list of strings in alphabetical order
unsorted_strings = ["banana", "apple", "orange", "grape"]
sorted_strings = sorted(unsorted_strings)
print("Sorted Strings: ",sorted_strings)


# Sort a list of numbers in decreasing order
unsorted_numbers = [5, 2, 8, 1, 3]
sorted_numbers = sorted(unsorted_numbers, reverse=True)
print("Sorted numbers (decreasing order):", sorted_numbers)

# Sort a list of numbers in Ascending order
asc_sorted_num = sorted(unsorted_numbers)
print("Sorted numbers (Increasing order):", asc_sorted_num)


# Tuple
# Trying to modify the tuple will result in an error
# student_info[0] = "Jane Smith"  # This line will raise a TypeError

# Creating a tuple to store a student's course grades
student_info = ("John Doe", [90, 85, 78, 92, 88])

# Accessing elements of the tuple
student_name = student_info[0]
grades = student_info[1]

# Displaying the student's name and grades
print("Student:", student_name)
print("Grades:", grades)

# built-in method of tuple
# Example of count() and index() methods with a tuple

# Creating a tuple
fruits = ("apple", "banana", "orange", "apple", "grape")

# Using count() method to count occurrences of an element
apple_count = fruits.count("apple")
print("Number of occurrences of 'apple':", apple_count)

# Using index() method to find the index of an element
orange_index = fruits.index("orange")
print("Index of 'orange':", orange_index)


# Dictionary
# A dictionary is an unordered collection of items. Each item stored in a dictionary has a key and value. 
# You can use a key to retrieve the corresponding value from the dictionary. Dictionaries have the type dict.

user1 = {
    'name' : 'Munir', #name is a key and written in single quotes
    'sex': 'Male',
    'age': 32,
    'married': True

}

print(type(user1))
print(user1)

# accessing dictionary values using their corresponding keys
print(user1['name'])
print(user1["married"])

# If a key isn't present in the dictionary, then a `KeyError` is *thrown*.
# user1['address']

# Other way to create Dictionary
user2 = dict(name = 'Munir',age=28, married=False)

# You can also use the get method to access the value associated with a key.
user2.get("name")

# You can check whether a key is present in a dictionary using the in operator.
'name' in user2

# You can change the value associated with a key using the assignment operator.
user2['married'] = True
print(user2["married"])

# The assignment operator can also be used to add new key-value pairs to the dictionary.
user1['address'] = '1, Penny Lane'
print(user1)

# To remove a key and the associated value from a dictionary, use the pop method.
user1.pop('address')

# Dictionaries also provide methods to view the list of keys, values, or key-value pairs inside it.
user1.keys()
user1.values()
user1.items()
