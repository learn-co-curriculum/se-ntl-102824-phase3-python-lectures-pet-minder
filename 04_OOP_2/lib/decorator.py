# 1. ✅ Demonstrate First Class Functions
# Create functions to be used as callbacks
# Create a higher-order function that will take a callback as an argument


def feed(pet):
    return f"{pet} has been fed"


def walk(pet):
    return f"{pet} has been walked"


# 2. ✅ Create a higher-order function that returns a function


def task_for_Rose(func):
    return func("Rose")


def task_for_Brooke(func):
    return func("Brooke")


print(task_for_Rose(feed))
print(task_for_Brooke(walk))


def task_for_pet():
    def feed(pet):
        return f"{pet} has been fed"

    return feed


print(task_for_pet()("Chase"))


# 3. ✅ Demonstrate a decorator
# Create a function that takes a function as an argument, has an inner function, and returns the inner function
# Demo examples of the decorator with and without pie syntax '@'


def coupon_calculator(func):
    def wrapper():
        print("Base price is $35/hr")
        new_price = func(35.00)
        print(f"Price after coupon is {new_price}/hour")

    return wrapper


def half_off(price):
    return f"{round(price/2):.2f}"


def twenty_off(price):
    return f"{round(price * .8):.2f}"


# Without pie syntax

half_price = coupon_calculator(half_off)
half_price()

coupon_calculator(twenty_off)()


# With pie syntax


@coupon_calculator
def ten_off(price):
    return f"{round(price * .9):.2f}"


ten_off()
