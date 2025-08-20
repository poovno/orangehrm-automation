from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # wait up to 10 seconds

        self.username = (By.NAME, "username")
        self.password = (By.NAME, "password")
        self.login_button = (By.CSS_SELECTOR, "button[type='submit']")

    def enter_username(self, uname):
        self.wait.until(EC.visibility_of_element_located(self.username)).send_keys(uname)

    def enter_password(self, pwd):
        self.wait.until(EC.visibility_of_element_located(self.password)).send_keys(pwd)

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()
