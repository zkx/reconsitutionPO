from selenium import webdriver
from selenium.webdriver.common.by import By

from pageobjects.page.basepage import BasePage

#BasePage类对通用代码的一个引入，对__init__做一个封装，被其他需要__init__的PO类来调用
#让所有的子类继承BasePage
class Register(BasePage):
    '''
     def __init__(self,driver):
        self.driver = driver
    '''

    def register(self,companyname):
        self.driver.find_element(By.ID, 'corp_name').send_keys(companyname)
        self.driver.find_element(By.ID, 'submit_btn').click()