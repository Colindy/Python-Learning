prompt = "\nPlease enter the name of a city you ahve visited"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

# This loop uses a 'break' statement to exit the loop