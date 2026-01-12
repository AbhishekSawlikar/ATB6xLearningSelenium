import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException


@allure.title("stale_element")
@allure.description("stale_element")
def test_stale_element_exp_demo():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    try:
        textarea = driver.find_element(By.NAME, "q")
        driver.refresh()
        textarea.send_keys("The Testing Academy")
        print("ENd of the test")
    except StaleElementReferenceException as see:
        print(see.msg)
    time.sleep(5)

    # response = {'status': 404, 'value': '{"value":{"error":"stale element reference","message":"stale element reference: stale elemen