import os
import sys
import json

PARENT_PATH = os.path.abspath("..")
if PARENT_PATH not in sys.path:
    sys.path.insert(0, PARENT_PATH)

from selenium import webdriver
from urllib.parse import unquote

BEHAVE_DEBUG_ON_ERROR = False

def before_all(context):
    
    browser = context.config.userdata['browser']
    language = context.config.userdata['language']

    # Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument("--lang=en")
    browser_language = {'intl.accept_languages': 'en,en_US'}

    context.driver = webdriver.Chrome(executable_path=os.path.dirname(os
                                          .path.realpath(__file__)) +
                                          "/resources/chromedriver",
                                          chrome_options=options)
     # Environment
    context._url = context.config.userdata['_url']

    # Language
    context.language = language

    # Browser manipulation
    context.driver.implicitly_wait(10)
    context.driver.maximize_window()

def after_all(context):
    context.driver.quit() 
