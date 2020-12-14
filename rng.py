import random


def isint(will_it_int):
    try:
        float(will_it_int)
        return True
    except ValueError:
        return False


while True:
    rng_1 = input("How many numbers do you want? ")
    while isint(rng_1) is False:
        rng_1 = input("No, try again.\nHow many numbers do you want? ")
    rng_1 = int(rng_1)
    rng_2 = input("What do you want the lowest number in the range to be? ")
    while isint(rng_2) is False:
        rng_2 = input("No, try again.\nWhat do you want the lowest number in the range to be? ")
    rng_2 = int(rng_2)
    rng_3 = input("What do you want the highest number in the range to be? ")
    while isint(rng_3) is False or int(rng_3) <= rng_2:
        rng_3 = input("No, try again.\nWhat do you want the highest number in the range to be? ")
    rng_3 = int(rng_3)
    for i in range(rng_1):
        rng_4 = random.randint(rng_2, rng_3)
        print(rng_4)
