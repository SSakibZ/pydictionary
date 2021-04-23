import json
import difflib
from difflib import get_close_matches

data = json.load(open("dic.json"))

def translate(word):
    word = word.lower()
    if word in data:
        print("<-------------------------Output------------------------->")
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print(f'Did you mean {get_close_matches(word, data.keys())[0]}?')
        decide = input("press y for yes and n for no: ")
        if decide == 'y':
            print("<-------------------Close Matches--------------------->")
            return(data[get_close_matches(word, data.keys())[0]])
        elif decide == 'n':
            return("Can't find...\nTry new word 😉")
        else:
            print("<-----------------------Error------------------------->")
            return("You have entered wrong input. Please enter just y or n")
    else:
        print("<-----------------------Error------------------------->")
        print("Can't find...\nTry new word 😉")


word = str(input("Enter the name to search: "))
output = translate(word)

if type(output) == list:
    for item in output:
        print(f'~ {item}')
else:
    print(output)
