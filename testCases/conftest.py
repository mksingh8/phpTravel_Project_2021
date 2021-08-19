import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def setup():
    option = Options()
    option.add_argument('--no-sandbox')
    option.add_experimental_option('useAutomationExtension', False)
    # option.add_argument('--headless')
    # option.add_argument("--disable-xss-auditor")
    # option.add_argument("--disable-web-security")
    # option.add_argument("--allow-running-insecure-content")
    # option.add_argument("--no-sandbox")
    # option.add_argument("--disable-setuid-sandbox")
    # option.add_argument("--disable-webgl")
    # option.add_argument("--disable-popup-blocking")
    # option.add_argument("window-size=1500,1200")
    # option.add_argument("disable-dev-shm-usage")
    # option.add_argument("disable-gpu")
    # option.add_argument("log-level=3")
    driver = webdriver.Chrome(executable_path="/home/manish/Documents/browsers/chromedriver", options=option)
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver
