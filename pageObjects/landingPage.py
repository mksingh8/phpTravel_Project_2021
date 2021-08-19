from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LandingPage:
    link_signup = "#signin2"
    link_signin = "#login2"
    link_cart = "#cartur"
    link_home = "//a[contains(text(),'Home')]"

    def __init__(self, driver):
        self.driver = driver

    def clickSignUp(self):
        self.driver.find_element_by_css_selector(self.link_signup).click()

    def clickSignIn(self):
        self.driver.find_element_by_css_selector(self.link_signin).click()

    def clickCart(self):
        self.driver.find_element_by_css_selector(self.link_cart).click()

    def clickSignIn(self):
        # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.link_signin)))
        self.driver.find_element_by_css_selector(self.link_signin).click()
