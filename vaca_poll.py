# Filling a dictionary with user input

# First, create a dictionary to store the responses
responses = {}

# Set a flag to trip if we need to exit the loop
active = True

# Here we make the loop
while active:
    # Get a user's name and response and set it to a variable
    name = input("What is your name? ")
    spot = input("What is your favorite vacation destination? ")

    # Here, we store the response
    responses[name] = spot

    # Now to check if anyone else needs to poll and
    # exit if not
    repeat = input("Is there another person to respond? yes/no ")
    if repeat == 'no':
        active = False

# Now we print the results
print("\n*********POLL RESULTS**********")
for name, spot in responses.items():
    print(f"{name} would like to go to {spot}!")
