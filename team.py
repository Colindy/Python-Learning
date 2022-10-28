## These are the lists that I'm working with for a random bs program :D
names = ["derrick jones", "renee eubanks", "chris nellinger"]
sw_chars = ["darth maul", "obi wan kenobi", "ahsoka tano"]
fruits = ["apple", "orange", "pear", "peach", "grape", "apricot", "blueberry"]


## Here are the different things I'm learning to do with lists :)

print("This is what happens if you just print the list...")
print(names)
print(sw_chars)
print("Now, here are some list manipulations!\n")
print(f"{names[1].title()} is the team lead in Indy.")
print(f"{names[0].title()} has been here the second longest.")
print(f"{names[2].title()} is the noob, having been here less than a year.")
print("\n")
print(f"{sw_chars[0].title()} is a Sith and he got cut in half by the Jedi, {sw_chars[1].title()}!")
print(f"{sw_chars[0].title()} also fought (and lost to) {sw_chars[2].title()} who also happens to be {names[2].title()}'s favorite character!")

print("Now we're going to manipulate some of these lists.")
leaving = names.pop(1)
print(f"If {leaving.title()} gets this promotion then only {names[0].title()} and {names[1].title()} left.")
print(names)
names.append("brian short")
print(f"If that does happen, {names[1].title()} hopes he can get {names[2].title()} the backfill spot.")
print(names)

## Now we're going to check for some conditions in a list

print(fruits)
if 'apricot' or 'strawberry' in fruits:
    print("The list contains either 'apricot' OR 'strawberry'.")

print("Does the fruit list have 'banana' in it?")
print('banana' in fruits)

## Let's see if it works in a simpler way...

print("Does the fruits list contain apple?\n", 'apple' in fruits)