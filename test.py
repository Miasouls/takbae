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
        webdriver_options = webdriver.ChromeOptions()
        webdriver_options .add_argument('headless')
        webdriver_options.add_argument('window-size=1920x1080')



        chromedriver = 'chromedriver.exe'
        driver = webdriver.Chrome(chromedriver, options=webdriver_options )

        driver.get('https://www.cjlogistics.com/ko/tool/parcel/tracking')
        driver.maximize_window()

        elem = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div/div/div[1]/input')
        elem.click()
        elem.send_keys('637529257326')
        driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div/div/div[2]/span[1]/input').click()
        body = driver.find_element_by_css_selector('body')
        body.send_keys(Keys.PAGE_DOWN)
        driver.implicitly_wait(3)
        driver.get_screenshot_as_file('택배.png')
        driver.quit()
        bot.send_photo(chat_id, open('택배.png','rb'))


updater = Updater(my_token, use_context=True)

message_handler = MessageHandler(Filters.text, get_message)
updater.dispatcher.add_handler(message_handler)

updater.start_polling(timeout=3, clean=True)
updater.idle()













    
