def count_vowels_consonants(text):
    text = text.lower()  # Convert to lowercase for easy checking
    result = {'vowels': 0, 'consonants': 0}  # Dictionary to store result
    vowels = "aeiou"

    for char in text:
        if char.isalpha():  # Only check letters
            if char in vowels:
                result['vowels'] += 1
            else:
                result['consonants'] += 1

    return result

# Example usage
word = input("Enter a word or sentence: ")
counts = count_vowels_consonants(word)

print("Vowels:", counts['vowels'])
print("Consonants:", counts['consonants'])
