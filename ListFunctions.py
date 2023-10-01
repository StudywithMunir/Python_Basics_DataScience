marks=["english",95,"chemistry",98]
marks.append("physics") #add new value in a list
marks.append(97)
print(marks)

marks.insert(0,"math") #insert new value at specific position
marks.insert(1,99)
print(marks)

print("math"in marks) #check if math is present in marks list or not

print(len(marks)/2) #to print length of a list
marks.clear() #to clear a list
print(marks)


i=0
while i<len(marks):
 print(marks[i])
 print(marks[i+1])
 i=i+2
