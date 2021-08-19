from selenium import webdriver
from selenium.webdriver.common.alert import Alert


class SignupPage:

    txt_username = "//input[@id='sign-username']"
    txt_password = "//input[@id='sign-password']"
    btn_signup = "//button[contains(text(),'Sign up')]"
    btn_close = "//div[@id='signInModal']//button[contains(text(),'Close')]"
    #

    # driver = webdriver.Chrome
    # driver.switch_to.alert()

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element_by_xpath(self.txt_username).clear()
        self.driver.find_element_by_xpath(self.txt_username).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.txt_password).clear()
        self.driver.find_element_by_xpath(self.txt_password).send_keys(password)

    def clickSignUp(self):
        self.driver.find_element_by_xpath(self.btn_signup).click()

    def getPopUpMsg(self):
        alert = self.driver.switch_to.alert
        alert_mdg = alert.text
        alert.accept()
        return alert_mdg

    def closeSignUpWindow(self):
        self.driver.find_element_by_xpath(self.btn_close).click()




