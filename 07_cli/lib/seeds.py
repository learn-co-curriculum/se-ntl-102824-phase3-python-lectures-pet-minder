import random

from faker import Faker
from handler import Handler
from job import Job
from owner import Owner
from pet import Pet

if __name__ == "__main__":

    print("Resetting tables...")

    Job.drop_table()
    Pet.drop_table()
    Handler.drop_table()
    Owner.drop_table()
    Owner.create_table()
    Handler.create_table()
    Pet.create_table()
    Job.create_table()

    print("Creating constants...")

    fake = Faker()

    # Create a list of species
    SPECIES = ["CAT", "DOG"]

    # create a list of cat breeds
    CAT_BREEDS = [
        "Domestic longhair",
        "Domestic short hair",
        "Siamese",
        "Ragdoll",
        "Sphynx",
        "Burmese",
    ]

    DOG_BREEDS = [
        "Mix",
        "Husky",
        "Malamute",
        "Dachshound",
        "Samoyed",
        "Shiba Inu",
        "Corgi",
    ]

    # Create an list of temperaments
    TEMPERAMENTS = ["Calm", "Nervous", "Mischievous", "Aggressive", "Hyper"]

    print("Making owners...")

    owners = []

    for _ in range(50):
        owner = Owner(
            name=f"{fake.first_name()} {fake.last_name()}",
            email=fake.email(),
            phone=random.randint(1000000000, 9999999999),
            address=fake.address(),
        )
        owner.save()
        owners.append(owner)

    print("Making pets...")

    pets = []

    for owner in owners:
        for _ in range(random.randint(1, 3)):
            rand_species = random.choice(SPECIES)
            pet = Pet.create(
                name=fake.name(),
                species=rand_species,
                breed=(
                    random.choice(CAT_BREEDS)
                    if rand_species == "CAT"
                    else random.choice(DOG_BREEDS)
                ),
                temperament=random.choice(TEMPERAMENTS),
                owner_id=owner.id,
            )
            pets.append(pet)

    print("Making handlers...")

    # 5.✅ Create a empty list set to handlers
    handlers = []
    # Create a for loop that iterates 50 times
    for _ in range(50):
        # Create a handler with faker data
        handler = Handler(
            name=f"{fake.first_name()} {fake.last_name()}",
            email=fake.email(),
            phone=random.randint(1000000000, 9999999999),
            hourly_rate=random.uniform(25.50, 80.50),
        )
        handler.save()
        # Append handler to handlers
        handlers.append(handler)

    requests = ["Walk", "Drop-in", "Boarding"]

    print("Making jobs...")

    jobs = []

    for handler in handlers:
        for _ in range(random.randint(1, 10)):
            # Create a Job using faker, the request list and pets list
            job = Job(
                request=random.choice(requests),
                date=fake.date_this_year(),
                notes=fake.sentence(),
                fee=handler.hourly_rate,
                handler_id=handler.id,
                pet_id=random.choice(pets).id,
            )
            # append the job to the jobs list
            job.save()
            jobs.append(job)

    print("Seeding complete!")
