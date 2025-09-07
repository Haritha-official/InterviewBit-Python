# main.py

"""
This program demonstrates Object-Oriented Programming (OOP) in Python
by defining a Student class with attributes and a method to print details.

Sample Output:
Robin CSE
Rahul ECE
"""

# Define the Student class
class Student:
    # Constructor to initialize student details
    def __init__(self, name, branch):
        self.name = name
        self.branch = branch

    # Method to print student information
    def printfunction(self):
        print(self.name + " " + self.branch)

# Define the main function
def main():
    # Create two Student objects
    stud1 = Student("Robin", "CSE")
    stud2 = Student("Rahul", "ECE")
    
    # Call the method to print student details
    stud1.printfunction()
    stud2.printfunction()
    
    # Return 0 to indicate successful execution
    return 0

# Run the main function only if this file is executed directly
if __name__ == '__main__':
    main()
