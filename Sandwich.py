# Run through a list of sandwich's and mark them as made
# Also, have a way to remove one sandwich that ran out

sandwich = ['rye', 'pastromi', 'chicken', 'bacon', 'rye', 'bacon', 'chicken', 'rye']
done_sandwich = []

print(sandwich)

while 'rye' in sandwich:
    sandwich.remove('rye')

print("Sorry, we ran our of rye.")
print("\nWe'll be removing those from the orders.")

while sandwich:
    current = sandwich.pop()
    print(f"\nMaking {current} right now!!  Order up!")
    done_sandwich.append(current)

print(done_sandwich)
