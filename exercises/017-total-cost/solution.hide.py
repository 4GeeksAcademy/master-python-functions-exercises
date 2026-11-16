def total_cost(dollars, cents, quantity):
    total_cents = (dollars * 100 + cents) * quantity
    return total_cents // 100, total_cents % 100


# Try your function with different values
print(total_cost(10, 15, 2))
