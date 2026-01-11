""" 
Use Case: Encapsulation in an E-commerce Platform

Scenario:

In an e-commerce system, we have User Accounts with sensitive information like passwords, email, and purchase history. 
We don’t want other parts of the system to access or modify these directly. Instead, we provide controlled access 
using methods (getters and setters). This is classic encapsulation.

Requirements:

Store user information: name, email, password, and purchase history.

Hide sensitive fields like password and purchase_history from direct access.

Provide controlled access:

Verify password before showing purchase history.

Allow updating email after validation.

Prevent accidental modification of critical fields."""

class User:
    def __init__(self, name, email, password):
        self.__name = name                  # Private attribute
        self.__email = email                # Private attribute
        self.__password = password          # Private attribute
        self.__purchase_history = []        # Private list of purchases

    # Getter for name (read-only)
    @property
    def name(self):
        return self.__name

    # Getter for email
    @property
    def email(self):
        return self.__email

    # Setter for email with basic validation
    @email.setter
    def email(self, new_email):
        if "@" in new_email and "." in new_email:
            self.__email = new_email
            print(f"Email updated to {new_email}")
        else:
            print("Invalid email address!")

    # Method to verify password
    def verify_password(self, password):
        return self.__password == password

    # Method to add purchase (controlled access)
    def add_purchase(self, item):
        self.__purchase_history.append(item)
        print(f"Added '{item}' to purchase history.")

    # Method to get purchase history (password required)
    def get_purchase_history(self, password):
        if self.verify_password(password):
            return self.__purchase_history
        else:
            return "Access Denied: Incorrect Password"

    # Method to change password (controlled access)
    def change_password(self, old_password, new_password):
        if self.verify_password(old_password):
            self.__password = new_password
            print("Password changed successfully.")
        else:
            print("Incorrect current password! Password not changed.")

# **Usage of Encapsulation**
if __name__ == "__main__":
    user1 = User("Alice", "alice@example.com", "secure123")

    # Access name (allowed)
    print("User Name:", user1.name)

    # Update email (validated)
    user1.email = "alice.new@example.com"
    user1.email = "alice_new_example.com"  # Invalid

    # Add purchases
    user1.add_purchase("Laptop")
    user1.add_purchase("Headphones")

    # Try to access purchase history with wrong password
    print(user1.get_purchase_history("wrongpass"))  # Access Denied

    # Correct password access
    print("Purchase History:", user1.get_purchase_history("secure123"))

    # Change password
    user1.change_password("secure123", "newpassword")
    print(user1.get_purchase_history("secure123"))   # Old password fails
    print(user1.get_purchase_history("newpassword")) # Works
