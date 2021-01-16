# Python's range() function makes it easy to generate a series of numbers
for value in range(1, 5):
    # The below prints 1 to 4 because python starts at the first value you give it, and stops at the second value and does not include it.
    print(value)

# To count to 5
for value in range(1, 6):
    print(value)
    
# You can also pass 1 argument 
for value in range(6):
    print(value) # prints values 0-5
    
# Using range to make a list of numbers
# If you want to make a list of numbers, you can covert the results of range() directly into a list using the list() function.

numbers = list(range(1, 6))
print(numbers)  # outputs [1, 2, 3, 4, 5]


# You can also use the range() function to tell python to skip numbers in a given range
# The third argument tells python to skip by 2
even_numbers = list(range(2, 11, 2))
print(even_numbers)  # outputs [2, 4, 6, 8, 10]
