# -*- coding = utf-8 -*-
# Motto : Practice makes perfect.
# Time : 30/8/2023 1:42 pm

from bs4 import BeautifulSoup
import requests

def get_soup() -> BeautifulSoup:
    headers: dict = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
    request = requests.get('https://www.bbc.com/news', headers=headers)
    #request : <Response [200]>
    # class:`Response <Response>` object
    html: bytes = request.content
    # Content of the response, in bytes.
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def get_headlines(soup: BeautifulSoup) -> list[str]:
    headlines: set = set()

    for h in soup.findAll('h3', class_='gs-c-promo-heading__title'):
        headline: str = h.contents[0].lower()
        headlines.add(headline)
      
    return sorted(headlines)

def check_headlines(headlines: list[str], term: str):
    terms_list: list[str] = []
    terms_found: int = 0

    for i, headline in enumerate(headlines, start=1):
        if term.lower() in headline:
            terms_found += 1
            terms_list.append(headline)
            print(f'{i}: {headline.capitalize()} ----------------{term} is here!')
        else:
            print(f'{i}: {headline.capitalize()}')

    print('Total--------------------------------')
    if terms_found:
        print(f'"{term} was mentioned {terms_found} times !"')
        print('--------------------------------')

        for i, headline in enumerate(terms_list, start=1):
            print(f'{i}: {headline.capitalize()}')

    else:
        print(f'No matches found for "{term}"')
        print('--------------------------------')

def main():
    soup: BeautifulSoup = get_soup()
    headlines: list[str] = get_headlines(soup)

    user_input: str = 'ukraine'
    check_headlines(headlines=headlines, term=user_input)

    for headline in headlines:
        print(headline)


if __name__ == '__main__':
    main()








