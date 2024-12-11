# Sequence Types
# Note: use print() to execute the examples. Comment out examples after they've been demoed.

# Creating Lists
# 1. ✅ Create a list of 10 pet names
pet_names = [
    "Rose",
    "Meow Meow Beans",
    "Mr.Legumes",
    "Luke",
    "Lea",
    "Princess Grace",
    "Spot",
    "Tom",
    "Mini",
    "Paul",
    "Tom",
]

# Reading Information From Lists
# 2. ✅ Print the first pet name
# print(pet_names[0])

# 3. ✅ Print all pet names beginning from the 3rd index
# print(pet_names[2:])


# 4. ✅ Print all pet names before the 3rd index
# print(pet_names[:2])


# 5. ✅  Print all pet names beginning from the 3rd index and up to the 7th (exclusive)
# print(pet_names[2:6])


# 6. ✅ Find the index of a given element
# print(pet_names.index("Tom"))
# print(pet_names.index("Chase"))


# 7. ✅ Reverse the original list (in-place)
# print(pet_names.reverse())
# print(pet_names)


# 8. ✅ Print the frequency of a given element
# print(pet_names.count("Tom"))
# print(pet_names.count("Chase"))

# Updating Lists
# 9. ✅ Change the first element to all uppercase
# print(pet_names[0].upper())  # upper() is non-destructive/non-mutating
# pet_names[0] = pet_names[0].upper()
# print(pet_names)

# 10. ✅ Append a new name to the list
pet_names.append("Chase")
# print(pet_names)


# 11. ✅ Add a new name at a specific index
pet_names.insert(3, "Miyuki")
# print(pet_names)

# 12. ✅ Add two lists together
new_pet_names = pet_names + list(("Bart", "Zeus", "Bert", "Ernie"))
# print(new_pet_names)

# 13. ✅ Remove the final element from the list
# print(pet_names.pop())
# print(pet_names)


# 14. ✅ Remove element by specific index
pet_names.pop(4)
# print(pet_names)


# 15. ✅ Remove a specific element
# print(pet_names.remove("Spot"))
pet_names.remove(pet_names[-2])
del pet_names[1]
# print(pet_names)


# 16. ✅ Remove all pet names from the list
# pet_names.clear()
# print(pet_names)

# Tuple
# 📚 Review With Students:
# Mutable, Immutable, Changeable, Unchangeable

# 17. ✅ Create a Tuple of pet 10 ages
pet_ages = (3, 5, 6, 2, 7, 10, 2, 11, 7, 2)

# 18. ✅ Print the first pet age
print(pet_ages[0])

# Testing Changeability
# 19. ✅ Attempt to remove an element with ".pop" (should error)
# pet_ages.pop()
print(type(pet_ages))
print(dir(pet_ages))

# 20. ✅ Attempt to change the first element (should error)
# pet_ages[0] = 4

# Tuple Methods
# 21. ✅ Return the frequency of a given element
print(pet_ages.count(2))

# 22. ✅ Return the index of a given element
print(pet_ages.index(7))
print(len(pet_ages))

# 23. ✅ Create a Range
# Note:  Ranges are primarily used in loops
r1 = range(10)
print(r1)
for i in r1:
    print(i)

r2 = list(range(10, 22, 2))
print(r2)

# Demo Sets (Stretch Goal)
# 24. ✅ Create a set of 3 pet foods
foods = {"kibble", "tuna", "mushrooms"}
snacks = frozenset(["liver", "kibble", "bone", "treats", "treats"])
print(dir(foods))
print(snacks)
# snacks.add("gummy bears")
foods.add("liver")
foods.add("liver")
print(foods)
print(foods.__contains__("tuna"))
print(foods.__contains__("banana"))
intersect = foods.intersection(snacks)
print(intersect)


# Demo Dictionaries
# Creating
# 25. ✅  Create a dictionary of pet information with the keys "name", "age" and "breed"
pet_info_rose = {"name": "rose", "age": 11, "breed": "domestic long "}
print(pet_info_rose)

# 26. ✅  Use dict to create a dictionary of pet information with the keys "name", "age" and "breed"
pet_info_spot = dict(name="Spot", age=25, breed="boxer")
print(pet_info_spot)

