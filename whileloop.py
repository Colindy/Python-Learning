# A simple loop with an out

# Prompt created for the user
prompt = "Tell me anything at all and I will repeat it back."
prompt += "\nType 'quit' to end the program. "

# Variable assigned to what the user typed in
message = ""

# While loop to print as long as the user wants to print
#while message != 'quit':
#    message = input(prompt)
#
#    if message != 'quit':
#        print(message)

# Comment out the part above this
# because I can use a 'flag' instead, like this

# Using 'active' as the flag, we can set it to true
# As long as it's true, the loop will run.
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)