# Find the longest word in a sentence.

text = "I am becoming a strong python programmer"

def longest_word(text):
    word = text.split()[0]
    for w in text.split():
        if len(w) > len(word):
            word = w
    return word

result = longest_word(text)
print(result)