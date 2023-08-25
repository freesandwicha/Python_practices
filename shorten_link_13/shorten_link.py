# -*- coding = utf-8 -*-
# Motto : Practice makes perfect.
# Time : 25/8/2023 8:45 pm

from typing import Final
import requests

API_KEY: Final[str] = 'af6c30b03c12ccdcf95ee284dbb96f6f1195c'
BASE_URL: Final[str] = 'https://cutt.ly/api/api.php'
# Final  is used for type hinting and marking variables as constants.

def shorten_link(full_link: str):
    payload: dict = {'key': API_KEY, 'short': full_link}
    # This dictionary is used to send data to the API.
    #Every time we want to shorten a long link using the cutt.ly service, an API call is made.
    request = requests.get(BASE_URL, params=payload)
    #This line sends a GET request to the cutt.ly API.
    data: dict = request.json()
    #The server typically sends the response back in a JSON format.
    # This line converts that JSON response into a Python dictionary for easier access.

    if url_data := data.get('url'):
        # it's trying to get the value associated with the key 'url' in the data dictionary.
        if url_data['status'] == 7:
            short_link: str = url_data['shortLink']
            print('Link', short_link)
        else:
            print('Error status', url_data['status'])


def main():
    input_link: str = input('Enter a link:')
    shorten_link(input_link)

if __name__ == '__main__':
    main()

