
from selenium import webdriver
from selenium.webdriver.chrome.service import Service #new one
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def stock_info(self, num, path='/Users/pikachu/PycharmProjects/pythonProject/chromedriver'):
    url = 'https://mis.twse.com.tw/stock/fibest.jsp?stock=' + str(num)
    chrome_options = Options()  # 啟動無頭模式
    chrome_options.add_argument('--headless')  # 規避google bug
    chrome_options.add_argument('--disable-gpu')
    s = Service(path)
    browser = webdriver.Chrome(service=s, options=chrome_options)
    browser.get(url)
    browser.get(url)
    element = browser.find_element(By.CSS_SELECTOR, "table[id='tabTrade']>tbody")
    result = element.text.split(' ')
    return result

class stock():

    def __init__(self,num):
        self.all = stock_info(self,num)
        self.time = stock_info(self,num)[0]
        self.price = stock_info(self,num)[1]
        self.change = stock_info(self,num)[2]
        self.volumn = stock_info(self,num)[3]


