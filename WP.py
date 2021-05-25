from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
added_options = webdriver.ChromeOptions()
added_options.add_argument(
    '--user-data-dir= /home/devendra/.config/google-chrome/Default')
added_options.add_argument('--profile-directory=Default')
driver = webdriver.Chrome(
    '/home/devendra/SDP/whatsapp_fry/chromedriver', options=added_options)
driver.get('https://web.whatsapp.com')
print("Scan QR code and hit Enter")
input()
print("Logged in")
time.sleep(1)
contact = input('enter name of contact : ')
msg_type = input(
    'enter 1 for text message \nenter 2 for image \nenter your choice : ')

search_box = driver.find_element_by_xpath(
    "//*[@id='side']/div[1]/div/label/div/div[2]")
search_box.send_keys(contact)
search_box.send_keys(Keys.ENTER)

if(msg_type == 1):
    msg = input('enter the message : ')
    no_of_msg = input('enter number of message : ')
    msg_box = driver.find_element_by_xpath(
        "//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
    time.sleep(1)
    for i in range(no_of_msg):
        msg_box.send_keys(msg)
        msg_box.send_keys(Keys.ENTER)
        time.sleep(0.4)
else:
    file_path = (input("enter file path : "))
    caption = (input("enter caption : "))
    attachment_section = driver.find_element_by_xpath(
        '//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/div')
    image_box = driver.find_element_by_xpath(
        '//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/span/div[1]/div/ul/li[1]/button/span')
    image_box.send_Keys(file_path)
    time.sleep(3)
    caption_box = driver.find_element_by_xpath(
        '//*[@id="app"]/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/div[1]/span/div/div[2]/div/div[3]/div[1]/div[2]')
    caption_box.send_keys(msg)
    send_button = driver.find_element_by_xpath(
        '//*[@id="app"]/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/span/div/div/span')
    send_button.click()
time.sleep(15)
driver.quit()
