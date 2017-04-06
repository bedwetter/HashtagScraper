from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time

from bs4 import BeautifulSoup


# ig scraper
# scrapes popular hashtags

class HashScraper:

    def __init__(self):

        fox_cap = DesiredCapabilities.FIREFOX
        fox_cap['marionette'] = True
        # geckodriver path here!!!!
        fox_cap['binary'] = '/usr/local/bin/geckodriver'

        # Enter phatomjs binary path here!
        self.browser = webdriver.PhantomJS('/Users/downloads/phantomjs')
        # needed
        self.browser.set_window_size(1000, 800)
        self.browser.get("https://www.instagram.com/instagram/")

    def input_tags(self):

        tag_input = input("Enter a hashtag you would like to search: \n")
        # search bar
        search = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div/div/div/div[2]/input')

        if '#' in tag_input:
            search.send_keys(tag_input)
        else:
            search.send_keys('#' + tag_input)

        print("Scraping popular tags...\n")

    def scrape(self):

        # scrape hash tags
        html = self.browser.page_source
        soup = BeautifulSoup(html, 'html.parser')
        for tags in soup.find_all('a', {'class': '_k2vj6'}):
            print('#' + tags.get_text())

    def execute(self):

        self.input_tags()
        # gotta wait sometimes
        time.sleep(3)
        self.scrape()
        self.browser.quit()

if __name__ == '__main__':

    hash_scrape = HashScraper()
    hash_scrape.execute()
