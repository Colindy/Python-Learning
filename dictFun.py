## Here we set two dictionaries, Chris and Cindy.

Chris = { 'age' : 40, 'hair' : 'brown', 'height' : '6 ft'}
Cindy = { 'age' : 36, 'hair' : 'brown', 'height' : '5 ft 2 in'}

## Let's print these two dictionaries

print(Chris)
print(Cindy)

## Now lets do some things with these dictionaries

chris_age = Chris['age']

## Now that a variable is set, lets try something
## I can print like this...

print(f"Chris is {chris_age} years old")

## Or I can print like this without the need for the variable

print(f"Chris is {Chris['age']} years old")

cindy_age = Cindy['age']
print(f"Cindy is {cindy_age} years old")

## Now lets add some values to the dictionaries

Chris['eye_color'] = 'green'
Cindy['eye_color'] = 'brown'

## And print them again

print(Chris)
print(Cindy)

## Now we're going to modify one of the aspects from each dictionary

print(Chris['hair'])

## Now we modify that like this

Chris['hair'] = 'red'

print(Chris['hair'])

## Now we remove an aspect of one of the dictionaries

print(Chris)

del Chris['hair']

print(Chris)

## I can also use the .get() function to specify what to do if there is no value assigned to a key

print(f"The value for key 'Shoes' is: {Chris.get('shoes', 'No value assigned')}")