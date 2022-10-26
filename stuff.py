stuff = []

print("First, we start with a list.")
print(stuff)
print("Then, we add some things to it and print it again.")

stuff.append("thing 1")
stuff.append("thing 2")
stuff.append("thing 3")

print(stuff)

print("Now, we'll add one more thing and then print once more.")

stuff.append("thing 4")

print(stuff)

print("Now, to pop an item off and view that popped item.")

popped_item = stuff.pop()

print("Here's the list after a popped item.")
print(stuff)
print("Here's the popped item.")
print(popped_item)

print("We can also remove items via index number.")
del stuff[1]
print(stuff)
print("I can also delete the item by specific name.")
stuff.remove("thing 1")
print(stuff)

print("Now that we're down to 1 item, need to add more.")

stuff.append("thing 5")
stuff.append("thing 6")
stuff.append("thing 7")
print(stuff)

print("Now I can also pop specific items, like this...")
spec_pop = stuff.pop(2)
print("Here's the new list.")
print(stuff)
print(f"And the item we popped from a specific spot was {spec_pop}.\n")
print("Now I want to list out the items in a list but don't want a lot of code.")
for thing in stuff:
    print(thing)

for thing in stuff:
    print(f"This is {thing}!")

print("Let's have some fun...xD")

for value in range(5,101, 5):
    print(value)