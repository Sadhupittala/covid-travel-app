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

## MODULES

GitHub Link: https://github.com/Sadhupittala/Python4DS

- Input | Passenger Information:
  Users will be asked to provide their current vaccination status, date of vaccination and current location in order to assess if they meet travel requirements.

- Scrape and HTTP Request COVID travel requirement data to return information:
  Our program would access online government websites and scrape information regarding their current travel requirements. For example, while Germany does not require COVID tests for vaccinated international travelers, the United Kingdom requires COVID tests prior to boarding and a test booking number for after landing. This information would then be compared to the users’ information in order to determine if they are eligible to travel into that country or not. As these government websites are updated, the COVID passenger information would also be updated, ensuring that the passenger does not travel with old information regarding requirements.
- Present resources regarding what documents are required for travel registration
  Most countries currently have passenger registration and locator forms for all international travellers. The program would pull links to these forms from each of the earlier mentioned government sites to present them in an easy to access area for the user to find and fill out.
- Compare COVID-19 regulations and make suggestions
  Users would be able to compare their current travel eligibility with countries across the board. Countries that they are currently eligible to travel to would display in green whereas countries that are closed would be displayed in red.
- Present data on current COVID numbers
  Users would also be able to determine if they would like to still travel to the country at hand based on current COVID numbers. These stats would be scraped from across the web as most government health agencies currently have a COVID tracker that presents up to date infection information.
  This would also potentially display what level each country is open, for example the user could determine whether or not they want to travel to a certain area depending on if indoor dining is open or if mask mandates are still in effect.
- Output Overview:
  To summarize, program output would entail the current travel status of the user (good to travel, missing documents/requirements, cannot travel) as well as information regarding current COVID conditions within the intended country of travel.
