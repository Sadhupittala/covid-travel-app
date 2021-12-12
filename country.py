from utils import get_code, get_country
from settings import Settings
from amadeus import Client

#calls country information given the name
#gets the code by passing the name to the getcode function

"""this class represents countryobject. contains all the data about the country and covid retrictions.
"""
class Country:

  def __init__(self, name):
    self.name = name
    self.code = self.get_code(name) #here
    self.url = '/v1/duty-of-care/diseases/covid19-area-report'
    self.data = self.get_data()
    self.area_restrictions = self.data['areaAccessRestriction']
 """_init_: this constructor initialize country object attributes: name, code, URL, data, area restrictions 
   
    Parameters
    ----------
    name: str
      country name
        """
  def get_country(self):
    return get_country(self.code)
 """get_country: returns the country name from API 
      Returns
      -------
      str: 
          returns country name  
      """
  def get_code(self, name):
    return get_code(name)
  """get_code: returns the code that matches the given country name from API 

      Parameters
      ----------
      name: str
        country name
      
      Returns
      -------
      code: str
          returns country code if exsist else return null 
      """
  def get_data(self):
    ##amadeus API call
    client_id = Settings['AMADEUS_CLIENT_ID']
    client_secret = Settings['AMADEUS_SECRET']

    if client_id is None or client_secret is None:
      raise("You must provide authentication for the Amadeus API")

    amadeus = Client(
        client_id = client_id,
        client_secret = client_secret
    )
    res = amadeus.get(self.url, countryCode = self.code)
    return res.data
  
  """get_data: this function uses amadeus API to get the data from the site  

    Returns
    -------
    res: dictionary
        returns the data from the site  
    """
    
  def get_banned_data(self):
      data = self.area_restrictions
      entry = data['entry']
      banned_countries = [country['iataCode'] for country in entry ['bannedArea']]
      text = entry['text']
      rules = entry['rules']
      # entry is a python dictionary .get allows you to set a default if it doesn't exist or returns a null by default
      exemptions = entry.get('exemptions')
      return(banned_countries, text, rules, exemptions)
  
    """get_banned_data: this function get and returns all country's covid information.  
    
    Returns
    -------
    tuple (of four):
        returns the tupel contains:
        1. banned_countries - list of banned countries
        2. text: dicationary    
        3. rulles: string that represents the country's rules
        4. exemptions: string that represents the country's exemptions from above rules
    """
    
  def get_required_docs(self):
    data = self.area_restrictions
    required = data['declarationDocuments'].get('documentRequired')
    text = data['declarationDocuments'].get('travelDocumentationLink')
    link = data['declarationDocuments'].get('travelDocumentationLink')
    return (required, text, link)
      
      """get_required_docs: this funcation returns all the document information needed.  
    
    Returns
    -------
    tuple (of three):
        returns the tupel contains:
        1. breuired - list of required documents ???
        2. text: string that represents ??  
        3. link: string that represents URL to read more information about needed documents ??
    """
      
  def get_certificate(self):
    data = self.area_restrictions
    certifs = data['diseaseVaccination'].get('acceptedCertificates',["Not Specified"])
    return certifs
  
   """get_certificate: this function returns if country recognize this vaccination certificate.  
    
    Returns
    -------
    certifs: string???
    """ 
    
  def get_vaccinations(self):
    data = self.area_restrictions
    qvac = data['diseaseVaccination'].get('qualifiedVaccines', ["No Vaccines Specified"])
    return qvac

    """get_vaccination: this function returns a list of country's qualified vaccinations.  
    
    Returns
    -------
    qvac: list of qualified vaccines
    """ 
    
  def get_test(self):
    data = self.area_restrictions
    test_type = data['diseaseTesting'].get('testType')
    return test_type
    """get_test: this function returns whish covid test is needed for entry.  
    
    Returns
    -------
    test_type: str
      returns the test type
    """ 
    
  def get_traveltxt(self):
    data = self.area_restrictions
    travel_text = data['diseaseTesting'].get('text')
    return travel_text
  
   """get_traveltxt: str 
    
    Returns
    -------
    travel_text: str
      returns data from the original data received from the API
    """ 
    
  
  def get_risk(self):
    data = self.data['diseaseRiskLevel']
    return data
    
      """get_risk: this function returns the covid risk level of this country.  
    
    Returns
    -------
    data: str ???
      returns the risk level 
    """ 
    
