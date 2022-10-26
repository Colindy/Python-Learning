## Dictionary loops

user1 = {
    'name': 'Cindy',
    'age': 37,
    'eyes': 'brown',
    }

for key, value in user1.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

## Printing just the keys from a Dictionary

for key in user1.keys():
    print(key)

    ##This can also be done like this and omit the '.keys()' method
for key in user1:
    print(key)