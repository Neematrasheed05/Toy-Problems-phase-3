def solve(word):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    
    substrings = []
    start = 0  # Initialize i outside the loop
    
    for i in range(len(word)):
        if word[i] in consonants:
            
            if i == 0 or word[i - 1] not in consonants:
                start = i
        else:
            
            if start < i:
                substrings.append(word[start:i])
                
    if start < len(word):
        substrings.append(word[start:])
    
    
    # Assign values to substrings
    substring_values = {}
    for substring in substrings:
        substring_values[substring] = sum(ord(char) - ord('a') + 1 for char in substring)

    # Return the highest value
    #.values() When called on a dictionary, it returns a view of all values in the dictionary.
    return max(substring_values.values())

