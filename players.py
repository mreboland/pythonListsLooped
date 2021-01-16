# Working with a specific part of a list is called slice
# To slice a list we need a start and end point. Like range() the slice does not include the second parameter.
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])  # outputs ['charles', 'martina', 'michael']

# for 2nd, 3rd, and 4th people
print(players[1:4])  # outputs ['martina', 'michael', 'florence']

# if you omit the first value, python starts at the beginning
print(players[:4])  # outputs ['charles', 'martina', 'michael', 'florence']

# If you want to start at a specific spot and slice to the end of the list
print(players[2:])  # outputs ['michael', 'florence', 'eli']

# Using negative numbers we can output for example, the last three people on the list
print(players[-3:])  # outputs ['michael', 'florence', 'eli']

# You can include a third value in the brackets indicating a slice. If a third value is
# included, this tells Python how many items to skip between items in the specified
# range. Similar to the third value in range.

# Looping through a slice
# You can use a slice in a for loop if you want to loop through a subset of elements in a list.
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team:")
# instead of looping through the entire list, using slice we can just loop through the first 3 names
for player in players[:3]:
    print(player.title())
    
