import json
from difflib import get_close_matches

data=json.load(open("dictionary.json"))

def translate(w):
  w=w.lower()

  if w in data:
    return data[w]
  elif len(get_close_matches(w,data.keys()))>0:
    yn=input("did u mean % s instead ? Y or N: " %get_close_matches(w,data.keys())[0])
    yn=yn.lower()
    if yn =="y":
      return data[get_close_matches(w,data.keys())[0]]
    elif yn=="n":
      return "the word does not exists..."
    else:
      return "We didnt find word.."

  else:
    print("word not found..")




word=input("Enter a word: ");

output=translate(word);

#print(output);

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
input('Press ENTER to exit')
