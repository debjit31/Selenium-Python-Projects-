from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import time

myContacts = []
class Contact:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    def getName(self):
        return self.name

    def getNumber(self):
        return self.contact

def automateWhatsApp():
    driver = webdriver.Chrome()
    driver.get('https://web.whatsapp.com/')
    driver.maximize_window()
    time.sleep(15)
    user_name = "Whatsapp Selenium Testing"
    chat = driver.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
    chat.click()

    time.sleep(3)

    for i in range(len(myContacts)):
        name = 'Name :- ' + myContacts[i].getName()
        mb = driver.find_element_by_xpath('//div[@class="_3uMse"]')
        time.sleep(1)
        mb.send_keys(name)
        time.sleep(1)
        send_btn = driver.find_element_by_xpath('//button[@class="_1U1xa"]')
        send_btn.click()
        time.sleep(1)
        contact = 'Contact Number :- ' + myContacts[i].getNumber()
        mb = driver.find_element_by_xpath('//div[@class="_3uMse"]')
        time.sleep(1)
        mb.send_keys(contact)
        time.sleep(1)
        send_btn = driver.find_element_by_xpath('//button[@class="_1U1xa"]')
        send_btn.click()
        time.sleep(1)

with open('phonenumbers.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        myContacts.append(Contact(row[0], row[1]))
    automateWhatsApp()




