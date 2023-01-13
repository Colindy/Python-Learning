# Pizza toppings loop that will store items entered

# Create the prompt to ask about toppings
prompt = "Thank you for chosing Py Pizza."
prompt += "\nWhat toppings would you like on your py?"
prompt += "\n: "

prompt2 = "We'll get that added."
prompt2 += "\nAnything else for you? Type 'done' if not."
prompt2 += "\n: "

# Create a dictionary to store the toppings
toppings = []

# Set the loop out cause this way is neat to me
active = True

# Get the first pizza topping
first = input(prompt)

# Add that topping to the list of toppings
toppings.append(first)

# Gather the rest of the items for the Py ;)
while active:
    message = input(prompt2)

    if message == 'done':
        active = False
    else:
        toppings.append(message)

# Tell them what they ordered
print(f"Your toppings include: {toppings}")