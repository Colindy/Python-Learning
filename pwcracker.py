def test_password(pw):
	if pw=="mike12345":
		return 1
	else:
		return 0

cracked = 0
i = 1

while cracked == 0:
	test="mike" + str(i)
	cracked=test_password(test)
	i=i+1

print("Cracked Password: ", test)