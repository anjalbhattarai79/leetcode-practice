# Write a function that takes in a string of one or more words,
# and returns the same string, but with all five or more letter words reversed 
#. Strings passed in will consist of only letters and spaces. 
# Spaces will be included only when more than one word is present.

def spin_words(sentence):
    word = sentence.split()
    length = len(word)
    for i in range(length):
        if len(word[i]) >= 5:
            word[i] = word[i][::-1]
    word = ' '.join(word)
    
    return word

print(spin_words('This is another test'))

