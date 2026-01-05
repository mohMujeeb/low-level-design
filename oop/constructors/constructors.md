## **Constructor**

A constructor is a **special method** in a class designed to initialize an object when it is created. It ensures that the object is set up with the required attributes and state before it is used.

In **Python**, the constructor is defined using the special method `__init__()`.

Consider the following example to understand the syntax and working of Constructors:

**Python** 

```python


class Employee:
    def __init__(self):
        self.__salary = 5000  # to store the salary of employee
        self.employeeName = "John Doe"  # to store the name of employee

    # Method to set the employee name as given input
    def setName(self, employeeName):
        self.employeeName = employeeName

    # Method to set the salary as given input
    def setSalary(self, val):
        self.__salary = val

    # Method to get the salary of the employee
    def getSalary(self):
        return self.__salary

# Main Class
if __name__ == "__main__":
    # Creating an object of Employee class
    obj = Employee()

    # Attributes of object initialized by the constructor
    print("Default values initialized by the constructor:\n")
    print("Employee Name:", obj.employeeName)
    print("Salary:", obj.getSalary())
```


## **Keypoints**

- **Syntax:** In Python, a constructor is defined using the `__init__()` method.
- A constructor is automatically called when an object is created.
- If no constructor is written, Python automatically provides a **default constructor.**

## **Purpose of Constructor**

There are three major purposes behind creating a constructor for a class:

- **Object Initialization:**
    
    Constructor helps in initializing an object at the time of creation by assigning default or user-defined values to object attributes.
    
- **Code Reusability:**
    
    Every time an object is created, the same code is reused, preventing writing multiple lines of code to initialize different objects.
    
- **Ensures Default Value:**
    
    Ensures that the object is always started in a default state when initiated.
    

## **Types of Constructor**

There are three different types of constructors:

- Non-parameterized Constructor
- Parameterized Constructor
- Copy Constructor

## **1. Non-parameterized Constructor**

When a constructor does not take any arguments as input, it is called a **Non-parameterized Constructor**.

**Python**

```python


class Employee:
    # Non-parameterised constructor
    def __init__(self):
        print("Employee created!")
```

### **2. Parameterized Constructor:**

It is a type of constructor that accepts arguments to initialize attributes with specific values. For example, the following code snippet shows a parameterized constructor initializing the attributes of the object with the arguments provided by the user.

**Python**

```python

class Employee:
    # To store the name of the employee
    # To store the salary of the employee
    def __init__(self, name, salary):
        self.employeeName = name
        self.salary = salary

# Main Class
if __name__ == "__main__":
    # Creating an object of Employee class and passing 
    # values for the parameterized constructor
    obj = Employee("Mujeeb", 10000)

    # Output
    print("The salary of employee named " + obj.employeeName + " is " + str(obj.salary))
```

### **Keypoints:**

- The keyword `self` in Python refers to the current object.
- Parameterized constructors are useful when objects must be initialized with user-defined values.

### **3. Copy Constructor:**

It enables the programmer to create a new object by copying the attributes of an existing object. Python doesn't have an explicit copy constructor like C++ does. However, a copy constructor can be implemented manually by creating a constructor that takes an object of the same class as a parameter and copies its attributes using Constructor Chaining. Here's an example:

**Python**

```python

class Employee:
    # Parameterized constructor
    def __init__(self, name, salary):
        self.employeeName = name  # To store the name of the employee
        self.salary = salary      # To store the salary of the employee

    # Copy Constructor
    @classmethod
    def from_employee(cls, employee):
        # Calling another constructor
        return cls(employee.employeeName, employee.salary)

# Main Class
if __name__ == "__main__":
    # Creating an object of Employee class and passing 
    # values for the parameterized constructor
    obj = Employee("Mujeeb", 10000)

    # Creating a copy of obj using Copy constructor
    objCopy = Employee.from_employee(obj)

    # Printing the attibutes of copied object
    print("Name of the copied employee: " + objCopy.employeeName)
    print("Salary of the copied employee: " + str(objCopy.salary))
```


## **Constructor Chaining**

Constructor chaining allows one constructor to call another constructor of the same class to avoid code duplication.

### **Python**

- Python achieves constructor chaining by calling another constructor using `cls()` inside a class method.
- This is commonly seen in copy constructors.

### **Keypoints**

- Constructor chaining helps reduce repeated initialization code.
- It ensures a single point of truth for object initialization.
- There is no limit to constructor chaining.

## **Constructor Overloading**

Python does **not support constructor overloading directly** like Java.

Instead, Python uses **default arguments** to simulate constructor overloading.

**Python** 

```python

class Employee:
    def __init__(self, employeeName="Unknown", salary=0):
        self.employeeName = employeeName  # To store the name of the employee
        self.salary = salary              # To store the salary of the employee

    # Method to display employee details
    def displayDetails(self):
        print("Employee Name:", self.employeeName)
        print("Salary:", self.salary)

# Main Class
if __name__ == "__main__":
    # Using Default Constructor
    emp1 = Employee()
    print("Details of Employee 1 (Default Constructor):")
    emp1.displayDetails()

    print()  # Line break for clarity

    # Using Constructor with one parameter
    emp2 = Employee("Mujeeb")
    print("Details of Employee 2 (One Parameter Constructor):")
    emp2.displayDetails()

    print()  # Line break for clarity

    # Using Constructor with two parameters
    emp3 = Employee("Saif", 5000)
    print("Details of Employee 3 (Two Parameters Constructor):")
    emp3.displayDetails()

```


### **Advantages:**

- ***Flexibility:** It provides different ways to create and initialize objects based on available data.*
- ***Code Reusability:** Allows user to reuse the same class for different initialization scenarios without duplicating code.*
- ***Improved Readability:** Makes the code more readable and cleaner by grouping related logic in one class.*