import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup



driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('https://www.linkedin.com/login')

nameidElem = driver.find_element_by_id('username')
nameidElem.send_keys('yourLinkedinUsername')

pwdidElem = driver.find_element_by_id('password')
pwdidElem.send_keys('yourLinkedinPassword')

continueElem = driver.find_element_by_class_name("btn__primary--large")
result = continueElem.submit()
time.sleep(10)


while(1):
    url = input("Enter Linkedin Company Url example https://www.linkedin.com/company/total-communications/")
    if(url == "Hello"):
        print("Ignore")
    else:
        try:
            link = url
            driver.get(link)

            firstcompany = driver.find_element_by_link_text("About")
            firstcompany.click()
            time.sleep(2)

            employees = driver.find_element_by_xpath("//a[@data-control-name='topcard_see_all_employees']/span")
            emptext = employees.text
            for word in emptext.split():
                if word.isdigit():
                    print("No. of employees are ", word)
            time.sleep(2)
        except:
            print("Error obtaining- ", url)


