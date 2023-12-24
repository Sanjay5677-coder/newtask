sentence = input("Enter a sentence: ")

sentence = sentence.lower()

vowel_count = 0
for char in sentence:
    if char in "aeiou":
        vowel_count += 1

print("Number of vowels in the sentence:", vowel_count)
