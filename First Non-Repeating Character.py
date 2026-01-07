'''
Using counter

'''

from collections import Counter

def first_non_repeating_letter(s):
    freq = Counter([c.lower() for c in s])
    print(freq)
    for c in s:
        if freq[c.lower()] == 1:
            return c
    return ""

print(first_non_repeating_letter('aabsb'))

''' 
My way of doing
'''

def first_non_repeating_letter(s):
    if not s:
        return s
    
    test = "".join([c for c in s ]) #getting duplicate 
    
    unique_letter = [ c.lower() for c in test]
    
    counter = []
    for c in test:
        count = unique_letter.count(c.lower())  
        if count == 1 :
            return c
        
        element = (c, count)
        counter.append(element)
        
    if counter:
        return ""
        
    
        
print(first_non_repeating_letter('aabb'))