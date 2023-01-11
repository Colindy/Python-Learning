#A simple program to evaluate a rental car need.


need = input("What make of car are you looking to rent? ")

if need.lower() == 'chevy':
    print(f"We have a {need.title()} for you right here!")
elif need.lower() == 'mazda':
    print(f"We have a {need.title()} right this way!")
elif need.lower() == 'ford':
    print(f"We have a {need.title()} in the back I believe.")
else:
    print(f"Not sure we have any {need.title()}s.")