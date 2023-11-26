def solve(word):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    substrings = []

    # Get consonant substrings
    for i in range(len(word)):
        if word[i] in consonants:
            start = i
            while i < len(word) and word[i] in consonants:
                i += 1
            substrings.append(word[start:i])

    # Assign values to substrings
    substring_values = {}
    for substring in substrings:
        substring_values[substring] = sum(ord(char) - ord('a') + 1 for char in substring)

    # Return the highest value
    return max(substring_values.values())

