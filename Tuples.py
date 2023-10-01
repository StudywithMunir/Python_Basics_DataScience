#They are like lists (sequence of objects) but they are immutable i.e. once they have been
 #defined we cannot change them.

marks = (95, 98, 97, 97)
 #marks[0] = 98
print(marks.count(97)) #check how many time 97 appear
print(marks.index(97)) #find index of 97


mark = 0 #mark counter is set to 0
while(mark < len(marks)): #0 < 4(length of marks)
     print(f"Marks are: {marks[mark]}") #prints the marks value that was on 0th index

     #then mark incremented
     mark = mark + 1