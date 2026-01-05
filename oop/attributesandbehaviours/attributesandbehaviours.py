"""

This file demonstrates the concept of attributes and behaviors in Python
using a simple Employee use case.

Focus areas:
- What are attributes
- Types of attributes (class and instance)
- What are methods (behaviors)
- Types of methods (instance, class, static)
- Why decorators like @classmethod and @staticmethod are used
"""

class Employee:
    """
    Employee represents a person working in a company.

    Attributes define the state of an employee.
    Methods define the behavior of an employee or the class.
    """

    # Class attribute
    # Shared across all Employee objects
    company_name = "Google"

    def __init__(self, name, age, department, salary):
        """
        Constructor to initialize instance attributes.

        Instance attributes are unique to each object.
        """
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary

    # Instance method
    def display_details(self):
        """
        Instance method because it works on individual employee data.
        Accesses instance attributes using self.
        """
        print("Employee Name:", self.name)
        print("Age:", self.age)
        print("Department:", self.department)
        print("Salary:", self.salary)
        print("Company:", Employee.company_name)

    # Instance method
    def update_salary(self, new_salary):
        """
        Updates salary for a specific employee.
        """
        self.salary = new_salary

    # Class method
    @classmethod
    def update_company_name(cls, new_name):
        """
        Class method because it modifies a class attribute.
        Uses cls to refer to the class.
        """
        cls.company_name = new_name

    # Static method
    @staticmethod
    def validate_age(age):
        """
        Static method because it does not access
        instance or class attributes.
        Used as a utility function.
        """
        if age < 18:
            return False
        return True


# -------------------------
# Use Case Execution
# -------------------------

# Validating age before creating an employee
if Employee.validate_age(25):
    emp1 = Employee("Alice", 25, "Engineering", 70000)

# Creating another employee
emp2 = Employee("Bob", 30, "HR", 50000)

# Display employee details
emp1.display_details()
print("-----")
emp2.display_details()

# Update salary for a specific employee
emp1.update_salary(75000)

# Update company name for all employees
Employee.update_company_name("Netflix")

print("----- After Updates -----")
emp1.display_details()
print("-----")
emp2.display_details()
