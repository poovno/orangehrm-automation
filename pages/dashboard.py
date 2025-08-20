from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.pim_menu = (By.XPATH, "//span[text()='PIM']")
        self.profile_dropdown = (By.CLASS_NAME, "oxd-userdropdown-tab")
        self.logout_button = (By.XPATH, "//a[text()='Logout']")

    def go_to_pim(self):
        self.driver.find_element(*self.pim_menu).click()

    def logout(self):
        self.driver.find_element(*self.profile_dropdown).click()
        self.driver.find_element(*self.logout_button).click()
