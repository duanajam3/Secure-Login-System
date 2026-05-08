import bcrypt

# Simulated user database (username : hashed_password)
users = {}

# Function to register user
def register():
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Hash the password
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Store in "database"
    users[username] = hashed
    print("User registered successfully!\n")

# Function to login user
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users:
        stored_password = users[username]

        # Check password
        if bcrypt.checkpw(password.encode('utf-8'), stored_password):
            print("Login successful ✅")
        else:
            print("Incorrect password ❌")
    else:
        print("User not found ❌")

# Main menu
while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        break
    else:
        print("Invalid option")