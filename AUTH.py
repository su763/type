# auth.py

users = {
    "admin": "admin123",
    "user1": "password1"
}

def login():
    """Simple login function with username and password check."""
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if users.get(username) == password:
        print(f"Welcome, {username}!")
        return True
    else:
        print("Invalid credentials. Try again.")
        return False
