from tkinter import Y
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import numpy as np
import os.path


global url
url = 'https://rocket-league.com/trading'


def Start_Update_Message():
    global dictionary
    try:
        dictionary = np.load('c:/Users/elik3/.Projects/RocketTrading/dictionary_saves/rlg_all_items_id.npy',allow_pickle='TRUE').item()
        if str(input('Would You like to update the data? (Y/N):\n')).lower() == 'y':
            Update_data()
    except:
        dictionary = {}
        Update_data()

def Get_Rocket_League_Garage_htmls(url):
    global array_of_file_names
    array_of_file_names = []
    options = webdriver.EdgeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Edge(options=options)
    driver.get(url)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'filterItem')))
    all_items_page = element.get_attribute('innerHTML')
    soup = bs(all_items_page, 'html.parser')
    with open('c:/Users/elik3/.Projects/RocketTrading/rl_garage_htmls/rlg_FullPage.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
    for i in soup.find_all('optgroup'):
        if i.get('label') == "Categories": continue
        array_of_file_names.append(f'rlg_{i.get("label").replace(" ", "_")}.html')
        with open(f'c:/Users/elik3/.Projects/RocketTrading/rl_garage_htmls/rlg_{i.get("label").replace(" ", "_")}.html', 'w', encoding='utf-8') as f:
            f.write(str(i))
    return 'Rocket League Garage categories updated successfully'


def Update_data():
    Get_Rocket_League_Garage_htmls(url)
    Get_item_ids()
    print('Everything updated successfully')
    return 'Everything updated successfully'


def Get_item_ids():
    for i in range(len(array_of_file_names)):
        with open(f'c:/Users/elik3/.Projects/RocketTrading/rl_garage_htmls/{array_of_file_names[i]}', 'r') as html_group_file:
            soup = bs(html_group_file, 'html.parser')
            for i in soup.find_all('option'):
                if i.get('value') == '341':
                    dictionary['341'] = 'Piñata'
                    continue
                dictionary[i.get('value')] = i.text.replace('\n','')[:-1]
    np.save('c:/Users/elik3/.Projects/RocketTrading/dictionary_saves/rlg_all_items_id.npy', dictionary) 
    return 'Rocket League Garage item ids updated successfully'

print( Start_Update_Message() )