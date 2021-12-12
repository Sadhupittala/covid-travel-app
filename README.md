# COVID TRAVEL APPLICATION (name pending)

## Run Development

To run locally for development purposes, clone the repository. Install the `requirements.txt`. And then create
an account at [Amadeus API](https://developers.amadeus.com/). Add your amadeus credintials, `client_id` and `client_secret`, to a `.env` file as shown below.

```
AMADEUS_CLIENT_ID='yourclientid'
AMADEUS_SECRET='yourclientsecret'
```

**NOTE**: Make sure the `.env` file is within the working directory of the `settings.py`.

**NOTE**: If installing with conda you may have to install `amadeus` and `python-dotenv` using pip after your base python environment is created.

## Synopsis

International travel since the onset of the pandemic has become an increasing challenge. Passengers have been forced to comply with ever changing travel restrictions, not only pertaining to their final destination but also with intermediary nations, and their home country once they return. Furthermore, a pandemic like the current one can technically happen any time again. Our tool will enable the user to better keep up with the changing regulations. The user will be able to select the country he is interested in and input his or her vaccination status. Upon this request, the data for this input is scraped from the respective government websites using the web scraping tool beautiful soup. The user would then obtain information regarding their country of travel and their current eligibility--as well as any missing documentation or requirements.

### Benefits

The tool will provide users with straightforward, comprehensive, and clear information on the country of destination, including the restrictions in place, the required documentation, and the number of new COVID-19 cases. It will hence save users time, allow for quick comparisons among traveling destinations, and avoid inconveniences.

# Documentation

### class Country

  __init__: this constructor initialize country object attributes: name, code, URL, data, area restrictions 

  ##### Parameters
  ----------
  name: str
  country name
  
#### def get_country(self):
  Gets the country name
  
  ##### Returns
  -------
  str: 
      returns country name  

#### def get_code(self, name):

  get_code: returns the code that matches the given country name
  
  ##### Parameters
  ----------
  name: str
    country name

  ##### Returns
  -------
  code: str
      returns country code if exsist else return null 
   
   
#### def get_data(self):
  get_data: this function uses amadeus API to get the data from the site  
  
  ##### Returns
  -------
  res: dictionary
      returns the data from the site  
      
####  def get_banned_data(self):
  get_banned_data: this function get and returns all country's covid information.  
    
  ###### Returns
  -------
  tuple (of four):
      returns the tupel contains:
      1. banned_countries - list of banned countries
      2. text: dicationary    
      3. rulles: string that represents the country's rules
      4. exemptions: string that represents the country's exemptions from above rules
####   def get_required_docs(self):
  get_required_docs: this funcation returns all the document information needed.  
    
 ##### Returns
  -------
  tuple (of three):
      returns the tupel contains:
      1. required: list of required documents from teavler 
      2. text: string
      3. link: string that represents URL to read more information about needed documents

####  def get_vaccinations(self):
  get_vaccination: this function returns a list of country's qualified vaccinations.  
    
  ##### Returns
  -------
  qvac: list of qualified vaccines
  
####  def get_test(self):
  get_test: this function returns whish covid test is needed for entry.  
    
 ##### Returns
  -------
  test_type: str
    returns the test type
    
####  def get_traveltxt(self):
  get_traveltxt: str 
    
  ##### Returns
    -------
  travel_text: str
    returns data from the original data received from the API

####   def get_risk(self):
  get_risk: this funcation returns the covid risk level of this country.  
    
   ##### Returns
  -------
  data: str 
    returns the risk level 

