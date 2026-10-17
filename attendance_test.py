"""
attendance_test.py - Automated attendance-marking test for AttendX.
Tool   : Selenium WebDriver (Python) + pytest
Run    : pytest attendance_test.py -v
"""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "http://localhost:3000"   # change to your AttendX URL


@pytest.fixture
def driver():
    drv = webdriver.Chrome()
    drv.implicitly_wait(5)
    yield drv
    drv.quit()


def login_as_teacher(driver):
    driver.get(f"{BASE_URL}/login")
    driver.find_element(By.ID, "username").send_keys("teacher01")
    driver.find_element(By.ID, "password").send_keys("Pass@123")
    driver.find_element(By.ID, "loginBtn").click()
    WebDriverWait(driver, 10).until(EC.url_contains("/dashboard"))


def test_mark_attendance(driver):
    login_as_teacher(driver)
    driver.get(f"{BASE_URL}/attendance")
    Select(driver.find_element(By.ID, "classSelect")).select_by_visible_text("IT-A")
    driver.find_element(By.CSS_SELECTOR, "input[data-student='1'][value='present']").click()
    driver.find_element(By.ID, "saveAttendance").click()
    msg = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "successMsg"))).text
    assert "saved" in msg.lower()
