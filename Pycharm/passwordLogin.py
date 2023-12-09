password = "Majnu@0101"
entries = ""
entries_count = 0
entries_limit = 3
cannot_login = False
while entries != password and not cannot_login:
    if entries_count < entries_limit:
        entries = input("Enter the password: ")
        entries_count += 1
    else:
        cannot_login = True
if cannot_login:
    print("foget password")
else:
    print("Logged in")
