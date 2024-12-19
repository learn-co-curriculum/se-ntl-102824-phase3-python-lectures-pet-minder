import sys

from handler import Handler
from helpers import *
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


# TODO: add error handling and messaging


# **********************
# Interface operations

# many fns in this section could reside in helpers


def display_welcome():
    print("[magenta]Hello! Welcome to [/magenta][bold cyan] Pet Minder![/bold cyan]")


def display_main_menu():
    print("[bold]Main Menu[/bold]")
    print("[i]1. Show all pets[/i]")
    print("[i]2. Add a pet[/i]")
    print("[i]3. Exit app[/i]")


def get_main_choice():
    return input("What is your command?")


def show_pet_jobs(pet):
    jobs = Job.get_jobs_by_pet_id(pet.id)
    # import ipdb

    # ipdb.set_trace()
    for job in jobs:
        print(
            f"{job.id} | {job.request} | {job.date} | {job.notes} | {job.fee:.2f} || with {Handler.find_handler_by_id(job.handler_id).name}"
        )


def handle_pet_choice(choice, pet):
    if choice == "1":
        show_pet_jobs(pet)
    elif choice == "2":
        add_job_to_pet(pet)
        show_pet_jobs(pet)
    elif choice == "3":
        exit_app()
    else:
        return


def display_pet_details_submenu(pet):
    print("1. See a pet's jobs")
    print("2. Add a job to a pet")
    print("3. Quit the app")
    print("4. Return to main menu")
    choice = input("What would you like to do?")
    handle_pet_choice(choice, pet)


def choose_pet_by_id():
    search_id = input("Enter the number of the pet you want to see")
    pet = Pet.find_pet_by_id(search_id)
    print(
        f"Id: {pet.id}, Name: {pet.name}, Species: {pet.species}, Breed: {pet.breed}, Temperament: {pet.temperament}"
    )
    display_pet_details_submenu(pet)


def display_pets_submenu():
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


def display_all_pets():
    pets = Pet.get_all_pets()
    for pet in pets:
        print(f"{pet.id} | {pet.name} | {pet.species}")
    display_pets_submenu()


def display_goodbye():
    print("[cyan]Thanks for using Pet Minder! Goodbye![/cyan]")


def exit_app():
    display_goodbye()
    sys.exit()


# *********************
# command line interface
if __name__ == "__main__":
    display_welcome()  # this could be abstracted into a main() fn called here
    while True:
        display_main_menu()
        choice = get_main_choice()
        if choice == "1":
            display_all_pets()
        else:
            exit_app()
