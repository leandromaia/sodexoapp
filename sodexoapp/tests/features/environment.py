import os
from selenium import webdriver
from splinter import Browser

def before_feature(context, feature):
#    chromedriver = "/var/www/workspace/selenium/features/chromedriver"
#    os.environ["webdriver.chrome.driver"] = chromedriver
#   context.driver = webdriver.Chrome()
#   context.driver.implicitly_wait(30)
#   context.driver.maximize_window()

#SPLINTER
#    context.driver = Browser('chrome')

	context.driver = Browser('phantomjs')
#   context.driver.set_window_size(1024, 768)
#   context.driver = webdriver.PhantomJS()
#   context.driver.set_window_size(1024, 768)
#    context.driver.set_window_size(1024, 768)
#
#def before_feature(context, feature):
#    context.driver = webdriver.Firefox()
#    context.driver.implicitly_wait(30)
#    context.driver.maximize_window()

def after_feature(context, feature):
	context.driver.quit()

