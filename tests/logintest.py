import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.dashboard import DashboardPage

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_valid_login(setup):
    driver = setup
    login = LoginPage(driver)
    dashboard = DashboardPage(driver)

    login.enter_username("Admin")
    login.enter_password("admin123")
    login.click_login()

    assert "dashboard" in driver.current_url.lower()
    dashboard.logout()
