# Movie ticket prices based on age

prompt = "Welcome to Py Cinema!  Here to see a movie?"
prompt += "\nOur prices vary by age.  How old is each member of your party?"
prompt += "\n> "

prompt2 = "Excellent! Any others in your party?  We'll need their ages too."
prompt2 += "\nIf not, type 'done' and I'll get you your total."
prompt2 += "\n> "

prices = []

active = True

first = input(prompt)
int(first)

if int(first) <= 3:
    price = 0
elif int(first) <= 12:
    price = 10
else:
    price = 15

prices.append(price)

while active:
    message = input(prompt2)

    if message == 'done':
        active = False
        break
    elif int(message) <= 3:
        price = 0
    elif int(message) <= 12:
        price = 10
    else:
        price = 15

    int(price)
    prices.append(price)

total = sum(prices)

print(f"That's great! Your total comes to {total}")