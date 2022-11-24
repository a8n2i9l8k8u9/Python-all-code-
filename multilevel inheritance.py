class Animal:
    def bark(self):
        print("Barking...")
class Dog(Animal):
    def dog(self):
        print("Dog ....")
class child(Dog):
    def liftchild(self):
        print("Derived class...")
d=child()
d.liftchild()
d.dog()
d.bark()

