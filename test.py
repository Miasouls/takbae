from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium
import pyautogui as gui
import time
import telegram
from telegram.ext import Updater, MessageHandler, Filters
bot = telegram.Bot(token='1683470996:AAEZEFlA913cDBYaqtNbxu838jpAMZpU95M')


my_token = '1683470996:AAEZEFlA913cDBYaqtNbxu838jpAMZpU95M'

print('start telegram chat bot')

# message reply function
def get_message(update, context):
    chat_id = 1638812607
    text = update.message.text
    if '택배' in text:
        
        bot.send_photo(chat_id, open('택배.png','rb'))


updater = Updater(my_token, use_context=True)

message_handler = MessageHandler(Filters.text, get_message)
updater.dispatcher.add_handler(message_handler)

updater.start_polling(timeout=3, clean=True)
updater.idle()













    
