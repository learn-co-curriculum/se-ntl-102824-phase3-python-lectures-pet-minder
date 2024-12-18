import sys

from handler import Handler
from job import Job
from pet import Pet
from rich import print

# User stories:
# As a user, I can:
# 1. select a menu option to see all the pets
# 2. select a menu option to see one pet's details
# 3. select a menu option to see a pet's jobs
# 4. select a menu option to create a job for a pet
# 5. select a menu option to add a pet


# **********************
# Interface operations


def display_welcome():
    print("[magenta]Hello! Welcome to [/magenta][bold cyan] Pet Minder![/bold cyan]")


def display_main_menu():
    print("[bold]Main Menu[/bold]")
    print("[i]1. Show all pets[/i]")
    print("[i]2. Add a pet[/i]")
    print("[i]3. Exit app[/i]")


def get_main_choice():
    return input("What is your command?")


def choose_pet_by_id():
    search_id = input("Enter the number of the pet you want to see")
    pet = Pet.find_pet_by_id(search_id)
    print(
        f"Id: {pet.id}, Name: {pet.name}, Species: {pet.species}, Breed: {pet.breed}, Temperament: {pet.temperament}"
    )


def display_all_pets():
    pets = Pet.get_all_pets()
    for pet in pets:
        print(f"{pet.id} | {pet.name} | {pet.species}")
    print("What would you like to see?")
    print("1. See more about a pet")
    print("2. Exit app")
    print("3. Return to main menu")
    choice = input()
    if choice == "1":
        choose_pet_by_id()
    elif choice == "2":
        exit_app()
    else:
        return


def display_goodbye():
    print("[lime]Thanks for using Pet Minder! Goodbye![/lime]")


def exit_app():
    display_goodbye()
    sys.exit()


# *********************
# command line interface
if __name__ == "__main__":
    display_welcome()
    while True:
        display_main_menu()
        choice = get_main_choice()
        if choice == "1":
            display_all_pets()
        else:
            exit_app()
