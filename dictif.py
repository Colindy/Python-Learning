## if statement for a dictionary

dict1 = {'eyes': 'green', 'hair': 'brown', 'skin': 'white'}
dict2 = {'eyes': 'red', 'hair': 'black', 'skin': 'red'}

if dict2['skin'] == 'red':
    print("Seems like you got some sun!")
elif dict2['skin'] == 'orange':
    print("Went with that spray tan didn't ya?")
elif dict2['skin'] == 'green':
    print("You feelin ok?")
else:
    print("I'm not sure what to say to you.")


