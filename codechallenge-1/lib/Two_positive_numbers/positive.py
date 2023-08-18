def exactly_two_positives(a, b, c):
    positive_count = 0

    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1

    return positive_count == 2

# Test cases
print(exactly_two_positives(1, -2, 3))  # Output: True
print(exactly_two_positives(-1, 2, 4))  # Output: True
print(exactly_two_positives(0, 1, 5))  # Output: True
print(exactly_two_positives(-1, -2, -3))  # Output: False
print(exactly_two_positives(4, 5, 6))  # Output: False
