#elements = {"a":1,"b":2}
#val = "b"
#print(elements[val])

import json
from difflib import get_close_matches

elements = json.load(open("wordbook.json"))



def findWord(word):
    if word in elements:
        return elements[word]
    elif word.lower() in elements:
        word=word.lower()
        return elements[word]
    elif word.upper() in elements:
        word= word.upper()
        return elements[word]            
    elif len(get_close_matches(word,elements.keys()))>0:
        ele = get_close_matches(word,elements.keys())[0] 
        ans = input("Are you looking for %s instead!(Y/N)"%ele)   
        if ans.lower() == 'y':
            return elements[ele]
        elif ans.lower() == 'n':
            return "Check for spelling mistakes"
        else:
            return "Incorrect Input!"    
    else:
        return "Check for spelling mistakes!"    

word = input("Enter any word to search meanings? ")

finalAnswer=findWord(word)

if type(finalAnswer) == list:
    for i in finalAnswer:
        print("=>",i)
else:
    print(finalAnswer)        
    
 

