from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# driver = webdriver.Chrome()
# driver.get('chromedriver.exe')
# driver = webdriver.Chrome('chromedriver.exe')
# driver.get('https://web.whatsapp.com/')

name = input('Enter the name of user or group : ').split()
msg = input('Enter the message : ')
# count = int(input('Enter the count : '))

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://web.whatsapp.com/')

wait = WebDriverWait(driver, 600)
#
for i in range(len(name)):
    msg_box = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/label/div/div[2]')))
    msg_box.send_keys(name[i] + Keys.ENTER)

    input_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    for i in range(1000):
        input_box.send_keys(msg + Keys.ENTER)
