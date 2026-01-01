def title_case(title, minor_words=''):
    
    if not title :
        return title
    
    if not minor_words:
        return " ".join([word.capitalize() for word in title.split()])
    
    words = title.split()
    transformed_words = []
        
    for i in range(len(words)):
        
        if i != 0 and words[i].lower() in [i.lower()for i in minor_words.split()]:
            transformed_words.append(words[i].lower())
        else :
            transformed_words.append(words[i].capitalize())
            
#     transformed_words[0] = transformed_words[0].capitalize()
            
    
    return " ".join(transformed_words)
    
            
        

    