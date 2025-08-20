from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PimPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.add_employee_btn = (By.XPATH, "//*[normalize-space(text())='Add Employee']")
        self.first_name = (By.NAME, "firstName")
        self.last_name = (By.NAME, "lastName")
        self.save_btn = (By.XPATH, "//button[@type='submit']")
        self.employee_list = (By.XPATH, "//*[normalize-space(text())='Employee List']")
        self.search_box = (By.XPATH, "//input[@placeholder='Type for hints...']")
        self.search_btn = (By.XPATH, "//button[@type='submit']")

    def add_employee(self, fname, lname):
        self.wait.until(EC.element_to_be_clickable(self.add_employee_btn)).click()
        self.wait.until(EC.visibility_of_element_located(self.first_name)).send_keys(fname)
        self.driver.find_element(*self.last_name).send_keys(lname)
        self.driver.find_element(*self.save_btn).click()

    def search_employee(self, name):
        self.wait.until(EC.element_to_be_clickable(self.employee_list)).click()
        self.wait.until(EC.visibility_of_element_located(self.search_box)).send_keys(name)
        self.driver.find_element(*self.search_btn).click()
