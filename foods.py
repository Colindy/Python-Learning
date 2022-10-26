my_foods = ["pizza", "cheesecake", "ice cream", "burger"]
friend_foods = my_foods[:]

print("My favorite foods are:")
for food in my_foods[:]:
    print(food)

print("\nMy friend's favorite foods are:")
for food in friend_foods[:]:
    print(food)

my_foods.append("apple crisp")
my_foods.append("apple pie")
friend_foods.append("tomato soup")
friend_foods.append("red vines")

print("But wait, we've got more to add.")

print(my_foods)
print(friend_foods)

print("\nI added:")
for food in my_foods[4:]:
    print(food)

print("\nMy friend added:")
for food in friend_foods[4:]:
    print(food)