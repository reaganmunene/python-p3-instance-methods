#!/usr/bin/env python3

class Dog:
    # Class body goes here

    #Instance method definition
    def bark(self):
        print("Woof!")

    def sit(self):
        print("The dog is sitting.")
    pass


fido = Dog()
snoopy = Dog()

fido.bark()
snoopy.bark()
snoopy.sit()
