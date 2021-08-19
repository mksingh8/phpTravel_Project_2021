import inspect
from time import sleep

from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
import logging

txt_username = "//input[@id='sign-username']"
txt_password = "//input[@id='sign-password']"
btn_signup = "//button[contains(text(),'Sign up')]"
logging.basicConfig(filename="testLOg.log", format='%(asctime)s: %(levelname)s: %(name)s: %(message)s', level=logging.INFO)
loggerName = inspect.stack()[0][3]
print("*****************************")
print(loggerName)
log = logging.getLogger()

log.info("setting up the chrome option")
option = Options()
option.add_argument('--no-sandbox')
# option.add_argument('--headless')

# option.binary_location = "/etc/firefox"
# driver = webdriver.Firefox(executable_path="/home/manish/Documents/browsers/geckodriver", options=option)
log.info("initiating browser and navigating to the webpage")
driver = webdriver.Chrome(executable_path="/home/manish/Documents/browsers/chromedriver", options=option)
# driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install(), options=option)
driver.get("https://www.demoblaze.com/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element_by_css_selector("#login2").click()
# driver.find_element_by_css_selector("#signin2").click()
# driver.find_element_by_xpath(txt_username).send_keys("admin01")
# driver.find_element_by_xpath(txt_password).send_keys("admin")
# # driver.find_element_by_xpath(btn_signup).click()
# sleep(2)
# alert = driver.switch_to.alert
# print(alert.text)
# # alert_text = alert.text
# # print(alert_text)
# alert.accept()

sleep(2)
driver.quit()
