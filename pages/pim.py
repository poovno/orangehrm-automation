from selenium.webdriver.common.by import By

class PimPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_employee_button = (By.LINK_TEXT, "Add Employee")
        self.first_name = (By.NAME, "firstName")
        self.last_name = (By.NAME, "lastName")
        self.save_button = (By.XPATH, "//button[@type='submit']")
        self.employee_list = (By.LINK_TEXT, "Employee List")
        self.search_box = (By.XPATH, "//input[@placeholder='Type for hints...']")
        self.search_button = (By.XPATH, "//button[@type='submit']")

    def add_employee(self, fname, lname):
        self.driver.find_element(*self.add_employee_button).click()
        self.driver.find_element(*self.first_name).send_keys(fname)
        self.driver.find_element(*self.last_name).send_keys(lname)
        self.driver.find_element(*self.save_button).click()

    def search_employee(self, name):
        self.driver.find_element(*self.employee_list).click()
        self.driver.find_element(*self.search_box).send_keys(name)
        self.driver.find_element(*self.search_button).click()
