#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
import os
import datetime
import sys
import telebot


options2 = webdriver.ChromeOptions()
options2.add_argument('--no-sandbox')
options2.add_argument('--headless')
options2.add_argument('--disable-gpu')
driver = webdriver.Chrome("chromedriver", options=options2)
# driver = webdriver.Chrome("chromedriver")

# bot = telebot.TeleBot("1272517220:AAGp0kXsJc7Ne7qhZudC0EuiF3z1qnUhj4Q")


# @bot.message_handler(commands=['now'])
# def start_message(message):
#     try:
#         dojob(message.chat.id)
#     except:
#         bot.send_message(message.chat.id, "Какая-та ошибка")


base_url = "https://2gis.kz/nur_sultan/search/%D0%BF%D0%BE%D0%BB%D0%B8%D1%86%D0%B8%D1%8F"

def dojob(put_url_here):
    driver.get(base_url)
    data = []
    new_flags = driver.find_elements_by_class_name("_1h3cgic")
    if len(new_flags) > 0:
        for flag in new_flags:
            data2 = str(flag.find_element_by_class_name("_13ptbeu").get_attribute('href')).split("?")[0]
            data.append(data2)
    
    others = driver.find_elements_by_class_name("_1hs4dnvh")
    others_urls = []
    if len(others) > 0 :
        for el in others:
            url = str(el.get_attribute('href'))
            if "search" in url and "page" in url:
                others_urls.append(url)

        for url in others_urls:
            driver.get(url)
            flags = driver.find_elements_by_class_name("_1h3cgic")
            for flag in flags:
                data2 = str(flag.find_element_by_class_name("_13ptbeu").get_attribute('href')).split("?")[0]
                data.append(data2)
    

    
    driver.close()
    print(data)


def analyze_page(url):
    driver.get(url)
    names = driver.find_elements_by_class_name("_oqoid")
    name = names[0]
    details = names[1]
    print(name)
    print(details)
    tels = driver.find_elements_by_partial_link_text("tel:")
    for tel in tels:
        tel.get_attribute("href").split("tel:")[1]
        print(tel)
    mails = driver.find_elements_by_partial_link_text("mailto:")
    for mail in mails:
        mail.get_attribute("href").split("mailto:")[1]
        print(mail)
    


if __name__=="__main__":
    analyze_page("https://2gis.kz/nur_sultan/firm/70000001041671674")
    # dojob("536244426")
    # bot.polling()


    # driver.get(url)
    #         time.sleep(2)
    #         data2 = driver.find_elements_by_class_name("_1h3cgic")
    #         data = data + data2