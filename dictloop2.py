## We need a big dictionary to work with.

fav_lang = {
    'kevin': 'c',
    'chris': 'python',
    'andy': 'ruby',
    'bryan': 'bash',
    'cindy': 'python',
    'eric': 'java',
    }

##  Now we can do some things with it.

## We can make a list

friends = ['chris', 'bryan', 'cindy']

##  Now we do our loop

for name in fav_lang.keys():
    print(f" Hi, {name.title()}!")

        ## Then we reference our language list with our friends list and give a little extra
        
    if name in friends:
        language = fav_lang[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
            
## Now we do a sorted loop with the same list and see how the output differs.

print("\nGet in a line, nice and orderly!!\n")

for name in sorted(fav_lang.keys()):
    print(f" Hi, {name.title()}!")

        ## Then we reference our language list with our friends list and give a little extra
        
    if name in friends:
        language = fav_lang[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
            

print("\nThose were the keys, now I just want the values of each.\n")

for value in fav_lang.values():
    print(f"{value.title()}")

print("\nBut, in an orderly fashsion.\n")

for value in sorted(fav_lang.values()):
    print(f"{value.title()}")