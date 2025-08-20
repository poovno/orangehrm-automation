import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.dashboard import DashboardPage
from pages.pim import PimPage

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_add_and_verify_employees(setup):
    driver = setup
    login = LoginPage(driver)
    dashboard = DashboardPage(driver)
    pim = PimPage(driver)

    
    login.enter_username("Admin")
    login.enter_password("admin123")
    login.click_login()


    dashboard.go_to_pim()

    employees = [("John", "Doe"), ("Jane", "Smith"), ("David", "Brown")]
    
   
    for fname, lname in employees:
        pim.add_employee(fname, lname)


    for fname, lname in employees:
        pim.search_employee(fname)
        assert fname in driver.page_source
        print(f"{fname} Verified")

   
    dashboard.logout()
