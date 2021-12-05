from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

usernameStr = '180106008'
passwordStr = '351999@rK'

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
#driver = webdriver.Chrome(options=options)

browser = webdriver.Chrome("C:/chromedriver_win32/chromedriver.exe", options=options)
browser.get(('https://192.168.193.1:1442/login?02fa595bfec228c3'))

# fill in username and hit the next button
username = browser.find_element_by_id('ft_un')
username.send_keys(usernameStr)
#nextButton = browser.find_element_by_id('next')
#nextButton.click()

# wait for transition then continue to fill items
password = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, 'ft_pd')))
password.send_keys(passwordStr)
 
signInButton = browser.find_element_by_css_selector('button')
signInButton.click()

