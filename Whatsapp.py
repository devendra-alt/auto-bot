from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

browser = webdriver.Chrome('/home/devendra/SDP/whatsapp_fry/chromedriver')
browser.get('https://web.whatsapp.com/')
wait = WebDriverWait(browser,1000)

user = '"Eat code sleep repeat"'
msg = "message by whatsapp bot"
x_arg = ' //span[contains(@title,'+ user +')]'
target = wait.until(ec.presence_of_element_located((By.XPATH,x_arg)))

target.click()

input_box = browser.find_element_by_class_name('2_1wd')

for i in range(10):
    input_box.send_keys(msg + Keys.ENTER)
    


