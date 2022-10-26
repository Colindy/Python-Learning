## First create a blank list

squares = []

# Then we create our 'for' loop and have it ammend the list

for value in range(1, 11):
    squares.append(value ** 2)

## And finally we print the list

print(squares)

# Afterwards, we can do different things with the list of numbers

minimum = min(squares)
print(minimum)
maximum = max(squares)
print(maximum)
total = sum(squares)
print(total)