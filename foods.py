# Copying a list
# To copy a list, you can make a slice that includes the entire original list by omitting the first and second index ([:])

myFoods = ['pizza', 'falafel', 'carrot cake']
# copying original list
friendFoods = myFoods[:]

# Both print out the same list
print("My favourite foods are:")
print(myFoods)

print("\nMy friend's favourite foods are:")
print(friendFoods)


# proof that the lists are different and not tied to each other
myFoods.append("cannoli")
friendFoods.append("ice cream")

print("My favorite foods are:")
print(myFoods)
print("\nMy friend's favorite foods are:")
print(friendFoods)

# If we were to try to do friendFoods = myFoods it would associate friendFoods with the original list. This means that any changes done to friendFoods would affect myFoods and vice versa

my_foods = ['pizza', 'falafel', 'carrot cake']

# This doesn't work:
friend_foods = my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')

# outputs are now the same when they should be different
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)


# 4-10. Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:

players = ['charles', 'martina', 'michael', 'florence', 'eli']

# • Print the message The first three items in the list are: . Then use a slice to
# print the first three items from that program’s list.

print("The first three players are:")
for player in players[:3]:
    print(player.title())

# • Print the message Three items from the middle of the list are: . Use a slice to
# print three items from the middle of the list.

print("\nThe middle three players are")
for player in players[1:4]:
    print(player.title())


# • Print the message The last three items in the list are: . Use a slice to print the
# last three items in the list.

print("\nThe last three players are")
for player in players[2:]:
    print(player)

# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
# (page 56). Make a copy of the list of pizzas, and call it friend_pizzas.

myPizzas = ["pepperoni", "hawaiian", "meat lover"]
friendsPizzas = myPizzas[:]

# Then, do the following:
# • Add a new pizza to the original list.

myPizzas.append("canadian")

# • Add a different pizza to the list friend_pizzas.

friendsPizzas.append("cheese")

# • Prove that you have two separate lists. Print the message My favorite
# pizzas are: , and then use a for loop to print the first list. Print the message
# My friend’s favorite pizzas are: , and then use a for loop to print the second
# list. Make sure each new pizza is stored in the appropriate list.

print("\nMy favourite pizzas are:")
for pizza in myPizzas:
    print(pizza.title())

print("\nMy friend's favourite pizzas are:")
for pizza in friendsPizzas:
    print(pizza.title())

# 4-12. More Loops: All versions of foods.py in this section have avoided using
# for loops when printing to save space. Choose a version of foods.py, and
# write two for loops to print each list of foods.

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("\nMy favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)
