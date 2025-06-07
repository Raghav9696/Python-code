print("============== Vowels and Consonants ================")
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
lettersfrequency = {}


inputstring = "Jack and Jill went up the hill."

for ch in inputstring:
    ch = ch.lower().strip()
    if ch in vowels:

        lettersfrequency["vowels"] = 1+lettersfrequency.get("vowels", 0)

    if ch in consonants:

        lettersfrequency["consonants"] = 1+lettersfrequency.get("consonants", 0)

# print("vowels", vowels)
# print("consonants", consonants)
print(lettersfrequency)
