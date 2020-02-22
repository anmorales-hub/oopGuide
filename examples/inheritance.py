class Person(object):
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printName(self):
        print(self.firstname,self.lastname)

class Child(Person):
    pass


test = Child("Andrey", "Morales")
Child.printName()