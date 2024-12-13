#!/usr/bin/env python3
# 📚 Review With Students:
# Introduction to Object Oriented programming, classes, instances, methods

from lib.cat import *
from lib.handler import *
from lib.job import *
from lib.owner import *

# Importing the pet class
from lib.pet import *

# Instances of the pet classes
rose = Pet("rose", 11, "domestic longhair", "sweet", "rose.jpg")
cookie = Pet("cookie", 1, "Dachshund", "hyper", "cookie.jpg")
princess_grace = Cat(
    "princess grace", 7, "domestic longhair", "affectionate", "gracy.png", True
)

# Instances of the owner class
jess = Owner("jess", "jess@mail.com")
chris = Owner("chris", "chris@mail.com")

# calling intance method on owners which create association with a pet
jess.adopt_pet(cookie)
jess.adopt_pet(rose)
chris.adopt_pet(princess_grace)

# create Handler instances
aixe = Handler("Aixe", "aixe@mail.com", 22)
hodor = Handler("Hodor", "hodor@mail.com", 19.99)

j1 = Job("2024-12-26 00:10:00", 2, "grooming", cookie, aixe)
cookie.book_job("2024-12-27 00:10:30", 1.5, "walk", hodor)
rose.book_job("2024-12-27 00:09:00", 1, "drop-in", hodor)
rose.book_job("2024-12-28 00:14:00", 2, "drop-in", aixe)

import ipdb

ipdb.set_trace()
