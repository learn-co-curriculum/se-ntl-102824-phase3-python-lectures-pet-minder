#!/usr/bin/env python3
# Demonstrate classes
# 1. ✅ Create a Pet class
# 2. ✅ Instantiate a few pet instance
# Compare the pet instances to demonstrate they are not the same object
# Note: add 'pass' to the pet class


class Pet:

    # 3. ✅ Demonstrate __init__
    # Add arguments to instances
    # use dot notation to access their attributes
    # update attributes with new values
    def __init__(self, name, age, breed, temperament, image_url):
        self.name = name
        self.age = age
        self.breed = breed
        self.temperament = temperament
        self.image_url = image_url

    # 4.✅ Demonstrate instance methods by creating a print_pet_details function that will print the pet attributes
    #     Review the self keyword
    #     Inexitvoke the print_pet_details on an instance
    #           ->
    # name:rose
    # age:11
    # breed:domestic longhair
    # temperament:sweet
    # image_url:rose.jpg

    def print_pet_details(self):
        print(
            f"""
                name: {self.name}
                age: {self.age}
                breed: {self.breed}
                temperament: {self.temperament}
                image_url: {self.image_url}
              """
        )

    def birthday(self):
        self.age += 1
        self.print_pet_details()

    # Demonstrate instances
    # Different Instances are Different Objects
    # Demonstrate __init__
    # Demonstrate instance method
    # Demonstrate the self keyword
    # Stretch Goals
    # Demonstrate object properties

    # Instances

    # Run in ipdb session
    # rose == cookie
    #   False

    # Read Attributes
    # rose.name -> rose
    # rose.age -> 11

    # Update
    # rose.age -> 11
    # rose.age = 12
    # rose.age -> 12

    # use properties to gain more control over attributes
    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if type(new_age) == int:
            self._age = new_age
        else:
            print("Age must be an integer")

    age = property(get_age, set_age)

    def __repr__(self):
        return f"<Pet name: {self.name} | breed: {self.breed}>"
