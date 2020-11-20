from django.test import TestCase
import requests
import fake_useragent
from bs4 import BeautifulSoup

user = fake_useragent.UserAgent().random
header = {'user-agent': user}

link = 'https://www.slo.ru/'
responce = requests.get(link, headers=header).text
soup = BeautifulSoup(responce, 'lxml')
block = soup.find("div", class_='flx')

for i in range(4):
    check_js = block.find_all('p', class_='news-desc')[i].text
    result_js = f'chrome: {check_js}'
    #
    # check_agent = block.find('div', id='user_agent').text
    # result_agent = f'{check_agent}'
    #
    # check_window = block.find_all('script')[2]

    print(result_js)
