sentence = input("Enter a sentence: ") # Get user input for the sentence
specific_word = input("Enter a word to count how many times it appears: ") # Get user input for the specific word to count
words = sentence.split() # Split the sentence into words
word_count = len(words) # Count the number of words
print(f"Number of words: {word_count}") 
char_count = len(sentence) # Count the number of characters including spaces
print(f"Number of characters (including spaces): {char_count}") 
char_count_no_spaces = len(sentence.replace(" ", "")) # Count the number of characters excluding spaces
print(f"Number of characters (excluding spaces): {char_count_no_spaces}")
print("Longest word(s): ", max(words, key=len)) # Find and print the longest word by length using max with key=len
specific_word_count = words.count(specific_word) # Count how many times the specific word appears in the list of words
print(f"The word '{specific_word}' appears {specific_word_count} time(s) in the sentence.")