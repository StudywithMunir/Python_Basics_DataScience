# Example Problem 1:
# A grocery store sells a bag of ice for $1.25 and makes a 20% profit. 
# If it sells 500 bags of ice, how much total profit does it make?

price_of_ice_bag = 1.25
profit_margin = .2
total_bags = 500
total_profit = total_bags * (profit_margin*price_of_ice_bag)

print(total_profit)

# assign values to multiple variables in a single statement
color1, color2, color3 = "red", "green", "blue"

# assign the same value to multiple variables by chaining multiple assignment operations within a single statement.

color4 = color5 = color6 = "magenta"


# While reassigning a variable, you can also use the variable's previous value to compute the new value.
counter = 10
counter = counter + 1
print(counter)


# The pattern var = var op something (where op is an arithmetic operator like +, -, *, /) is very common, 
# so Python provides a shorthand syntax for it.
counter = 12
counter+=1
print(counter)