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


base_url = "https://2gis.kz/nur_sultan/search/qmobot"

def dojob(chat_id):
    driver.get(base_url)
    print("Got url")
    time.sleep(2)
    data = []


    new_flags = driver.find_elements_by_class_name("_1h3cgic").get_attribute('href')
    if len(new_flags) > 0:
        for flag in flags:
            data2 = base_url.split("/search/")[0] + str(flag.get_attribute('href'))
            data.append(data2)
    
    others = driver.find_elements_by_class_name("_1hs4dnvh")

    print("Len of data is: " + str(len(data)))
    print("Len of others is: " + str(len(others)))

    data_urls = []
    others_urls = []

    if len(others) > 0 :
        for el in others:
            url = base_url.split("/search/")[0] + str(el.get_attribute('href'))
            others_urls.append(url)

        for url in others_urls:
            driver.get(url)
            time.sleep(2)
            flags = driver.find_elements_by_class_name("_1h3cgic")
            for flag in flags:
                data2 = base_url.split("/search/")[0] + str(flag.get_attribute('href'))
                data.append(data2)
    
    print(data)


if __name__=="__main__":
    dojob("536244426")
    # bot.polling()


    # driver.get(url)
    #         time.sleep(2)
    #         data2 = driver.find_elements_by_class_name("_1h3cgic")
    #         data = data + data2