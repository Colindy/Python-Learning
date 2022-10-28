# Store information about a pizza being ordered

pizza = {
    'crust': ['thick'],
    'toppings': ['mushrooms', 'extra cheese'],
    'extra1': ['stuff', 'to', 'make'],
    'extra2': ['this', 'code', 'work'],
    }

# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza\n with the following toppings:")

# Print out the toppings in a loop
for topping in pizza['toppings']:
    print(f"\t{topping}")


# Now going to print out the items of each dictionary value

for spot, things in pizza.items():
    print(f"\n{spot} has these items:")
    for thing in things:
        print(f"\t{thing}")