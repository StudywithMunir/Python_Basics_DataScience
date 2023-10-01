friends=["amar","akbar","anthony"]
print(friends[0])
print(friends[1])
print(friends[-1]) #returns anthony bcz -ve values start from right to left and 0 is excluded
print(friends[-2])
friends[0]="aman"
print(friends)
print(friends[0:2])#returns a new list

#return all friends
for friend in friends:
 print(friend)