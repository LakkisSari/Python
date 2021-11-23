password_set = False
while not password_set:
    count = 0
    password = input("Enter a password: ")
    for x in password:
        count = count + 1
    if count < 8:
        print("Your password size must be at least 8 characters!")
    else:
        password_set = True
print("Your password is accepted!")