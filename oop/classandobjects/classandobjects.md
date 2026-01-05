## **Class**

In object-oriented programming, a **Class** is a **blueprint** or **template** for creating objects. It is the logical representation that defines a set of attributes (data) and methods (functions) that the objects created from the class will have. A class does not occupy memory on its own. It's essentially a definition or a structure from which individual objects are instantiated.

For example, Consider the following code snippet representing an **Account** class:

**Python**

```python
class Account:
    def __init__(self):
        self.__balance = 0  # private attribute for balance
        self.account_number = ""  # public attribute for account number

    # Method to deposit money
    def deposit(self, amount):
        self.__balance += amount

    # Method to withdraw money
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount

    # Method to get balance
    def get_balance(self):
        return self.__balance
```

![Class and Objects](/images/classandobjects.png)

### **Keypoints:**

- *The **Account** class acts as a blueprint that has the set of attributes and methods defined in it providing a logical meaning to a real-world entity account.*
- *The **Account** class has a set of attributes (account_number and balance) and a set of methods (deposit, withdraw, getBalance) providing different functionality.*

## **Object**

An **object** is an instance of a class. When an object is created from a class, memory is allocated for it, and it holds the data as specified by the class. An object interacts with other parts of the program, and methods can be called and attributes accessed that belong to it.

For example, Consider the following code snippet demonstrating the creation of objects from the **Account** class:

**Python** 

```python
# Creating first Account object
acc1 = Account()
acc1.account_number = "ACC123"
acc1.deposit(5000)

# Creating second Account object
acc2 = Account()
acc2.account_number = "ACC456"
acc2.deposit(8000)

# Accessing attributes
print("Balance of", acc1.account_number, "is", acc1.get_balance())
print("Balance of", acc2.account_number, "is", acc2.get_balance())
```

### **Keypoints:**

- *The class by itself doesn't take any memory. It is the object that takes up the memory once initialized.*
- *The two objects (acc1 and acc2) have separate memory allocated for them even though they have the same attributes and methods.*
- *The code creates two separate objects(instances) of **Account Class** representing two separate bank accounts (ACC123 and ACC456).*

## **Attributes & Behaviours**

### **Attributes:**

Attributes (also called properties or fields) are the data or characteristics of an object. They represent the state of the object at any given moment. Attributes are typically defined within a class and can hold different types of information related to the object.

For example, In the **Account** class, there are two attributes: *account_number* and *balance*

### **Behaviours:**

Behaviors (also called methods or functions) are the actions or operations that an object can perform.

For example, In the **Account** class, there are three behaviours/methods: *deposit()*, *withdraw()* and *get_balance()*.

---

![Attributes and Behaviours](/images/classandobjects_01.png)

---

## **Creation of an object**

To create an object of the **Account** class in Java and Python, the following statement are used:

```python
// In Jave, Creating an object of Employee class
Employee obj1 = new Employee();

// In Python
obj1 = Employee()
```

### **Key Points:**

- ***Creating a new object:***
    - In Python, an object is created by calling the class like a function, for example:
        
        `emp1 = Employee()`
        
        This creates a **new instance** of the `Employee` class and automatically calls the class constructor (`__init__` method).
        
    - The actual object (instance) is stored in **heap memory**, because Python allocates all objects dynamically in the heap.
- ***Assigning the reference to the variable:***
    - `emp1` is a **reference variable** that points to the Employee object stored in the heap. When we write:
        
                                                      `emp1 = Employee()`
        
        we are storing the reference (memory address) of that newly created object in the variable `emp1`.
        
    - This reference variable (`emp1`) is stored in **stack memory**, because Python stores local variables and references on the stack.
    - The reference acts like a pointer - it simply holds the **memory address** of where the actual Employee object is located in the heap.

---

## **Deletion of an Object**

In Python, objects are also deleted automatically by the **Garbage Collector (GC)**. Python uses automatic memory management, meaning programmers do not manually delete objects. Instead, Python removes objects from memory when any variable **no longer references** them.

