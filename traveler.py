from country import Country
from utils import get_code
from click import secho
from utils import print_indent


class Traveler:
  ''' 
Travel Class creates a Country class internally in the __init__ method.
self.destination is an instance of the Country class. Thats where the data comes
from. 
'''
"""this class represents travelobject. contains all the data about the travler.
"""

  def __init__(self, vac, origin, destination):
    
      """_init_: this constructor initialize travler object attributes: vac. origin, destination. 
   
    Parameters
    ----------
    vac: boolean
      if person is vacinatated
    origin: str
      the origin country of this travler
    destination: str
      the destination country for this travler 
        """

    self.vac = vac
    self.origin = origin
    self.destination = Country(destination)
   


  def is_banned(self):
    
        """is_banned: this method returns if the origin country is banned in destination country.  
    
    Returns
    -------
    boolean
      returns if origin country is banned in destination country 
    """ 
    origin_code = get_code(self.origin)
    banned_countries, text, rules, exemptions = self.destination.get_banned_data()

    return origin_code in banned_countries
  

    
  def can_travel(self):
    
     """can_travel: this method prints for the travler if he can travler to destination country, by rule or through exemption.   
    """ 
      
    banned_but_vacc = """
    It looks like your country of origin is currently banned from your destination country. 
    But you are vaccinated. 
    Check out the exemptions for your country

    """

    banned= """
    You are banned and cannot travel.
    """

    banned_countries, text, rules, exemptions = self.destination.get_banned_data()
    self.travel_header()
    if self.is_banned():
        if self.vac:
            print(banned_but_vacc)
            print(exemptions)

        else:
            print(banned)
    else:
        all_sets = """
        You are all set to travel! Check out the additional information for your destination:
        """

        print(all_sets) 
        


  def dest_vaccines(self):
       """dest_vaccines: this method prints all the accepted vaccinations at the destination.   
    """ 
    #prints all the accepted vaccinations at the destination
    vaccs = self.destination.get_vaccinations()
    if vaccs is not None:
      secho("The accepted vaccines at the destination country: ")
      for vac in vaccs:
        print_indent(vac)
 
  def travel_header(self):
    
     """travel_header: this method prints the relevant colored header according to results above.    
    """  
    if self.is_banned():
      header = "You are banned"
      secho(header, fg="white", bg="red")
    else:
      header = "You're all good to travel"
      secho(header, fg="black", bg="green")
      
 

  def print_travel_risk(self):
        
 """print_travel_risk: this method prints a colored massege according to the risk level in destenation country.   
    """  
    country = self.destination.get_country()
    message = f'Current risk level in {self.destination.get_country()} based on number of COVID cases: '
    risk_level = self.destination.get_risk()
    color = "white"
    if risk_level.lower() == "low":
        color = "green"
    elif risk_level.lower() == "medium":
      color = "yellow"
    elif risk_level.lower() == "high" :
      color = "red"
    elif risk_level.lower() == "extreme" :
      color = "magenta"
    
    secho(message, nl=False) ##nl means new line
    secho(risk_level, bg=color)


  def print_accepted_certifs(self):
     """print_accepted_certifs: this method prints list of approved certificates with indentation.   
    """ 
    certifs = self.destination.get_certificate()
    secho("These are the accepted proof of vaccination at your destination: ")
    for certif in certifs:
        print_indent(certif)
        


  def print_travel_info(self):
       """print_travel_info: this method prints traver's information: if he can travel, risk, needed  vaccination in destenation country
      and accepted certificates in in destenation country.   
    """  
    self.can_travel()
    print()
    self.print_travel_risk()
    print() #prints a space for the visual aesthetic
    self.dest_vaccines()
    print()
    self.print_accepted_certifs()
    

