import json

def get_country_list():
    with open("country-codes.json", "r") as f:
        country_list = json.load(f)
    
    return country_list

def get_country(code):
    country_list = get_country_list()
    for k,v in country_list.items():
        if code == v:
            return k
    return code
    
def get_code(name):
    ## gets the two char code
    country_list = get_country_list()
    code = country_list.get(name.lower())
    return code

def print_indent(string, bullet=True):
    indent = "   "
    if bullet:
        indent = "   -"
    print(indent + string)