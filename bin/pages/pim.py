# pim.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PimPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Navigation and Add Employee
        self.pim_tab = (By.XPATH, "//span[text()='PIM']")
        self.add_employee_button = (By.LINK_TEXT, "Add Employee")
        self.first_name_field = (By.NAME, "firstName")
        self.last_name_field = (By.NAME, "lastName")
        self.save_button = (By.XPATH, "//button[@type='submit']")
        self.employee_list = (By.LINK_TEXT, "Employee List")

        # Search-related locators
        self.filter_button = (By.CSS_SELECTOR, "button[aria-label='filter']")
        self.employee_name_field = (By.XPATH, "//label[contains(text(), 'Employee Name')]/following-sibling::div//input")
        self.search_button = (By.XPATH, "//button[@type='submit' and .='Search']")
        self.table_rows = (By.CSS_SELECTOR, ".oxd-table-body .oxd-table-row")

    def add_employee(self, first_name, last_name):
        self.wait.until(EC.element_to_be_clickable(self.add_employee_button)).click()
        self.wait.until(EC.visibility_of_element_located(self.first_name_field)).send_keys(first_name)
        self.driver.find_element(*self.last_name_field).send_keys(last_name)
        self.driver.find_element(*self.save_button).click()

        # Wait for confirmation that the employee is added
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//h6[contains(text(), 'Personal Details')]")))

        # Go back to employee list
        self.wait.until(EC.element_to_be_clickable(self.employee_list)).click()

    def search_employee(self, name):
        # Open Employee List tab
        self.wait.until(EC.element_to_be_clickable(self.employee_list)).click()

        # Wait for any spinner to disappear
        self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "oxd-loading-spinner")))

        # Click filter button to reveal search fields
        self.wait.until(EC.element_to_be_clickable(self.filter_button)).click()

        # Type in employee name
        self.wait.until(EC.visibility_of_element_located(self.employee_name_field)).send_keys(name)

        # Click Search
        self.wait.until(EC.element_to_be_clickable(self.search_button)).click()

        # Wait for results to load
        self.wait.until(EC.visibility_of_all_elements_located(self.table_rows))

        # Verify if the employee appears in results
        rows = self.driver.find_elements(*self.table_rows)
        for row in rows:
            if name.lower() in row.text.lower():
                return True
        return False


