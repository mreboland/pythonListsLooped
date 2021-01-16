# Tuples are a list of items that cannot change. Python refers to values that cannot change as immutable, and an immutable list is called a tuple.

# Tuples are defined like a list, except instead of using [] we use ()
# Defining a tuple
dimensions = (200, 50)
# accessing tuple data is the same as a list
print(dimensions[0])
print(dimensions[1])

# If we attempt to change a value of a tuple
# dimensions[0] = 250
# results in a type error.

# Tuples are technically defined by the presence of a comma the parentheses make them
# look neater and more readable. If you want to define a tuple with one element, you
# need to include a trailing comma:

my_t = (3,)

# It doesn’t often make sense to build a tuple with one element, but this can happen
# when tuples are generated automatically.

# Looping through all the values in a tuple

dimensions = (200, 50)
for dimension in dimensions:
    # Prints out just like a list
    print(dimension)

# Although we can't modify a tuple, we can assign a new value to a variable that represents a tuple.

# Defining the initial dimensions
dimensions = (200, 50)

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

# Associate a new tuple with the variable dimensions
# Python doesn't raise any errors because reassigning a variable is valid
dimensions = (400, 100)

print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

# When compared with lists, tuples are simple data structures. Use them
# when you want to store a set of values that should not be changed throughout
# the life of a program.

# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
# simple foods, and store them in a tuple.

foods = ("pasta", "sandwhich", "eggs", "toast", "pancakes")

# • Use a for loop to print each food the restaurant offers.

print("Original menu:")
for food in foods:
    print(food)

# • Try to modify one of the items, and make sure that Python rejects the
# change.

# foods[0] = "sausage"

# • The restaurant changes its menu, replacing two of the items with different
# foods. Add a line that rewrites the tuple, and then use a for loop to print
# each of the items on the revised menu.

foods = ("sausage", "sandwhich", "eggs", "crepes", "pancakes")

print("\nNew menu:")
for food in foods:
    print(food)