import selenium
import getch
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(r'/usr/bin/chromedriver')
driver.get('https://web.whatsapp.com')
print('Log in to your whatsapp & press [ENTER]')
char = getch.getch()
if(char!="\n"):
    print("Press [ENTER] to continue")
name = input('Enter the name of the person to whom message is to be sent! \n')
driver.find_element_by_xpath('//*[@title="New chat"]').click()
driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/label/input').send_keys(name)
driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[2]/div[1]/div/div/div[2]/div').click()
text = input('What message do you want to send?')
driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(text)
driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.RETURN)
print('Message Sent!')
