import random

def lottery():
    for i in range(11):
        yield random.randint(1,100)

for random_number in lottery():
    print("The next number is %d!" %
    (random_number))
