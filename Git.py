"""
constructor_and_decorator_demo.py

Mini project showing:
- Class constructor (__init__)
- @property / @setter decorators (encapsulation style)
- Custom function decorator for logging
"""


# -----------------------------
# 1. Custom decorator
# -----------------------------
def log_call(func):
    """Simple decorator to log function calls and return values."""
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling: {func.__name__}()")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__}() returned: {result}")
        return result
    return wrapper


# -----------------------------
# 2. Class with constructor + property decorators
# -----------------------------
class Student:
    def __init__(self, name, marks):
        """
        Constructor: runs automatically when creating an object.
        Example:
            s = Student("Rahul", 80)
        """
        self._name = name      # "protected" style attribute
        self._marks = marks    # raw marks value

    @property
    def name(self):
        """Getter for name (read-only in this example)."""
        return self._name

    @property
    def marks(self):
        """Getter for marks."""
        return self._marks

    @marks.setter
    def marks(self, value):
        """Setter with simple validation."""
        if 0 <= value <= 100:
            self._marks = value
        else:
            raise ValueError("Marks must be between 0 and 100")

    @property
    def grade(self):
        """Computed property, no direct attribute."""
        if self._marks >= 90:
            return "A"
        elif self._marks >= 75:
            return "B"
        elif self._marks >= 60:
            return "C"
        else:
            return "D"

    def __repr__(self):
        return f"Student(name='{self._name}', marks={self._marks}, grade='{self.grade}')"


# -----------------------------
# 3. Using decorator on function that works with objects
# -----------------------------
@log_call
def is_topper(student: Student):
    """Return True if student has grade A."""
    return student.grade == "A"


def main():
    # Using the constructor
    s1 = Student("Rahul", 92)
    s2 = Student("Anita", 67)

    print("Student objects created using constructor:")
    print(s1)
    print(s2)

    # Using property getter
    print("\nAccess with @property:")
    print("Name:", s1.name)
    print("Marks:", s1.marks)
    print("Grade:", s1.grade)

    # Using property setter
    print("\nUpdating marks using @marks.setter:")
    s2.marks = 88
    print(s2)

    # Using custom decorator
    print("\nChecking toppers using @log_call decorator:")
    is_topper(s1)
    is_topper(s2)


if __name__ == "__main__":
    main()
