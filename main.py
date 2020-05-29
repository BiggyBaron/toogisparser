#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
import os
import datetime
import sys
import telebot
from copy import deepcopy
import pandas as pd


options2 = webdriver.ChromeOptions()
options2.add_argument('--no-sandbox')
options2.add_argument('--headless')
options2.add_argument('--disable-gpu')
driver = webdriver.Chrome("chromedriver", options=options2)
bot = telebot.TeleBot("1272517220:AAGp0kXsJc7Ne7qhZudC0EuiF3z1qnUhj4Q")


@bot.message_handler(content_types=['text'])
def start_message(message):
    try:
        dojob(message.chat.id, message.text)
    except:
        bot.send_message(message.chat.id, "Неправильный URL")


def dojob(id, base_url):
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
    bot.send_message(id, "Короче тут компаний ровно: " + str(len(data)) + " и я пошел ебашить")
    finds = []
    for url in data:
        finds.append(analyze_page(url))
    
    df = pd.DataFrame.from_dict(finds)
    df.to_excel('finds.xlsx')
    bot.send_document(id, "finds.xlsx")


def analyze_page(url):
    value = {
        "name": "",
        "info": "",
        "tel": "",
        "email": "",
        "address": ""
    }

    driver.get(url)
    names = driver.find_elements_by_class_name("_oqoid")
    value["info"] = names[1].text
    value["name"] = name[0].text
    infos = driver.find_elements_by_class_name("_84s065h")

    for info in infos:
        if "geo" in info.get_attribute("href"):
            value["address"] = info.text
        elif "tel" in info.get_attribute("href"):
            value["tel"] = info.get_attribute("href").split("tel:")[1]
        elif "mailto:" in info.get_attribute("href"):
            value["email"] = info.text

    return value.deepcopy()

if __name__=="__main__":
    bot.polling(none_stop=True)