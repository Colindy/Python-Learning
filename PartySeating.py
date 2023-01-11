# A check for restaurant seating

party = input("Hello!  How many will be dining with us today? ")
party = int(party)

if party >= 8:
    print("We will need a moment to get a table ready for you.")
else:
    print("We have a table ready! Right this way.")
