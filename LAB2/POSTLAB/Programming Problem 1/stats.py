def calculate_mean(numbers):
    
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    
    if not numbers:
        return 0
    
    numbers.sort()
    midpoint = len(numbers) // 2

    if len(numbers) % 2 == 1:
        return numbers[midpoint]
    else:
        return (numbers[midpoint] + numbers[midpoint - 1]) / 2

def calculate_mode(words):
    if not words:
        return 0
    
    # Count occurrences of each word
    word_counts = {}
    for word in words:
        count = word_counts.get(word, None)
        if count is None:
            word_counts[word] = 1
        else:
            word_counts[word] = count + 1

    # Find the maximum count
    max_count = max(word_counts.values())

    # Find words with maximum count (modes)
    modes = [key for key in word_counts if word_counts[key] == max_count]
    
    return modes

def main():
    # Test the statistical functions with a given list
    test_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    test_words = ["apple", "banana", "apple", "orange", "banana", "grape"]

    print("Mean:", calculate_mean(test_numbers))
    print("Median:", calculate_median(test_numbers))
    print("Mode:", calculate_mode(test_words))

if __name__ == "__main__":
    main()