# Reading
# 27. ✅ Print the pet attribute of "name" using bracket notation
print(pet_info_rose["name"])
# print(pet_info_rose["mood"])

# 28. ✅ Print the pet attribute of "age" using ".get"
# Note: ".get" is preferred over bracket notation in most cases because it will return "None" instead of an error
print(pet_info_rose.get("age"))
print(pet_info_rose.get("mood"))

# Adding
pet_info_rose["mood"] = "Nonchalant"
pet_info_spot.setdefault("mood", "mischievous")
print(pet_info_rose)
print(pet_info_spot)

# Updating
# 29. ✅ Update the pets age to 12
pet_info_rose["age"] = 12
print(pet_info_rose)

# 30. ✅ Update the other pets age to 26
pet_info_spot.update(age=26)
print(pet_info_spot)

# Deleting
# 30. ✅ Delete a pets age using the "del" keyword
del pet_info_rose["age"]
print(pet_info_rose)


# 31. ✅ Delete the other pets age using ".pop"
pet_info_spot.pop("age")
print(pet_info_spot)


# 32. ✅ Delete the last item in the pet dictionary using "popitem()"
pet_info_spot.popitem()
print(pet_info_spot)


# Demo Loops
pet_info = [
    {
        "name": "rose",
        "age": 11,
        "breed": "domestic long-haired",
    },
    {
        "name": "spot",
        "age": 25,
        "breed": "boxer",
    },
    {
        "name": "Meow Meow Beans",
        "age": 2,
        "breed": "domestic long-haired",
    },
]

# 33. ✅ Loop through a range of 10 and print every number within the range
# r1 = range(10)
# print(r1)
# for i in r1:
#     print(i)
for num in range(10):
    print(num)


# 34. ✅ Loop through a range between 50 and 60 that iterates by 2 and print every number
for num in range(50, 61, 2):
    print(num)


# 35. ✅ Loop through the "pet_info" list and print every dictionary
# for pet in pet_info:
#     print(pet)


# 36. ✅ Create a function that takes a list as an argument
# The function should use a "for" loop to loop through the list and print every item
# Invoke the function and pass it "pet_names" as an argument
def print_info(info_list):
    for item in info_list:
        print(item)


print_info(pet_info)
print_info(pet_names)
print_info(foods)


# 37. ✅ Create a function that takes a list as an argument. (simple example)
# The function should define a counter and set it to 0
# Create a "while" loop
# The loop will continue as long as the counter is less than the length of the list
# Every loop should increase the count by 1
# Return the counter


def count_items(item_list):
    counter = 0
    while counter < len(item_list):
        counter += 1
    return counter


print(count_items(pet_info))


# 38. ✅ Create a function that updates the age of a given pet
# The function should take a list of "dict"s, "name" and "age" as parameters
# Create am index variable and set it to 0
# Create a while loop
# The loop will continue so long as the list does not contain a name matching the "name" param and the index is less then the length of the list
# Every list will increase the index by 1
# If the dict containing a matching name is found, update the item's age with the new age
# Otherwise, return 'pet not found'


def update_age(info_list, name, age):
    index = 0
    while index < len(info_list) - 1 and info_list[index].get("name") != name:
        index += 1
    if info_list[index].get("name") == name:
        info_list[index]["age"] = age
        return info_list[index]
    else:
        return "pet not found"


print(update_age(pet_info, "rose", 13))
print(update_age(pet_info, "marc", 13))


# map like
# 39. ✅ Use list comprehension to return a list containing every pet name from "pet_info" changed to uppercase
upper_names = [pet.get("name").upper() for pet in pet_info]
print(upper_names)


# find like
# 40. ✅ Use list comprehension to find a pet named spot
find_spot = [pet for pet in pet_info if pet.get("name") == "spot"][0]
print(find_spot)

# filter like
# 41. ✅ Use list comprehension to find all of the pets under 3 years old
results = []
for pet in pet_info:
    if pet.get("age") < 3:
        results.append(pet)
# print(results)
young_pets = [pet for pet in pet_info if pet.get("age") < 3]
print(young_pets)


# 43. ✅ Create a generator expression matching the filter above. Compare and contrast the generator to the list comprehension.
young_pets_generator = (pet for pet in pet_info if pet.get("age") < 5)
print(young_pets_generator)
for pet in young_pets_generator:
    print(pet)
