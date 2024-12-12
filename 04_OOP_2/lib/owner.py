from lib.pet import *


class Owner:

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def adopt_pet(self, pet):
        pet.owner = self

    def get_pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def __repr__(self):
        return f"<Owner: {self.name}>"
