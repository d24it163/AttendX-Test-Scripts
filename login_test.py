"""
login_test.py - Automated login test for the AttendX attendance app.
Tool   : Selenium WebDriver (Python) + pytest
Run    : pytest login_test.py -v
Note   : BASE_URL points to the demo/local AttendX instance.
"""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "http://localhost:3000"   # change to your AttendX URL


@pytest.fixture
def driver():
    drv = webdriver.Chrome()
    drv.implicitly_wait(5)
    yield drv
    drv.quit()


def login(driver, username, password):
    driver.get(f"{BASE_URL}/login")
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "loginBtn").click()


def test_valid_login(driver):
    login(driver, "teacher01", "Pass@123")
    WebDriverWait(driver, 10).until(EC.url_contains("/dashboard"))
    assert "Dashboard" in driver.title


def test_invalid_password(driver):
    login(driver, "teacher01", "wrong")
    msg = driver.find_element(By.ID, "errorMsg").text
    assert "Invalid" in msg


def test_empty_fields(driver):
    login(driver, "", "")
    msg = driver.find_element(By.ID, "errorMsg").text
    assert "required" in msg.lower()
