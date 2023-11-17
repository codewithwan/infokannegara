import requests

class CountryInfo:
    def __init__(self):
        self.base_url = "https://restcountries.com/v3.1/"

    def get_country_info(self, country_name):
        url = f"{self.base_url}name/{country_name}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_country_capital(self, country_name):
        country_info = self.get_country_info(country_name)
        if country_info:
            return country_info[0]['capital']
        else:
            return None

    def get_country_population(self, country_name):
        country_info = self.get_country_info(country_name)
        if country_info:
            return country_info[0]['population']
        else:
            return None
