import selenium
import getch
from selenium.webdriver.common.keys import Keys
import subprocess as s
import time
driver = webdriver.Chrome(r'/usr/bin/chromedriver')
driver.get('https://web.whatsapp.com')
name = "" # Name you want to set the notification for
def automate(name):
    online_status = driver.find_element_by_xpath('//*[@id="main"]/header/div[2]/div[2]/span').text
    return online_status

def go_to(name):
    driver.find_element_by_xpath('//*[@title="New chat"]').click()
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/label/input').send_keys(name)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[2]/div[1]/div/div/div[2]/div').click()

def check_online(name):
    status = "offline"
    while(status!="online"):
        status = automate(name)
        time.sleep(5)
        automate(name)
    if(status == "online"):
        s.call(['notify-send','WhatsApp Automate',name + ' is Online'])
     
check_online(name)
