import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_javascript_alerts_prompt():
    driver = webdriver.Chrome()
    driver.get("https://www.makemytrip.com/")

    WebDriverWait(driver=driver, timeout=5).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//span[@data-cy='closeModal']")
        ))

    element_close_modal = driver.find_element(By.XPATH, "//span[@data-cy='closeModal']")
    element_close_modal.click()

    time.sleep(5)
    driver.quit()