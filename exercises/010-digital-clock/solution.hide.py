def digital_clock(minutes):
    return (minutes // 60) % 24, minutes % 60


# Try your function with different values
print(digital_clock(150))