An object becomes eligible for deletion when **all references** pointing to it are removed or go out of scope. Once no variable refers to that object, Python’s garbage collector identifies it as unused and frees the memory. This prevents memory leaks and ensures efficient memory usage.

In practice, the programmer can *suggest* deletion by using:

```python
del obj
```

But this only deletes the **reference**, not the actual object.

If no other references exist, the garbage collector will automatically remove the object from the heap.

---

## **Understanding Stack and Heap Memory Allocation**

### **1. Stack Memory**

- *The stack is where primitive variables (such as int, double, and boolean) and references to objects (like obj1) are stored.*
- ***obj1** will hold the reference (memory address) of the object created by the new Employee().*
- *When the main method finishes executing, the stack memory associated with obj1 will be cleared, but the object in the heap will remain as long as references are pointing to it.*

### **2. Heap Memory**

- *The heap is where objects (instances of classes) are stored. The object created by the new Employee() is allocated memory in the heap.*
- *The Employee object will have its attributes (e.g., salary, employeeName) stored here.*
- *This memory will remain allocated as long as references are pointing to it. Once there are no more references to the object (i.e., the reference in the stack becomes null or goes out of scope), the object can be garbage collected.*

# Real Coding Scenario for Class and Object

Imagine you are designing a simple banking system where each customer has a separate bank account.To represent these accounts, you create an Account class, which acts as a blueprint for how every bank account should behave. Each account object will have two important attributes: the account number, which uniquely identifies the customer’s account, and the balance, which stores how much money the customer currently has. Along with these attributes, every account needs to perform basic banking operations, so you define two methods: deposit() and withdraw(). The deposit method allows customers to add money into their account by increasing their balance. For example, if the balance is 5,000 and a customer deposits 2,000, the new balance becomes 7,000. The withdraw method performs the opposite action—when customers want to take money out, this method subtracts the required amount from the balance, but only if they have enough funds. If a customer tries to withdraw more than the available balance, the method can display a warning message like “Insufficient funds.” Using this Account class, the bank can create multiple account objects—for example, one account for Mujeeb and another for Saif—each with its own independent balance and account number, but both following the same structure and rules defined in the class.

```python
"""
- banking system for account handling
- each user with seperate bank account
--- Account Class ---- Done
------- account number
------- balance
----------- deposit () allow user to add amount into their bankaccount
            user.deposit()
                current_balance += amount 
                5000 += 2000 user's new balance will be 7000
----------- withdraw() allow user to get money
            user.withdraw()
                current_balance -= amount 
                5000 -= 2000 user's new balance will be 3000
                LOGIC
                if withdraw_amount > current_balance
                    return Insufficient Funds
"""
class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Account with {self.account_number} deposited amount {amount}. Your new balance is {self.balance}")
        else:
            print("Depost Amount must be a positive integer")
        return self.balance
    
    def withdraw(self, amount):
        if amount < 0:
            print("WITHDRAW AMOUNT MUST BE POSITIVE")
        elif amount > self.balance:
            print("INSUFFICIENT FUNDS!")
            print("YOUR CURRENT BALANCE IS: ", self.balance)
        else:
            self.balance -= amount
            print(f"Account with {self.account_number} withdrawn with amount {amount}. Your new balance is {self.balance}")
        return self.balance
        
# Syntax
# objName = ClassName
print("Mujeeb's Information")
Mujeeb = Account("ACC1001", 10000)
print(Mujeeb.account_number)
print(Mujeeb.balance)
print(Mujeeb.deposit(100000))
print(Mujeeb.withdraw(1000))
print(id(Mujeeb))

print("===================")
print("Saif's Information")
Saif = Account("ACC1002", 20000)
print(Saif.account_number)
print(Saif.balance)
print(Saif.deposit(100))
print(Saif.withdraw(20000))
print(id(Saif))
```