# Indenting unnecessarily

message = "Hello world!"
# avoid this error by indenting only when you have a specific reason to do so.
    # print(message)
    
# Indenting unnecessarily after the loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
    # Doing the below by accidentally indenting a sentence that should be left out of the loop is also a logical error. When don't want it printing for every iteration of the loop.
    print("Thank you everyone, that was a great magic show!")
    
# Forgetting the colon
# The colon in the for loop tell python that the next line is the start of a loop. If you forget it we get a syntax error.
# magicians = ['alice', 'david', 'carolina']
# for magician in magicians
#     print(magician)


# 4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these
# pizza names in a list, and then use a for loop to print the name of each pizza.

pizzas = ["pepperoni", "hawaiian", "meat lover"]

# for pizza in pizzas:
#     print(pizza)

# • Modify your for loop to print a sentence using the name of the pizza
# instead of printing just the name of the pizza. For each pizza you should
# have one line of output containing a simple statement like I like pepperoni
# pizza.

for pizza in pizzas:
    print(f"{pizza.title()} is the best kind of pizza!")

# • Add a line at the end of your program, outside the for loop, that states
# how much you like pizza. The output should consist of three or more lines
# about the kinds of pizza you like and then an additional sentence, such as
# I really love pizza!

print(f"\nPizza is the besttttttt food! There is nothing better than a pizza, regardless of whether it's breakfast, lunch, or dinner! \nI want to eat pizza all the time! Some of my favourites are {pizzas[0].title()}, {pizzas[1].title()}, and {pizzas[2].title()}!\n")

# 4-2. Animals: Think of at least three different animals that have a common characteristic.
# Store the names of these animals in a list, and then use a for loop to
# print out the name of each animal.

animals = ["dogs", "cats", "fish"]

for animal in animals:
    # print(animal)

# • Modify your program to print a statement about each animal, such as
# A dog would make a great pet.

    print(f"{animal.title()} make great pets!")

# • Add a line at the end of your program stating what these animals have in
# common. You could print a sentence such as Any of these animals would
# make a great pet!

print("\nAny of these animals would make a great pet!")
