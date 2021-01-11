import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

REQUEST_URL = 'http://45.79.43.178/source_carts/wordpress/wp-admin/'
POST_URL_LOGIN = 'http://45.79.43.178/source_carts/wordpress/wp-login.php?loggedout=true&wp_lang=en_US'


def using_request():
    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }

    data = {
        'log': 'admin',
        'pwd': '123456aA',
        'wp-submit': 'Log In',
        'redirect_to': 'http://45.79.43.178/source_carts/wordpress/wp-admin/',
        'testcookie': 1
    }

    with requests.Session() as s:
        post = s.post(POST_URL_LOGIN, data=data)
        r = s.get(REQUEST_URL, headers=headers, cookies=post.cookies)
        # check resource site after login
        # print(r.text)
        bs_content = bs(r.content, 'html.parser')
        print('Current username: ' + bs_content.find('span', {'class', 'display-name'}).text)


def using_selenium():
    """
    Command to auto open Chrome:
    - brew cask install chromedriver
    - which chromedriver
    """

    try:
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)

        driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=chrome_options)
        driver.set_window_size(1800, 900)
        driver.get(POST_URL_LOGIN)
        username = 'admin'
        password = '123456aA'

        driver.execute_script(f'var element = document.getElementById("user_login"); element.value = "{username}";')
        driver.execute_script(f'var element = document.getElementById("user_pass"); element.value = "{password}";')
        driver.execute_script(f'document.getElementById("wp-submit").click();')

        # check resource site after login
        # print(driver.page_source)
        bs_content = bs(driver.page_source, 'html.parser')
        print('Current username: ' + bs_content.find('span', {'class', 'display-name'}).text)
    except Exception as e:
        print(e)


using_request()
using_selenium()
