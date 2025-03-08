#/usr/bin/python3
# Set a correct password
correct_password = "secure123"

# Number of attempts
attempts = 3

# Loop to allow the user to enter the password
for attempt in range(attempts):
    entered_password = input("Enter your password: ")
    
    # Check if the entered password is correct
    if entered_password == correct_password:
        print("Access Granted!")
        break
    else:
        # If not correct, give the user another chance
        if attempt < attempts - 1:
            print("Incorrect password. Try again.")
        else:
            print("Access Denied!")
