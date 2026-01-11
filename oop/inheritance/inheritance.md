# **Inheritance**

Inheritance is a fundamental concept in **object-oriented programming (OOP)** that allows a class (subclass) to inherit the **attributes** (fields) and **methods** (behaviors) of another class (superclass). It promotes **code reuse**, helps organize code hierarchically, and allows subclasses to extend or modify the behavior of a parent class.

In Python, inheritance is straightforward: a subclass inherits from a parent class using parentheses in the class definition. Python supports **single, multilevel, hierarchical, and multiple inheritance**.

## **Basic Example of Inheritance**

Consider a `School` class (parent) and a `Student` class (child). The child class can use methods of the parent class without redefining them.

```python
# Parent class
class School:
	def __init__(self):
		self.__school_name = "DPS" # private attribute

	def print_school_name(self):
		print("School name:", self.__school_name)

# Subclass
class Student(School):
	def __init__(self, name):
		super().__init__() # Call parent constructor
		self.__student_name = name # private attribute

	def print_student_name(self):
		print("Student name:",self.__student_name)

# Main execution
if __name__ =="__main__":
    student = Student("Mujeeb")
    student.print_student_name() # Output: Student name: Mujeeb
    student.print_school_name() # Output: School name: DPS
```

## **Parent Class vs Subclass**

- **Parent Class (Superclass):** Provides common attributes and methods for other classes to reuse.
    
    Example: `School` class.
    
- **Subclass (Child Class):** Inherits from the parent class and can extend or override its behavior.
    
    Example: `Student` class.
    

## **Types of Inheritance in Python**

### 1. **Single Inheritance**

A single child class inherits from **one parent class**.

```python
# Parent class
class Animal:
	def eat(self):
		print("This animal eats food.")

# Child class
class Dog(Animal):
	def bark(self):
		print("This dog barks.")

if __name__ =="__main__":
    dog = Dog()
    dog.eat() # Inherited from Animal
    dog.bark() # Defined in Dog
```

**Key Points:**

- One-to-one relationship between parent and child.
- Simple and common form of inheritance.

### 2. **Multilevel Inheritance**

A chain of inheritance where a class inherits from a child class.

```python
class Animal:
	def eat(self):
		print("This animal eats food.")

class Mammal(Animal):
	def walk(self):
		print("This mammal walks.")

class Dog(Mammal):
	def bark(self):
		print("This dog barks.")

if __name__ =="__main__":
    dog = Dog()
    dog.eat() # From Animal
    dog.walk() # From Mammal
    dog.bark() # From Dog

```

**Key Points:**

- One-to-one-to-one relationship.
- Each subclass inherits from its immediate parent.

### 3. **Hierarchical Inheritance**

Multiple subclasses inherit from the same parent class.

```python
class Animal:
	def eat(self):
		print("This animal eats food.")

class Dog(Animal):
	def bark(self):
		print("This dog barks.")

class Cat(Animal):
	def meow(self):
		print("This cat meows.")

if __name__ =="__main__":
    dog = Dog()
    cat = Cat()

    dog.eat() 
    dog.bark()
    cat.eat() 
    cat.meow()

```

**Key Points:**

- One-to-many relationship.
- Child classes share common parent methods but can have unique methods.

---

## **Important Concepts in Python Inheritance**

### 1. **Access Modifiers**

Python has no strict private/protected enforcement, but conventionally:

- `_protected_var` → intended for internal use.
- `__private_var` → name mangling prevents accidental access.

### 2. **Method Overriding**

A subclass can provide a **new implementation** of a method inherited from the parent class.

```python
class Animal:
    def speak(self):
        print("Some generic sound")

class Dog(Animal):
    def speak(self): # overriding
        print("Bark!")

if __name__ =="__main__":
    dog = Dog()
    dog.speak() # Output: Bark!
```

**Rules:**

- Same method name in parent and child.
- Parameters should match.
- Use `super()` if you want to call the parent method from the child.

### 3. **The `super()` Keyword**

`super()` allows a subclass to:

- Access parent methods.
- Call parent constructors.

```python
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        super().greet()# call parent method
        print("Hello from Child")

c = Child()
c.greet()
```

### 4. **Multiple Inheritance**

A class can inherit from **more than one parent**.

```python
class Father:
    def skills(self):
        print("Gardening")

class Mother:
    def skills(self):
        print("Cooking")

class Child(Father, Mother):
    pass

c = Child()
c.skills() # Follows MRO (Method Resolution Order): prints "Gardening"

```

**Note:**

- Python supports multiple inheritance.
- **Diamond Problem** is resolved using **Method Resolution Order (MRO)**.

## **Advantages of Inheritance in Python**

1. **Code Reusability:** Reuse methods and attributes from parent classes.
2. **Modularity:** Clear separation of responsibilities in classes.
3. **Extensibility:** Easily add new features in subclasses.
4. **Maintainability:** Centralized code for common behaviors.

### **Difference Between Method Overloading and Overriding in Python**

| Feature | Method Overloading | Method Overriding |
| --- | --- | --- |
| Definition | Same method name, different parameters | Subclass provides new implementation |
| Inheritance | Not required | Required |
| Parameters | Must differ | Must be the same |
| Access Modifiers | Any | No stricter than parent |
| Python Note | Python does not natively support true overloading; can use default arguments or `*args`. | Fully supported |

---

**Python-specific Notes:**

- Python uses `super()` instead of Java’s `super`.
- Private attributes use **name mangling** (`__var`).
- Python allows multiple inheritance but uses **MRO** to resolve conflicts.