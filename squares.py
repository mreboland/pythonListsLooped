# More examples of creating numbers with range()
# Using exponents

squares = []

for value in range(1, 11):
    # take each value from 1 to 10 and square it. 
    square = value ** 2
    # add the value of the squared value to the list squares.
    squares.append(square)
    
print(squares)  # outputs [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# We can write the above code more concisely:
squares = []

for value in range(1, 11):
    squares.append(value ** 2)
    
print(squares)

# Simple statistics with a list of numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))


# List comprehension allow you to generate code using just one line
# Using the previous squares example
# We create a list and within the square brackets we first define an expression (value**2) we then define the loop values omitting the :
squares = [value ** 2 for value in range(1, 11)]
print(squares)  # outputs [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
# inclusive.

for value in range(1, 21):
    print(value)

# 4-4. One Million: Make a list of the numbers from one to one million, and then
# use a for loop to print the numbers. (If the output is taking too long, stop it by
# pressing ctrl-C or by closing the output window.)

millions = []

for value in range(1, 1000000):
    millions.append(value)
    # print(value)


# 4-5. Summing a Million: Make a list of the numbers from one to one million,
# and then use min() and max() to make sure your list actually starts at one and
# ends at one million. Also, use the sum() function to see how quickly Python can
# add a million numbers.

millions = [value for value in range(1,1000001)]
print(min(millions))
print(max(millions))
print(sum(millions))

# 4-6. Odd Numbers: Use the third argument of the range() function to make a
# list of the odd numbers from 1 to 20. Use a for loop to print each number.

oddNumbers = []

for value in range(1, 21, 2):
    oddNumbers.append(value)
    print(value)

# 4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
# print the numbers in your list.

threes = []

for value in range(3, 31, 3):
    threes.append(value)
    print(value)

# 4-8. Cubes: A number raised to the third power is called a cube. For example,
# the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes(that
# is, the cube of each integer from 1 through 10), and use a for loop to print out
# the value of each cube.

cubed = []

for value in range(1, 11):
    cubed.append(value ** 3)
    print(value ** 3)

# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the
# first 10 cubes.

cubedTwo = [value ** 3 for value in range(1, 11)]
print(cubedTwo)
