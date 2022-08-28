from selenium import webdriver
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs


url = 'https://rl.insider.gg/en/pc?mobile'


def Get_Containers(url):
    options = webdriver.EdgeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Edge(options=options)
    driver.get(url)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "paintedDecalsPricesContainer")))
    html = driver.find_element(By.ID, 'itemPricesContainer')
    all_items_page = html.get_attribute('innerHTML')
    soup = bs(all_items_page, 'html.parser')
    all_ids = []
    for i in soup.find_all(class_='priceTableContainer'):
        with open(r'__pycache__/rl_insider_htmls/rli_{}.html'.format(i.get("id")), 'w', encoding='utf-8') as f:
            f.write(str(i))
        all_ids.append(i.get('id'))
    return all_ids

print( Get_Containers(url) )