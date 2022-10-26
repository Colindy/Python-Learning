## users = ['admin', 'colindy', 'chris', 'cynthia', 'jon']
users = []

## Comment out the full list to use the empty list
## 'if users' checks to make sure there are users

if users:
    for user in users:
        if user == 'admin':
            print(f"Hello {user.title()}!  Would you like to see a status report.")
        else:
            print(f"Hello {user.title()}!  Thank you for logging in.")
else:
    print("We need some users!!")


## Here we'll put the ending on numbers correctly

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

for number in numbers:
    if number == '1':
        print("1st\n")
    elif number == '2':
        print("2nd\n")
    elif number == '3':
        print("3rd\n")
    else:
        print(f"{number}th\n")