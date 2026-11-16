def two_timestamps(hour1, min1, sec1, hour2, min2, sec2):
    first = hour1 * 3600 + min1 * 60 + sec1
    second = hour2 * 3600 + min2 * 60 + sec2
    return second - first


# Try your function with different values
print(two_timestamps(1, 1, 1, 2, 2, 2))
