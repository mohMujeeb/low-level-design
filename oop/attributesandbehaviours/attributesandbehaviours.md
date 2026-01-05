## **Attributes and Methods**

## **Attributes**

Attributes (also called properties or fields) are the data or characteristics of an object. They represent the state of the object at any given moment. Attributes are typically defined within a class and can hold different types of information related to the object.

### **Example: BankAccount Class**

We wish to create two data fields for our `BankAccount` class:

- **Name:** to store the name of the account holder. The `String` data-type would be best suited for it.
- **Balance:** to store the account balance. The `double/integer` data-type would be the perfect fit for this.

Since the attribute **balance** is a personal information of the account holder, in a real-world scenario these things will be hidden from the outside world, i.e., no user will be able to check the account balance of a different user.

To handle such cases, the **balance** attribute must be declared with restricted access.

In **Python**, this is achieved using **name mangling (`__balance`)**, which serves the same purpose as `private` in other languages.

## **Methods**

Methods are functions that are defined inside a class and represent the behavior or actions that an object of the class can perform. Methods define what an object can do, and they often operate on the attributes (or fields) of the class.

Every object of a class can call the methods of the class to perform specific tasks.

### **Example Methods in a BankAccount Class**

- **Check Balance:** The user can check the account balance.
- **Deposit:** The user can deposit a certain amount.
- **Withdraw:** The user can withdraw money from his/her bank account.

**Python**

```python
from typing import List

class BankAccount:
    def __init__(self, name, balance):
        self.__name = name  # to store the name of account holder
        self.__balance = balance  # to store the balance

    # Method to set the name
    def setName(self, name):
        self.__name = name

    # Method to get the name
    def getName(self):
        return self.__name

    # Method to get the balance
    def getBalance(self):
        return self.__balance

    # Method to make a deposit
    def deposit(self, amount):
        self.__balance += amount  # Update the balance

    # Method to make a withdrawal
    def withdrawal(self, amount):
        if amount >= self.__balance:
            print("Insufficient amount")
            return False
        self.__balance -= amount  # Update the balance
        return True

```


## **Understanding the Interaction Between Attributes and Methods**

In a class implementing a real-world scenario, the attributes and methods interact with each other constantly. Methods allow controlled access to the attributes.

In many cases, attributes are marked as private to restrict direct access from outside the class, promoting **encapsulation**.

### **Example**

The `balance` attribute was set as private in the `BankAccount` class.

Now, in order to get the balance, there must be some method implemented that can access the private attribute. This brings the two major methods used in real-world OOP projects:

- **Setters:** A method to set the value of a particular attribute, e.g., `setName()`
- **Getters:** A method to get or retrieve the value of a particular attribute, e.g., `getName()`

These methods are necessary because they provide users access to private data attributes which otherwise cannot be accessed directly from the object.

## **Important Points**

Some important points must be taken care of while implementing real-world entities using Object-Oriented Programming:

- **Accessing Attributes:**
    
    Use methods (getters and setters) to access private attributes.
    
    Example: `getBalance()` retrieves the current balance.
    
- **Encapsulation:**
    
    Keep attributes private and provide controlled access using public methods to ensure data integrity.
    
- **Default Values:**
    
    Attributes have default values if not explicitly initialized
    
    (e.g., `0` for numeric types, `None` for objects in Python).
    
- **Method Parameters:**
    
    Methods can take parameters to modify attributes
    
    (e.g., `deposit(amount)`).
    
- **Error Handling:**
    
    Ensure methods validate inputs
    
    (e.g., disallow negative deposits or withdrawals exceeding balance).