from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

class Spyder(object):
    name = 'MyCustomSpyder'
    start_urls = [
        'http://www.ebay.com/sch/i.html?&_nkw=apple',
        'http://www.ebay.com/sch/i.html?&_nkw=motorola'
    ]
    xpath_items = '//ul[@id="ListViewInner"]/li'
    items_output = []

    def __init__(self):
        print 'starting the spyder ' + self.name
        self.driver = webdriver.Firefox()

    def trace(self, message):
        print 'log: ' + message
    
    def start(self):
        for url in self.start_urls:
            self.navigate_to(url)

    def navigate_to(self, url):
        self.driver.get(url)
        self.crawl_page()

    def crawl_page(self):
        self.trace('begin parsing')
        page_items = self.find_elements_by_xpath(self.xpath_items)
        index = 1
        for item in page_items:
            self.parse_item(item, index)
            index = index + 1

    def parse_item(self, item, index):
        #self.trace('parsing item')
        self.trace('item ==> ' + item.text)
        element = self.find_by_xpath('//ul[@id="ListViewInner"]/li[' + str(index) + ']/h3/a')
        #item = 
        self.items_output.append(element.text)

    #helpers from here
    def find_by_xpath(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locator))
        )
        return element
    
    def find_elements_by_xpath(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locator))
        )
        return self.driver.find_elements_by_xpath(locator)

    def find_by_name(self, name):
        element = WebDriverWait(self.driver, 10).until(lambda driver: self.driver.find_element_by_name(name))
        return element

    def find_by_id(self, id):
        element = WebDriverWait(self.driver, 10).until(lambda driver: self.driver.find_element_by_id(id))
        return element
        
    def wait_for_title(self, title):
        print('old ' + self.driver.title)
        wait = WebDriverWait(self.driver,10)
        wait.until(lambda driver: self.driver.title.lower().startswith(title))
        print('title ' + self.driver.title)
        
    def wait_for_different_title(self, title):
        print('old ' + self.driver.title)
        wait = WebDriverWait(self.driver,10)
        wait.until(lambda driver: self.driver.title != title)
        print('title ' + self.driver.title)
        
    def get_last_title(self):
        return self.driver.title
        
    def __del__(self):
        self.driver.quit()    

spyder = Spyder()
spyder.trace('init')
spyder.start()