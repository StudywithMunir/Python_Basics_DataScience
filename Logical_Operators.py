my_favorite_number = 1
a_neutral_number = 3

# And Operator (Both conditions needs to be True)
print(my_favorite_number > 0 and my_favorite_number <= 3)
print(my_favorite_number > 0 and my_favorite_number >= 3)

# Or Operator (At Least One Condition is True)
print(a_neutral_number == 3 or my_favorite_number < 0)
print(a_neutral_number != 3 or my_favorite_number < 0)

# NOT Operator gives negative result(make false from true or true to false)
print(not a_neutral_number == 3)
print(not my_favorite_number < 0)
