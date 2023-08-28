# -*- coding = utf-8 -*-
# Motto : Practice makes perfect.
# Time : 28/8/2023 10:42 am

import re
from typing import Final

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

EMAIL_REGEX: Final[str] = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[
\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[
a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[
0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[
\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""


class Browser:
    def __init__(self, driver: str):
        print('Starting up...')
        self.chrome_options = Options()
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--disable-extensions')
        self.chrome_options.add_argument('--disable-gpu')
        #Discard some unuseful functions

        self.service = Service(driver)
        self.browser = webdriver.Chrome(service=self.service, options=self.chrome_options) #Create an instance by webdriver.Chrome()
        #Start a new browser session
        # After this line, a new Chrome browser instance is running (in headless mode, without extensions, and without GPU acceleration)

    def scape_emails(self, url: str) -> set:
        print(f'Scaping: "{url}" for emails.')
        self.browser.get(url)
        #When we call the get method, Selenium sends a command to the browser asking it to navigate to the given URL.
        #The browser then loads the web page associated with that URL.
        page_source: str = self.browser.page_source
        #The page_source property of the browser instance retrieves the current page's entire HTML source as a string.
        # This means everything from the opening <html> tag to the closing </html> tag is fetched and returned.

        list_of_emails: set = set()
        # Using a set ensures that any duplicate email addresses encountered will be automatically discarded, as sets don't allow duplicate values.
        for re_match in re.finditer(EMAIL_REGEX, page_source):
            #The re.finditer method is a regular expression function that returns an iterator yielding match objects for each match of the regular expression in the string.
            list_of_emails.add(re_match.group())
            #The group() method of a match object is used to retrieve the actual matched string. I
            # In this case, it retrieves the email address that was matched by the regular expression.


        return list_of_emails

    def close_browser(self):
        print('Closing browser...')
        self.browser.close()



def main():
    driver: str = 'chromedriver'  #Path to chromedriver
    browser = Browser(driver=driver)

    emails: set = browser.scape_emails('https://www.randomlists.com/email-addresses?qty=50')

    for i, email in enumerate(emails, start=1):
        print(i, email, sep=': ')


if __name__ == '__main__':
    main()
