"""
Mini Project #1 (Selenium)
// Locators - Find the Web elements
// Open the URL https://app.vwo.com/#/login
// Find the Email id** and enter the email as admin@admin.com
// Find the Pass inputbox** and enter passwrod as admin.
// Find and Click on the submit button
// Verify that the error message is shown "_**Your email, password, IP address or location did not match"**_

"""
import time
import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def test_selenium_homework_task1():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://app.vwo.com/#/login")
    print(driver.current_url)

    # Find the element of the email address and password fields and clicking on Submit button
    email_address = driver.find_element(By.ID, "login-username")
    email_address.send_keys("admin@admin.com")
    password = driver.find_element(By.ID, "login-password")
    password.send_keys("admin")
    sign_in = driver.find_element(By.ID, "js-login-btn")
    sign_in.click()
    time.sleep(2)

    # Verifying the error message after submitting the invalid credentials
    error_message = driver.find_element(By.ID, "js-notification-box-msg")
    print(error_message.text)

    assert "Your email, password, IP address or location did not match" == error_message.text
    time.sleep(2)
    driver.quit()