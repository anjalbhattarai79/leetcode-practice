#Complete the method/function so that it converts dash/underscore delimited words 
# into camel casing. The first word within the output should be capitalized only 
# if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). 
# The next words should be always capitalized.


import re 


def to_camel_case (text):
    if not text: #if text == "" or text ==None
        return text 
    
    words = re.split(r"[-_ ]", text)
    result = [words[0]]
    
    for word in words[1:]: 
        result.append(word[0].upper()+word[1:])
        
    return "".join(result)

answer = to_camel_case("i am a go kay")
print(answer)