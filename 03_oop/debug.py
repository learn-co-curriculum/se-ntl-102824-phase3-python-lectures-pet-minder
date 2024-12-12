#!/usr/bin/env python3

from lib.pet import *

chase = Pet("Chase", 7, "pug", "rowdy", "./assets/cookie.jpg")
brooke = Pet("Brooke", 8, "American shorthair", "chill", "./assets/rose.jpg")

chase.age = 8
print(chase.age)

brooke.birthday()
print(brooke)


import ipdb

ipdb.set_trace()
