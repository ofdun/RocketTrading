#import  requests as req
from bs4 import BeautifulSoup as bs4
import requests as req
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#rlg-trade__items.html == html
def Get_Item_Price(html, needable_item_id):
    try:
        soup = bs4(html, 'html.parser')
        soup = soup.find(class_='rlg-trade__items')
        itemhas = soup.find('div')
        itemwant = soup.find(class_='rlg-trade__itemswants')
        for count, file in enumerate(itemhas.findAll(class_='--hover'), start=1):
            href = file.find_all('a')[1].get('href')
            item_id = href[href.find('=') + 1:href.find('&')]
            if item_id == needable_item_id:
                order = count
                break
        for count, file in enumerate(itemwant.findAll(class_='--hover'), start=1):
            if count != order: continue
            quantity = file.find(class_='rlg-item__quantity')
            return int(quantity.text)
    except:
        return 'cost not found :('

def Get_Trade_Items_Htmls(trade_url):
    try:
        options = webdriver.EdgeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Edge(options=options)
        driver.get(trade_url)
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'rlg-trade__items')))
        #WebDriverWait(driver, 10).until(
            #EC.presence_of_element_located((By.XPATH, '//*[@id="acceptPrivacyPolicy"]')))
        driver.find_element(By.XPATH, '//*[@id="acceptPrivacyPolicy"]').click()
        driver.find_element(By.XPATH, '/html/body/main/div/div/div[1]/div[2]/div/div/form/input').click()
        #page = element.get_attribute('innerHTML')
        html = driver.page_source
        time.sleep(100)
        #soup = bs4(page, 'html.parser')
        return 'soup'
    except:
        return 'error'

#print( Get_Item_Price(html=open(r'c:/Users/elik3/source/repos/RocketTrading/RocketTrading/testing/test_price.html'), needable_item_id='1536') )

print( Get_Trade_Items_Htmls(trade_url='https://rocket-league.com/trading?filterItem=270&filterCertification=N\
    &filterPaint=N&filterSeries=A&filterMinCredits=0&filterMaxCredits=100000&filterPlatform%5B%5D=1&filterSearchType=1&filterItemType=0'))