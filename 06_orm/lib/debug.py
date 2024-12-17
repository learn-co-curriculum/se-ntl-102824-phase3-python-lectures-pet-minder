#!/usr/bin/env python3

from owner import CONN, CURSOR, Owner
from pet import CONN, CURSOR, Pet

psql = """
    DROP TABLE IF EXISTS pets
"""

osql = """
    DROP TABLE IF EXISTS owners
"""

# CURSOR.execute(psql)
CURSOR.execute(osql)

# Pet.drop_table()

# Owner.create_table()
# frank = Owner("frank", "555-555-5555", "frank@gmail.com", "555 Somewhere St.")
# frank.save()

Pet.create_table()
# spot = Pet("spot", "dog", "chihuahua", "feisty")
spot = Pet.create("spot", "dog", "chihuahua", "feisty", 1)
simon = Pet.create("simon", "cat", "Munchkin", "brat", 1)
# spot = Pet("spot", "dog", "chihuahua", "feisty", 1)
# spot.save()

import ipdb

ipdb.set_trace()
