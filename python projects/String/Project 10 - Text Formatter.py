paragraph = input("Enter a paragraph: ")
formatted = ' '.join(paragraph.split()) # Remove extra spaces
    
vowels = "aeiouAEIOU" # Define vowels by creating a string
vowel_count = sum(1 for char in formatted if char in vowels) # Count vowels
consonant_count = sum(1 for char in formatted if char.isalpha() and char not in vowels) # Count consonants
if formatted: # Capitalize first letter if string is not empty
    formatted = formatted[0].upper() + formatted[1:]
word_count = len(formatted.split()) # Count words

# Output results
print("Formatted Text:", formatted)
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
print("Word Count:", word_count)
