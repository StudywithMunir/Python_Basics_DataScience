students=["ram","shyam","kishan","radha","radhika"]

#if the loop find radha it will break the loop kind of searching
for student in students:
 if(student == "radha"):
  break
print(student)

#If loop find kishan it will skip kishan
for student in students:
 if(student == "kishan"):
  continue
 print(student)
