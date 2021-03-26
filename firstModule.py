from selenium import webdriver
import time

browser = webdriver.Chrome("/Users/nongluck/Downloads/chromedriver 2")

browser.maximize_window()
time.sleep(3)

browser.get("https://www.amazon.com")
time.sleep(3)

browser.quit()
