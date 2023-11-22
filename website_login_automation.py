# import the Selenium library
# Selenium has to be installed on the system  (CMD, "pip install Selenium")

from selenium import webdriver
import yaml

conf = yaml.load(open('loginDetails.yml'))
myEmail = conf['my_user']['email']
myPassword = conf['my_user']['password']
url = conf['my_user']['url']


driver = webdriver.Chrome()

def login(url,usernameId, username, passwordId, password, submit_buttonId):
   driver.get(url)
   driver.find_element_by_id(usernameId).send_keys(username)
   driver.find_element_by_id(passwordId).send_keys(password)
   driver.find_element_by_id(submit_buttonId).click()


# calling the function "login" with the data
login(url, "email", myEmail, "pass", myPassword, "loginbutton")