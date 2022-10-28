## Making some 'if' statements and things like that

ages = [14, 15, 16, 27, 62, 63, 65]

racers = ['matt', 'savanah', 'paul', 'scott', 'chuck']

## We've set our values, now let's play with them

for age in ages:
    if age < 16:
        print(f"Since you are {age}, your admission price is $5!")
    elif age >=16 and age < 63:
        print(f"You are {age}, your price for admission will be $15")
    else:
        print(f"Since you are {age}, your price is $7")

if 'matt' in racers:
    print("Matt is a racer.")
else:
    print("Matt is not a racer.")
if 'savanah' in racers:
    print("Savanah is a racer!")
else:
    print("Savanah is not a racer today.")
if 'jason' in racers:
    print("Jason is a racer as well.")
else:
    print("Jason will not be racing today.")

racers.append('jason')

if 'jason' in racers:
    print("Jason is now a racer as well.")
else:
    print("Jason will not be racing today.")