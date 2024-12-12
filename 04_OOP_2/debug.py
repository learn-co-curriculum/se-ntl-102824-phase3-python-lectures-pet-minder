#!/usr/bin/env python3
# 📚 Review With Students:
# Introduction to Object Oriented programming, classes, instances, methods

from lib.cat import *
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

import ipdb

ipdb.set_trace()
