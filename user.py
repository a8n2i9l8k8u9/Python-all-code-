username = input("Please enter your username: ")
password = input("Please enter your password: ")

username_password = {
    'Mert': "mertt"
}

if username in username_password:
    if username == "Mert" and password == username_password[username]:
        print("Welcome Sir")
    else:
        print("You're not authorized!")
else:
    confirmation = input("Do you want to register? (Y/N): ")
    if confirmation == "Y":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        password_2 = input("Confirm your password: ")
        if password == password_2:
            username_password[username] = password
        else:
            print("Your password is incorrect!")
    else:
        print("Good bye")
print(username_password)
