from time import sleep

from pageObjects.landingPage import LandingPage
from pageObjects.loginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_002_Login:
    url = ReadConfig.getApplication_URL()
    userName = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_login(self, setup):
        self.logger.info("Test_002_Login")
        self.driver = setup
        self.driver.get(self.url)
        self.landingPage = LandingPage(self.driver)
        self.landingPage.clickSignIn()
        sleep(2)

        self.loginpage = LoginPage(self.driver)
        self.loginpage.enterUserName(self.userName)
        self.loginpage.enterPassword(self.password)
        self.loginpage.clickonLoginbtn()
        sleep(2)
        welcomeMg = self.loginpage.getWelcomeMsg()
        # print(welcomeMg)
        #
        assert self.userName in welcomeMg

        self.driver.quit()





