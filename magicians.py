# Looping through an entire list
# When you want to do the same action with every item in a list, you use a for loop

# Printing out each name
magicians = ["alice", "david", "carolina"]
# The below reads out as "for every magician in the list of magicians, print the magician's name".
# The loop runs for ever item in the list regardless of if it's 3 or 3 million
# The variable, magician can be named whatever you want
for magician in magicians:
    print(magician)
    
# We can expand on the loop by printing a message to each magician.
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    # anything indented within the loop is apart of that loop
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
    
# Doing something after a for loop is finished.
# Once the above loop is completed (runs 3 times), the below print statement will only run once as it's not apart of the loop
print("Thank you everyone. That was a great magic show!")

# Indentation errors
# A big problem with python is indentation. Python forces indents in order to make code easy to read. However if proper indentation isn't followed python will break.

# Example:
# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
# The below will give an indentation error as it doesn't follow the proper python rules.
# print(magician)

# Another common issue is forgetting to indent additional lines. This will cause the for loop to run but can give odd results

magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
# Because the below wasn't indented, the loop runs through the above print() 3 times then only prints the below print once, at the end as it's not included within the loop. This is called a logical error.
print(f"I can't wait to see your next trick, {magician.title()}.\n")
