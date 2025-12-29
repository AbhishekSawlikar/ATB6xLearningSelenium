"""
Mini Project #2 (Selenium)

// Locators - Find the Web elements

// Open the URL: www.idrive360.com/enterprise/account?upgradenow=true

// Find the Email id** and enter the email as augtest_040823@idrive.com

// Find the Pass inputbox** and enter password as 123456.

// Find and Click on the Sigin button

// Verify that the message is shown "Your free trail has expired"

"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

def test_selenium_homework_task2():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://www.idrive360.com/enterprise/account?upgradenow=true")

    wait = WebDriverWait(driver, 15)

    # Wait for and enter email
    email_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    email_input.send_keys("augtest_040823@idrive.com")

    # Wait for and enter password
    password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    password_input.send_keys("123456")

    # Click Sign In
    sign_in_button = wait.until(EC.element_to_be_clickable((By.ID, "frm-btn")))
    sign_in_button.click()

    # Verify "Your free trial has expired!" message
    expired_msg = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "id-card-title")))
    assert expired_msg.text.strip() == "Your free trial has expired!"

    # Verify header message
    header_msg = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Your free trial has expired']")))
    assert header_msg.text.strip() == "Your free trial has expired"

    # Verify Upgrade Now button
    upgrade_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.id-btn.id-warning-btn-drk.id-tkn-btn")))
    assert upgrade_button.text.strip() == "Upgrade Now!"

    driver.quit()