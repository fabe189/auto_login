from selenium import webdriver
import yaml

conf = yaml.load(open('loginDetails.yml'))
myFbEmail = conf['fb_user']['email']
myFbPassword = conf['fb_user']['password']