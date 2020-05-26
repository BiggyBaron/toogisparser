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
options2.add_argument('headless')
driver = webdriver.Chrome("chromedriver", options=options2)
# bot = telebot.TeleBot("1272517220:AAGp0kXsJc7Ne7qhZudC0EuiF3z1qnUhj4Q")


# @bot.message_handler(commands=['now'])
# def start_message(message):
#     try:
#         dojob(message.chat.id)
#     except:
#         bot.send_message(message.chat.id, "Какая-та ошибка")


base_url = "https://2gis.kz/almaty/search/%D1%88%D0%BA%D0%BE%D0%BB%D0%B0%20%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F%20%D0%BE%D0%BD%D0%BB%D0%B0%D0%B9%D0%BD"

def dojob(chat_id):
    driver.get(base_url)
    time.sleep(2)
    data = driver.find_elements_by_class_name("_1h3cgic")#.get_attribute('innerHTML')
    
    others = driver.find_elements_by_class_name("_1hs4dnvh")

    if len(others) > 0 :
        for el in others:
            url = el.get_attribute('href')
            driver.get(url)
            time.sleep(2)
            data2 = driver.find_elements_by_class_name("_1h3cgic")
            data = data + data2

    if len(data) > 0:
        for el in data:
            url = el.get_attribute('href')
            driver.get(url)
            time.sleep(2)
            name = driver.find_element_by_class_name("_1r7sat2").find_element_by_class_name("_oqoid").get_attribute('innerHTML')
            type = driver.find_element_by_class_name("_11eqcnu").find_element_by_class_name("_oqoid").get_attribute('innerHTML')
            address = driver.find_element_by_class_name("_599hh").find_element_by_class_name("_15t9xwf").find_element_by_class_name("_49kxlr").find_element_by_class_name("_13eh3hvq").get_attribute('innerHTML')
            data = data + data2

    print(len(data))


if __name__=="__main__":
    dojob("536244426")
    # bot.polling()