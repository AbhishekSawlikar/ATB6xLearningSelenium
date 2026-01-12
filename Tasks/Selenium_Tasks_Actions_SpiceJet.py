import allure
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

@allure.title("SpiceJet City selection")
@allure.description("To verify that the From - Delhi and To - Chandigarh cities are selected.")
def test_spiceJet():
    driver = webdriver.Chrome()
    driver.get("https://www.spicejet.com/")
    driver.maximize_window()

    fromCity = driver.find_element(By.XPATH, "//div[@data-testid='to-testID-origin']//input[@type='text']")
    fromCity.send_keys("DEL")

    time.sleep(2)

    toCity = driver.find_element(By.XPATH, "//div[@data-testid='to-testID-destination']//input[@type='text']")
    toCity.send_keys("IXC")

    time.sleep(5)

    driver.quit()