# **Access Modifiers**

Access modifiers in object-oriented programming are **keywords or conventions** that define the visibility and accessibility of classes, methods, variables, and other members of a program. They determine which parts of the program can interact with a particular component, ensuring adherence to **encapsulation**, a core principle of object-oriented programming.

Access modifiers provide controlled interaction between objects and help enforce good design practices, making programs more reliable, scalable, and easier to debug.

---

## **Purpose of Access Modifiers**

Access modifiers play a crucial role in object-oriented programming and serve the following purposes:

- **Encapsulation:** Protects sensitive data and internal implementation details.
- **Controlled Access:** Defines clear boundaries for how components interact.
- **Modularity and Security:** Prevents unintended modification of internal data.
- **Flexibility:** Enables safe and controlled data sharing between classes.

---

## **Access Control in Python**

Unlike Java or C++, **Python does not enforce access modifiers at the language level**. Instead, it follows **naming conventions** to indicate intended access levels. Most object-oriented languages define four access levels, which can be **conceptually mapped to Python** as follows:

- **Public:** Accessible from anywhere.
- **Private:** Intended to be accessible only within the defining class.
- **Protected:** Intended for access within the class and its subclasses.
- **Default (Package-private):** Exists in Java, **but not in Python**.

---

## **1. Public Access (Python Default)**

In Python, **all attributes and methods are public by default** unless indicated otherwise. Public members can be accessed freely from anywhere in the program.

### **Example**

```python
class Employee:
	def __init__(self):
		self.name = None          # Public attribute

	def display_name(self):     # Public method
		print("Employee Name:",self.name)

if __name__ =="__main__":
    emp = Employee()
    emp.name ="Alice"        # Accessible globally
    emp.display_name()       # Accessible globally
```

Here, both `name` and `display_name()` are publicly accessible.

### **Key Points**

- Default visibility in Python.
- Accessible from anywhere.
- Suitable for methods and attributes meant for general use.
- No access restrictions enforced by the language.

---

## **2. Private Access (Using Name Mangling)**

Python simulates private access using **name mangling**, achieved by prefixing the attribute or method name with **double underscores (`__`)**.

### **Example**

```python
class BankAccount:
	def __init__(self):
		self.__balance = 0    # Private attribute (name mangling)

	defget_balance(self):
		return self.__balance

	def deposit(self, amount):
		if amount > 0:
			self.__balance += amount

if __name__ =="__main__":
    account = BankAccount()

# print(account.__balance)  # AttributeError
print(account.get_balance())

```

Here, `__balance` cannot be accessed directly outside the class due to name mangling.

### **Key Points**

- Prevents accidental access from outside the class.
- Encourages controlled access using getter/setter methods.
- Still technically accessible via `_ClassName__attribute`, but **discouraged**.
- Not accessible directly by subclasses.

---

## **3. Protected Access (By Convention)**

Protected members are indicated by a **single leading underscore (`_`)**. This is a **convention**, signaling that the member is intended for internal use within the class and its subclasses.

### **Example**

```python
class Vehicle:
	def __init__(self):
		self._type = None      # Protected attribute

	def _display_type(self): # Protected method
		print("Vehicle Type:", self._type)

class Car(Vehicle):
	def __init__(self):
		super().__init__()
		self._type ="Car"      # Accessible in subclass
```

Here, the subclass `Car` can access the protected attribute `_type`.

### **Key Points**

- Designed to support **inheritance**.
- Accessible in subclasses.
- Should not be accessed by unrelated external classes.
- Enforced by developer discipline, not by the language.

---

## **4. Default (Package-Private) — Not Applicable in Python**

In languages like Java, members without an access modifier are **package-private**, meaning they are accessible only within the same package.

⚠️ **Python does not support package-private access control.**

If no underscore is used, the member is treated as **public**.

### **Example**

```python
class PackageDemo:
    def show_message(self):
				print("Accessible everywhere in Python")

if __name__ =="__main__":
    demo = PackageDemo()
    demo.show_message()

```

### **Key Points**

- Python has **no package-level access restriction**.
- Unprefixed members are always public.
- Package-level encapsulation relies on developer discipline and module design.

---

## **Access Modifier Comparison (Conceptual Mapping)**

| **Access Level** | **Class** | **Module / Package** | **Subclass** | **External Code** |
| --- | --- | --- | --- | --- |
| **Public** | ✔️ | ✔️ | ✔️ | ✔️ |
| **Protected** | ✔️ | ✔️ (by convention) | ✔️ | ❌ (discouraged) |
| **Private** | ✔️ | ❌ | ❌ | ❌ |
| **Default** | ❌ (N/A) | ❌ | ❌ | ❌ |

> ⚠️ Protected and Private access in Python are enforced by convention, not by the compiler or interpreter.
