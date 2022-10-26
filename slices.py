coworkers = ["derrick", "renee", "david", "anthony", "james"]

# I can print indexed 'slices' like this

print(coworkers[0:3])

# I can also do it like this

print(coworkers[1:4])

# I can even use this syntax

print(coworkers[-3:])

# Here, we're taking that and looping through to get the first 3 items

for coworker in coworkers[:3]:
    print(coworker.title())