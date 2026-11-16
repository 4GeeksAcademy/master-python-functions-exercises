import math


def car_route(daily_distance, route_length):
    return math.ceil(route_length / daily_distance)


# Try your function with different values
print(car_route(20, 40))
