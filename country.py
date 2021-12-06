from utils import get_code, get_country
from settings import Settings
from amadeus import Client

#calls country information given the name
#gets the code by passing the name to the getcode function
class Country:
  def __init__(self, name):
    self.name = name
    self.code = self.get_code(name) #here
    self.url = '/v1/duty-of-care/diseases/covid19-area-report'
    self.data = self.get_data()
    self.area_restrictions = self.data['areaAccessRestriction']

  def get_country(self):
    return get_country(self.code)

  def get_code(self, name):
    return get_code(name)
  
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
    
  def get_banned_data(self):
      data = self.area_restrictions
      entry = data['entry']
      banned_countries = [country['iataCode'] for country in entry ['bannedArea']]
      text = entry['text']
      rules = entry['rules']
      # entry is a python dictionary .get allows you to set a default if it doesn't exist or returns a null by default
      exemptions = entry.get('exemptions')
      return(banned_countries, text, rules, exemptions)
  
  def get_required_docs(self):
    data = self.area_restrictions
    required = data['declarationDocuments'].get('documentRequired')
    text = data['declarationDocuments'].get('travelDocumentationLink')
    link = data['declarationDocuments'].get('travelDocumentationLink')
    return (required, text, link)
  
  def get_certificate(self):
    data = self.area_restrictions
    certifs = data['diseaseVaccination'].get('acceptedCertificates',["Not Specified"])
    return certifs
  
  def get_vaccinations(self):
    data = self.area_restrictions
    qvac = data['diseaseVaccination'].get('qualifiedVaccines', ["No Vaccines Specified"])
    return qvac

  def get_test(self):
    data = self.area_restrictions
    test_type = data['diseaseTesting'].get('testType')
    return test_type
  
  def get_traveltxt(self):
    data = self.area_restrictions
    travel_text = data['diseaseTesting'].get('text')
    return travel_text
  
  def get_risk(self):
    data = self.data['diseaseRiskLevel']
    return data
    
    