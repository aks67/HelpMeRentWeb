import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time



def gen_url(br, postcode, budget):
    budget = round(budget / 50) * 50

    url = f'https://www.realestate.com.au/rent/with-{br}-bedrooms-between-0-{budget}-in-{postcode}/list-1?maxBeds=3&source=refinement'
    return url

def scraper(url):
    # driver = webdriver.Chrome()
    # url = 'https://www.selenium.dev/documentation/'
    # driver.get(url)
    # time.sleep(10)
    # # page_source = driver.page_source
    # # print(div_with_residential_title)

    
    options = webdriver.ChromeOptions() 
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.realestate.com.au/sold/")
    print(driver.page_source)


    # driver.quit()


if __name__ == '__main__':
    print(gen_url(3, 2033, 900))