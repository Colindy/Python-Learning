# A check to see if a number is a multiple of 10

num = input("Pick a number, any number: ")
num = int(num)

if num % 10 == 0:
    print("This number is a multiple of 10.")
else:
    print("This number is NOT a multiple of 10.")
