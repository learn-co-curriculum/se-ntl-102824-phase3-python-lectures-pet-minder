#!/usr/bin/env python3
# Class Attributes and Methods


class Pet:

    total_pets = 0
    all = []

    def __init__(self, name, age, breed, temperament, image_url):
        self.name = name
        self.age = age
        self.breed = breed
        self.temperament = temperament
        self.image_url = image_url
        # Pet.total_pets += 1
        # Pet.increase_pet_count()
        self.__class__.increase_pet_count()
        self.__class__.all.append(self)
        self.owner = None

    # 6✅. Create a class method increase_pets that will increment total_pets
    # replace Pet.total_pets += 1 in __init__ with increase_pets()

    @classmethod
    def increase_pet_count(cls):
        cls.total_pets += 1
        print(f"The {cls.__name__} class has created {cls.total_pets} pet instances")

    def print_pet_details(self):
        print(
            f"""
            name:{self.name}
            age:{self.age}
            breed:{self.breed}
            temperament:{self.temperament}
            image_url:{self.image_url}
        """
        )

    def __repr__(self):
        return f"<Pet name: {self.name} | breed: {self.breed} >"
