class Person(object):

    # Constructor
    def __init__(self, name):
        self.name = name

        # To get name
    def getName(self):
        return self.name

        # To check if this person is employee
    def isEmployee(self):
        return False

# Inherited or Sub class
class Employee(Person):
    def isEmployee(self):
        return True


emp = Person("Geek1")  # An Object of Person
print(emp.getName(), emp.isEmployee())
#returns False

emp = Employee("Geek2")  # An Object of Employee
print(emp.getName(), emp.isEmployee())
#returns True