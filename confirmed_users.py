# Start with two lists, one for unconfirmed users
# and another for confirmed users

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Use a 'while' loop to confirm those users
# and move each user accordingly

while unconfirmed_users:
	current_user = unconfirmed_users.pop()

	print(f"Verifying user: {current_user.title()}")
	confirmed_users.append(current_user)

# Show the confirmed users
print("The following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())
