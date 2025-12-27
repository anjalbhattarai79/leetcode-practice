# Write a function that takes in a string of one or more words,
# and returns the same string, but with all five or more letter words reversed 
#. Strings passed in will consist of only letters and spaces. 
# Spaces will be included only when more than one word is present.

#1. Looping over index
def spin_words(sentence):
    word = sentence.split()
    length = len(word)
    for i in range(length):
        if len(word[i]) >= 5:
            word[i] = word[i][::-1]
    word = ' '.join(word)
    
    return word

print(spin_words('This is another test'))

# looping over copy of list.
def prctc(text):
    words = text.split()
    result = [] # Needeed !!!
    for word in words:
        if len(word) >= 5:
            result.append(word[::-1]) 
        else: 
            result.append(word)
    return " ".join(result)