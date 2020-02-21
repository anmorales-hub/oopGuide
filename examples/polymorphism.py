class Bear(object):
    def sound(self):
        print("Groarrr")


class Dog(object):
    def sound(self):
        print("Woof woof!")

def makeSound(animal):
    animal.sound()


bearObj = Bear()
dogObj = Dog()

makeSound(bearObj)
#prints "Groarrr"

makeSound(dogObj)
#prints "Woof woof!"