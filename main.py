import json
from difflib import get_close_matches

data = json.load(open('data.json'))


def definition(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data)) > 0:
        print(f'did you mean {get_close_matches(word, data, n=1)}')
        yes_no = input('enter Y if yes or N if not: ').lower()
        if yes_no == 'y':
            return data[get_close_matches(word, data.keys(), cutoff=0.8)[0]]
        else:
            return f"the word {word} doesn't exist,double check it"
    else:
        return f"the word {word} doesn't exist,double check it"


word = input('word: ').lower()
toprint = definition(word)
if type(toprint) is list:
    for item in toprint:
        print(item)
else:
    print(toprint)
