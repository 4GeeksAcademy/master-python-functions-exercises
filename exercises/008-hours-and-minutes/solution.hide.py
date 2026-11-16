def hours_minutes(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return hours, minutes


# Try your function with different values
print(hours_minutes(3900))
