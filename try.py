import json
from difflib import get_close_matches
data=json.load(open("data.json"))

def define(alpha):
    alpha=alpha.lower()
    if alpha in data:
        return data[alpha]
    elif alpha.upper() in data:
        return data[alpha.upper()]
    elif alpha.title() in data:
        return data[alpha.title()]
    elif len(get_close_matches(alpha,data.keys())[0]) > 0:
        confirm=input("DID YOU MEAN '%s' INSTEAD.ENTER Y FOR YES AND N FOR NO." % get_close_matches(alpha,data.keys())[0])    
        if confirm == "Y":
            return data[get_close_matches(alpha,data.keys())[0]] 
        elif confirm == "N":
            return "PLEASE ENTER A VALID WORD."
        else:
             return "PLEASE ENTER A VALID WORD."         
    else:
        return "PLEASE ENTER A VALID WORD."

word = input("ENTER WORD : ")
output = define(word)
if isinstance(output,list):
    for item in output:
        print(item)
else:
    print(output)                        