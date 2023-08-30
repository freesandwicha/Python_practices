# -*- coding = utf-8 -*-
# Motto : Practice makes perfect.
# Time : 30/8/2023 10:15 am

import json
from typing import Final
import requests

BASE_URL: Final[str] = 'http://api.exchangeratesapi.io/v1/latest'
API_KEY: Final[str] = '' 


# This function fetches exchange rates either from a local JSON file (rates.json) or from the online API,
def get_rates(mock: bool = False) -> dict:
    if mock:
        with open('rates.json', 'r') as file:
            return json.load(file)

    payload: dict = {'access_key': API_KEY}
    request = requests.get(url=BASE_URL, params=payload)
    # The params=payload argument appends the payload as query parameters to the URL.
    data: dict = request.json()
    # After receiving the response from the server, this method converts the JSON data in the response into a Python dictionary.

    # Create the file
    # with open('rates.json', 'w') as file:
    #     json.dump(data, file)
    return data
    #Regardless of whether the data was fetched from the local file or the online API, the function will return the exchange rates as a Python dictionary.

def get_currency(currency: str, rates: dict) -> float:
    currency: str = currency.upper()
    if currency in rates.keys():
        return rates.get(currency)
    else:
        raise ValueError(f'{currency} is not a valid currency.')


def convert_currency(amount: float, base_cur: str, vs_cur: str, rates: dict) -> float:
    base_rate: float = get_currency(base_cur, rates)
    vs_rate: float = get_currency(vs_cur, rates)

    conversion: float = round((vs_rate / base_rate) * amount, 2)
    print(f'{amount:,.2f} ({base_cur}) is {conversion:,.2f}({vs_cur}) ')
    return conversion


def main():
    data: dict = get_rates(mock=True)
    rates: dict = data.get('rates')

    convert_currency(100, 'AUD', 'CNY', rates)


if __name__ == '__main__':
    main()
