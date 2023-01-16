# A while loop to run through and remove
# specific items in a list

# First, set a list of pets
pets = ['cat', 'dog', 'bird', 'cat', 'dog', 'cat', 'lizard']

# Print the list so you can compare it later
print(pets)

# Run the loop to remove one item, in this case 'cats'
while 'cat' in pets:
    pets.remove('cat')

# Now check that the loop worked
print(pets)
