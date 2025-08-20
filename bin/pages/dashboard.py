from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.profile_dropdown = (By.CLASS_NAME, "oxd-userdropdown-tab")
        self.logout_button = (By.XPATH, "//a[text()='Logout']")
        # Add locator for PIM menu link
        self.pim_menu = (By.XPATH, "//a[@href='/web/index.php/pim/viewPimModule']")

    def go_to_pim(self):
        # Wait for PIM menu to be clickable and click
        self.wait.until(EC.element_to_be_clickable(self.pim_menu)).click()

    def logout(self):
        self.wait.until(EC.element_to_be_clickable(self.profile_dropdown)).click()
        self.wait.until(EC.element_to_be_clickable(self.logout_button)).click()
