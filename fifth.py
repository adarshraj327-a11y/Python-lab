# Count the frequency of words and characters

sentence = input("Enter a sentence: ")

# Word frequency
word_freq = {}
for word in sentence.lower().split():
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# Character frequency
char_freq = {}
for char in sentence.lower():
    if char != " ":      
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1

print("\nWord Frequency:")
for word in word_freq:
    print(word, ":", word_freq[word])

print("\nCharacter Frequency:")
for char in char_freq:
    print(char, ":", char_freq[char])