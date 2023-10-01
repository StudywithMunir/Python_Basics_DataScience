#  Dictionary is an unordered collection of Items. Dictionary stores a (key, value) pair

marks = {"math" : 99, "chemistry" : 98, "physics" : 97}
print(marks)
print(marks["chemistry"])

marks["english"] = 95
print(marks)
marks["math"] = 96
print(marks)


#Iterating over a dictionary
# converting marks dictionary into a list so we can access each value stored in dictionary
mark_values = list(marks.values())

mark = 0
while(mark < len(mark_values)):
    print(f"Marks are: {mark_values[mark]}")
    mark+=1