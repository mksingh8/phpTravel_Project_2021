from time import sleep

from pageObjects.landingPage import LandingPage
from pageObjects.signupPage import SignupPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_SignUp:
    url = ReadConfig.getApplication_URL()
    # url = "https://www.demoblaze.com/"
    userName = ReadConfig.getUserName()
    # userName = "admin02"
    password = ReadConfig.getPassword()
    # password = "admin"
    log = LogGen.loggen()

    def test_signup(self, setup):
        print("##########Test_001_SignUp#########")
        self.log.info("********Test_001_SignUp*******")
        self.log.info("starting browser and navigating to the phpTravel site")
        self.driver = setup
        self.driver.get(self.url)
        self.log.info("Initiating landing page Object")
        self.landingPage = LandingPage(self.driver)
        self.log.info("Clicking on Signup Page")
        self.landingPage.clickSignUp()
        sleep(2)

        self.sp = SignupPage(self.driver)
        self.log.info("Setting up user credentials")
        self.sp.setUserName(self.userName)
        self.sp.setPassword(self.password)
        self.sp.clickSignUp()
        sleep(2)
        # print(self.sp.getPopUpMsg())
        self.log.info(self.sp.getPopUpMsg())
        self.sp.closeSignUpWindow()
        self.log.info("CLosing the signup pop up window")

        self.driver.quit()
