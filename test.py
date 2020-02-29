from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

from credentials import *


chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=chrome_options)


driver.get("https://www.facebook.com/")

name_form = driver.find_element_by_name("email")
pw_form = driver.find_element_by_name("pass")

name_form.clear()
name_form.send_keys(username)

pw_form.clear()
pw_form.send_keys(password)

submit_form = driver.find_elements_by_xpath(
    "/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[3]/label/input")[0].click()

events_button = driver.find_elements_by_xpath(
    "/html/body/div[1]/div[3]/div[1]/div/div[2]/div[1]/div/div/div/div/div[3]/div[3]/ul/li[1]/a/div[2]")[0].click()

print(driver.current_url)
sleep(2)

bdays_button = driver.find_element_by_xpath(
    "/html/body/div[1]/div[3]/div[1]/div/div[1]/div/div/div[2]/div[3]")
print(bdays_button)
