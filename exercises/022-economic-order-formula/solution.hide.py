import math


def order_quantity(demand):
    C = 50
    H = 30
    return round(math.sqrt((2 * C * demand) / H))


# Try your function with different values
print(order_quantity(150))
