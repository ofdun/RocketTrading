from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
#from time import sleep as sl
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import rl_garage_ids


def Divide(string):
    if 'PricesContainer' in string: string = string.replace('PricesContainer', '')
    for i in string:
        if i.isupper(): string = string.replace(i, ' ' + i)
    if 'B M' in string: string = string.replace('B M', 'BM')
    return string

def Poryadok(arr):
    newarr = []
    for i in arr:
        newarr.append( Divide(i) )
    return newarr


rl_garage_ids.Start_Update_Message()


url = 'https://rl.insider.gg/en/pc?mobile'