import json

def get_country_list():
    
"""
get_country_list: this function reads the URL and maps the country to its own code from the site
Gets the list of country with the codes since each country has a two letter code. this is the code that the API uses

Returns
-------
country_list: dictionary 
   a dictionary where the key is the country name and the value is a code 
"""
    with open("country-codes.json", "r") as f:
        country_list = json.load(f)
    
    return country_list


def get_country(code):
 
"""get_country: this function returns the country that matches to the given code, if there is no such country it returns the code 

    Parameters
    ----------
    code: str
      country code
    
    Returns
    -------
    code: str
        returns country name if exsist else return the code 
    """

    country_list = get_country_list()
    for k,v in country_list.items():
        if code == v:
            return k
    return code

    
def get_code(name):
 
"""get_code: this function returns the country code that matches  the given country, if there is no such code it returns null 

    Parameters
    ----------
    name: str
      country name
    
    Returns
    -------
    code: str
        returns country code if exsist else return null 
    """

    ## gets the two char code
    country_list = get_country_list()
    code = country_list.get(name.lower())
    return code


def print_indent(string, bullet=True):
    """print_indent: this function prints indents with bullets or without according the flag bullet
 
    Parameters
    ----------
    string: str
      the string we want to print
    bullet: boolean
      a flag represent if we want bullet, the default value is true    
    """
    indent = "   "
    if bullet:
        indent = "   -"
    print(indent + string)
    
 
