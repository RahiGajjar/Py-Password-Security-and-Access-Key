import re
import getpass

class User:
    def __init__(self, username, password, access_level):
        self.username = username
        self.password = password
        self.access_level = access_level
    
    def is_password_strong(self):
        # Password must be at least 8 characters
        if len(self.password) < 8:
            print("Password must be minimum of 8 characters.")
            return False
        
        # Check for uppercase letter
        if not re.search(r"[A-Z]", self.password):
            print("Password must have at least one uppercase letter.")
            return False
        
        # Check for lowercase letter
        if not re.search(r"[a-z]", self.password):
            print("Password must have at least one lowercase letter.")
            return False
        
        # Check for digit
        if not re.search(r"\d", self.password):
            print("Password must have at least one digit.")
            return False
        
        # If all conditions pass
        return True
    
    def verify_password(self, verify_password):
        return self.password == verify_password
    
    def grant_access(self):
        if self.access_level == "basic":
            print(f"User {self.username} has been granted basic access.")
            print("Basic access allows reading and reviewing files on the desktop.")
        elif self.access_level == "escalated":
            print(f"User {self.username} has been granted escalated access.")
            print("Escalated access allows reading and reviewing files on the desktop and downloads folder.")
        # Add other access levels and their respective permissions here

# Main program
while True:
    username = input("Enter Your Username: ")
    password = getpass.getpass("Enter Your Password: ")

    user = User(username, password, "basic")  # Default to basic access

    if user.is_password_strong():
        verify_password = getpass.getpass("Please re-enter your password to verify: ")

        if user.verify_password(verify_password):
            secret_password = getpass.getpass("Enter the secret password to escalate privileges (or enter to skip): ")

            if secret_password == "GrantMeAces$$":
                user.access_level = "escalated"
                user.grant_access()
            else:
                user.grant_access()
            break
        else:
            print("Passwords do not match. Please try again.")
    else:
        print("Please choose a stronger password.")
