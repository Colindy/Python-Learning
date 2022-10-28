# Simple input() snippet

# name = input("Please enter your name: ")
# print(f"Hello, {name.title()}")

# A bit more fancy but this gives a nice prompt

prompt = "Hello and welcome!  We have many fine activities!"
prompt += "\nPlease, provide for me your name and we can get started!"
prompt += "\n>: "

name = input(prompt)
print(f"\nHello, {name}! Glad to see you could make it!")

# Now we test an input for a number, and make it an integer

age = input(f"Say, {name}.  How old are you? ")
age = int(age)

print(f"So you're {age} years old huh?")

if age >= 21:
    print("You are old enough to drink!!  Wanna buy a round?")
else:
    print("Aww, so close to being able to buy everyone a round!")