from selenium import webdriver


class LoginPage:

    textbox_username_id = "loginusername"
    textbox_password_id = "loginpassword"
    btn_login_xpath = "//button[contains(text(),'Log in')]"
    btn_close_xpath = "//button[contains(text(),'Log in')]//parent::div/button"
    link_welcomeMsg_CSS = "#nameofuser"
    link_logout_CSS = "#logout2"

    # constructor
    def __init__(self, driver):
        self.driver = driver

    # driver = webdriver.Chrome()

    def enterUserName(self, userName):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(userName)

    def enterPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickonLoginbtn(self):
        self.driver.find_element_by_xpath(self.btn_login_xpath).click()

    def clickonClosebtn(self):
        self.driver.find_element_by_xpath(self.btn_close_xpath).click()

    def getWelcomeMsg(self):
        welcomeMsg = self.driver.find_element_by_css_selector(self.link_welcomeMsg_CSS).text
        return welcomeMsg

    def clickonLogOutbtn(self):
        self.driver.find_element_by_css_selector(self.link_logout_CSS).click()


    # def clickonLogOutbtn(self):
    #     self.driver.find_element_by_link_text(self.link_text_logout).click()
    #

