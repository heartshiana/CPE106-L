# Programming Problem 1
# stats.py

def MEDIAN(numbers):
    median = sorted(numbers)
    n = len(median)
    if n % 2 == 0:
        # Even number of elements
        mid_1 = n // 2
        mid_2 = mid_1 - 1
        return (median[mid_2] + median[mid_1]) / 2
    else:
        # Odd number of elements
        return median[n // 2]

def MODE(numbers):
    mode = max(numbers, key = numbers.count)
    return mode

def MEAN(numbers):
    mean = sum(numbers)/len(numbers)
    return mean

# test run for odd number of elements = [10, 8, 5, 5, 6, 7, 5, 11, 4, 9, 3][2, 4, 6, 5, 5, 3]
numbers = [10, 8, 5, 5, 6, 7, 5, 11, 4, 9, 3]

print("Median:", MEDIAN(numbers))
print("Mode:", MODE(numbers))
print("Mean:", MEAN(numbers))

