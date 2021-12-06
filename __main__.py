from traveler import Traveler
from utils import get_country_list

country_list = get_country_list()

if __name__ == "__main__":
    orig = 0
    while orig == 0:
        input1 = input("Please insert your country of origin: ").lower()
        if input1 in country_list:
            orig = input1
        else: print("We could not find your country, have you mispelled the name?")

    destin = 0
    while destin == 0:
        input2 = input("Please insert the country of destination: ").lower()
        if input2 != orig:
            if input2 in country_list:
                destin = input2
            else: print("We could not find your country, have you mispelled the name?")
        else: print("Your destination country is the same as your origin country. Please reenter the correct destination country.")
    
    vaccination = 5
    while vaccination == 5: 
        input3 = input("Will you be fully vaccinated at the day you are planning to travel, with the vaccination day being at least 14 days ago? Please answer YES or NO: ")
        if input3.lower() == "yes":
            vaccination = True
        elif input3.lower() == "no":
            vaccination = False
        else: print("Please answer with either YES or NO")

    traveler = Traveler(vaccination, orig, destin)
    traveler.print_travel_info()