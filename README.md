
# SC-Movie
Python library leveraging REST Countries API to fetch and display country-specific data such as capitals, populations, currencies, and languages



## API 
Python Basic API wrapper
```http
  https://restcountries.com/v3.1/
```

## Installation

Install my-project with npm

```bash
  pip install infokannegara
```
    

## Usage

Basic Usage :

```python
from countryinfo.negara import CountryInfo

country_data = CountryInfo()
country_name = input("Masukkan nama negara: ")

capital = country_data.get_country_capital(country_name)
population = country_data.get_country_population(country_name)

if capital and population:
    print(f"Ibu kota dari {country_name} adalah {capital}")
    print(f"Populasi {country_name} adalah {population}")
else:
    print("Data negara tidak ditemukan.")
```

